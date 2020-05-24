from copy import deepcopy
from itertools import groupby
from datetime import datetime
from services.repository.openaq.params import DataFields, DateFormat
from services.repository.openaq.params import GeoJsonKeys, Skeletons
from beans.operations import OperationsBeans


class GeaojsonTreatment:
    def __init__(self):
        self.mappings = OperationsBeans.MAPPINGS.value
        self.aggs = OperationsBeans.AGGREGATIONS.value

    def geojson(self, raw_data):
        result = deepcopy(Skeletons.GEOJSONPARENT.value)
        temp_data = self.get_field(raw_data,
                                   DataFields.RESULTS.value)
        groups = groupby(temp_data,
                         key=lambda d: (d[DataFields.COORDINATES.value],
                                        d[DataFields.PARAMETER.value]))
        for x, y in groups:
            y_list = list(y)
            mean = self.aggs.calculate_mean(y_list)
            el = y_list.pop(0)
            self.insert_field(el, DataFields.MEAN.value, mean)
            result.get(GeoJsonKeys.FEATURES.value) \
                .append(self.geojson_point(el))
        return result

    @staticmethod
    def get_field(source, field):
        return source[field]

    @staticmethod
    def insert_field(container, key, value):
        container[key] = value

    @staticmethod
    def delete_field(container, key):
        if key in container:
            del container[key]

    @staticmethod
    def coordinates_json_to_list(json_coordinates):
        latitude = json_coordinates.get(DataFields.LATITUDE.value)
        longitude = json_coordinates.get(DataFields.LONGITUDE.value)
        return [longitude, latitude]

    def geojson_point(self, json):
        geojson = deepcopy(Skeletons.GEOJSONPOINT.value)
        coordinates_key = DataFields.COORDINATES.value
        coordinates = self.coordinates_json_to_list(json.get(coordinates_key))
        mean = json.get(DataFields.MEAN.value)
        parameter = json.get(DataFields.PARAMETER.value)
        date_key = DataFields.DATE.value
        date = datetime.strptime(json.get(date_key)
                                 .get(DataFields.UTC.value),
                                 DateFormat.RESPONSE.value)
        self.insert_field(geojson.get(GeoJsonKeys.GEOMETRY.value),
                          coordinates_key, coordinates)
        self.insert_field(geojson.get(GeoJsonKeys.PROPERTIES.value),
                          parameter,
                          mean)
        self.insert_field(geojson.get(GeoJsonKeys.PROPERTIES.value),
                          date_key,
                          date.strftime(DateFormat.FINAL_RESULT.value))
        return geojson
