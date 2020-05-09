from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import requests
from copy import deepcopy
from itertools import groupby
from services.repository.api.endpoints import OpenAqEndpoints
from .params import OpenAqDataFields, \
    Skeletons, GeoJsonKeys
from ..common_params import RequestParams
from beans.operations import OperationsBeans


class AirQualityApi(AirQualityRepositoryInterface):
    def __init__(self):
        self.mappings = OperationsBeans.MAPPINGS.value
        self.aggs = OperationsBeans.AGGREGATIONS.value

    def fetch_by_city(self, date_from, date_to, city):
        params = {RequestParams.CITY.value: city,
                  RequestParams.FROM.value: date_from,
                  RequestParams.TO.value: date_to}
        raw_data = requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                                params=params).json()
        return self.geojson(raw_data)

    def fetch_by_country(self, date_from, date_to, country):
        params = {RequestParams.COUNTRY.value: country,
                  RequestParams.FROM.value: date_from,
                  RequestParams.TO.value: date_to}
        raw_data = requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                                params=params).json()
        return self.geojson(raw_data)

    def geojson(self, raw_data):
        result = deepcopy(Skeletons.GEOJSONPARENT.value)
        temp_data = self.get_field(raw_data,
                                   OpenAqDataFields.RESULTS.value)
        groups = groupby(temp_data,
                         key=lambda d: (d[OpenAqDataFields.COORDINATES.value],
                                        d[OpenAqDataFields.PARAMETER.value]))
        for x, y in groups:
            y_list = list(y)
            mean = self.aggs.calculate_mean(y_list)
            el = y_list.pop(0)
            self.insert_field(el, OpenAqDataFields.MEAN.value, mean)
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
        latitude = json_coordinates.get(OpenAqDataFields.LATITUDE.value)
        longitude = json_coordinates.get(OpenAqDataFields.LONGITUDE.value)
        return [longitude, latitude]

    def geojson_point(self, json):
        geojson = deepcopy(Skeletons.GEOJSONPOINT.value)
        coordinates_key = OpenAqDataFields.COORDINATES.value
        coordinates = self.coordinates_json_to_list(json.get(coordinates_key))
        self.insert_field(geojson.get(GeoJsonKeys.GEOMETRY.value),
                          coordinates_key, coordinates)
        self.insert_field(geojson.get(GeoJsonKeys.PROPERTIES.value),
                          json.get(OpenAqDataFields.PARAMETER.value),
                          json.get(OpenAqDataFields.MEAN.value))
        return geojson
