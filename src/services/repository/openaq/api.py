from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import requests
from itertools import groupby
from .endpoints import OpenAqEndpoints
from .params import OpenAqRequestParams, OpenAqDataFields
from ...operations.beans import OperationsBeans


class AirQualityApi(AirQualityRepositoryInterface):
    def __init__(self):
        self.mappings = OperationsBeans.MAPPINGS.value
        self.aggs = OperationsBeans.AGGREGATIONS.value

    def fetch_by_city(self, date_from, date_to, city):
        result = []
        aq_raw = self.fetch_from_source(date_from, date_to, city)
        temp_data = self.get_field(aq_raw,
                                   OpenAqDataFields.RESULTS.value)
        groups = groupby(temp_data,
                         key=lambda d: d[OpenAqDataFields.COORDINATES.value])
        for x, y in groups:
            y_list = list(y)
            mean = self.aggs.calculate_mean(y_list)
            level = self.mappings.get_pollution_level(mean)
            el = y_list.pop(0)
            self.insert_field(el, OpenAqDataFields.MEAN.value, mean)
            self.insert_field(el, OpenAqDataFields.LEVEL.value, level)
            result.append(el)
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
