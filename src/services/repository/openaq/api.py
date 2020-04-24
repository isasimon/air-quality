from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import requests
from datetime import datetime, timedelta
from .endpoints import OpenAqEndpoints
from .params import OpenAqRequestParams, OpenAqDataFields, \
    OpenAqDataFormat
from .measurement_levels import MeasurementLevels


class AirQualityApi(AirQualityRepositoryInterface):
    def fetch_by_city(self, date_to, city):
        date_from = self.date_from(date_to)
        params = {OpenAqRequestParams.CITY.value: city,
                  OpenAqRequestParams.FROM.value: date_from,
                  OpenAqRequestParams.TO.value: date_to}
        aq = requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                          params=params).json()
        parsed_data = self.get_field(aq,
                                     OpenAqDataFields.RESULTS.value)
        return self.format_data(parsed_data)

    @staticmethod
    def date_from(date_to):
        delta = timedelta(days=1)
        datetime_to = datetime.strptime(date_to,
                                        OpenAqDataFormat.DATE_TO.value)
        datetime_from = datetime_to - delta
        return datetime_from.strftime(OpenAqDataFormat.DATE_FROM.value)

    @staticmethod
    def get_field(source, field):
        return source[field]

    def format_data(self, data):
        parameter = OpenAqDataFields.PARAMETER.value
        value = OpenAqDataFields.VALUE.value
        date = OpenAqDataFields.DATE.value
        city = OpenAqDataFields.CITY.value
        country = OpenAqDataFields.COUNTRY.value
        coordinates = OpenAqDataFields.COORDINATES.value
        level = OpenAqDataFields.LEVEL.value
        return [{parameter: x[parameter],
                 value: x[value],
                 date: x[date],
                 city: x[city],
                 country: x[country],
                 coordinates: x[coordinates],
                 level: self.calculate_level(x[value])}
                for x in data]

    @staticmethod
    def insert_field(self, obj, field):
        pass

    @staticmethod
    def calculate_level(measurement):
        ml = MeasurementLevels()
        return ml.calculate_level(measurement)

