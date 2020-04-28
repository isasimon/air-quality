from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import requests
from itertools import groupby
from .endpoints import OpenAqEndpoints
from .params import OpenAqRequestParams, OpenAqDataFields
from .measurement import Measurement


class AirQualityApi(AirQualityRepositoryInterface):
    def fetch_by_city(self, date_from, date_to, city):
        m = Measurement()
        aq = self.fetch_from_source(date_from, date_to, city)
        temp_data = self.get_field(aq,
                                   OpenAqDataFields.RESULTS.value)
        groups = groupby(temp_data,
                         key=lambda d: d[OpenAqDataFields.COORDINATES.value])
        els = []
        for x, y in groups:
            y_list = list(y)
            mean = m.calculate_mean(y_list)
            level = m.calculate_level(mean)
            el = y_list.pop(0)
            self.insert_field(el, OpenAqDataFields.MEAN.value, mean)
            self.insert_field(el, OpenAqDataFields.LEVEL.value, level)
            els.append(el)
        return els

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
