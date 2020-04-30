from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import requests
from copy import deepcopy
from itertools import groupby
from .endpoints import OpenAqEndpoints
from .params import OpenAqRequestParams, OpenAqDataFields, \
    Skeletons, GeoJsonKeys
from ...operations.beans import OperationsBeans


class AirQualityApi(AirQualityRepositoryInterface):
    def __init__(self):
        self.mappings = OperationsBeans.MAPPINGS.value
        self.aggs = OperationsBeans.AGGREGATIONS.value

    def fetch_by_city(self, date_from, date_to, city):
        result = deepcopy(Skeletons.GEOJSONPARENT.value)
        aq_raw = self.fetch_from_source(date_from, date_to, city)
        temp_data = self.get_field(aq_raw,
                                   OpenAqDataFields.RESULTS.value)
        groups = groupby(temp_data,
                         key=lambda d: (d[OpenAqDataFields.COORDINATES.value],
                                        d[OpenAqDataFields.PARAMETER.value]))
        for x, y in groups:
            y_list = list(y)
            mean = self.aggs.calculate_mean(y_list)
            level = self.mappings.get_pollution_level(mean)
            el = y_list.pop(0)
            self.insert_field(el, OpenAqDataFields.MEAN.value, mean)
            self.insert_field(el, OpenAqDataFields.LEVEL.value, level)
            result.get(GeoJsonKeys.FEATURES.value)\
                .append(self.to_geojson_feature(el))
        return result

    @staticmethod
    def fetch_from_source(date_from, date_to, city):
        params = {OpenAqRequestParams.CITY.value: city,
                  OpenAqRequestParams.FROM.value: date_from,
                  OpenAqRequestParams.TO.value: date_to}
        return requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                            params=params).json()

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
        latitud = json_coordinates.get(OpenAqDataFields.LATITUDE.value)
        longitud = json_coordinates.get(OpenAqDataFields.LONGITUDE.value)
        return [latitud, longitud]

    def to_geojson_feature(self, json):
        geojson = deepcopy(Skeletons.GEOJSONPOINT.value)
        coordinates_key = OpenAqDataFields.COORDINATES.value
        coordinates = self.coordinates_json_to_list(json.get(coordinates_key))
        self.insert_field(geojson.get(GeoJsonKeys.GEOMETRY.value),
                          coordinates_key, coordinates)
        self.insert_field(geojson.get(GeoJsonKeys.PROPERTIES.value),
                          json.get(OpenAqDataFields.PARAMETER.value),
                          json.get(OpenAqDataFields.MEAN.value))
        self.insert_field(geojson.get(GeoJsonKeys.PROPERTIES.value),
                          OpenAqDataFields.LEVEL.value,
                          json.get(OpenAqDataFields.LEVEL.value))
        return geojson
