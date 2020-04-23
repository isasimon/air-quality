from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import requests
import json
from datetime import datetime, timedelta
from .endpoints import OpenAqEndpoints
from .params import OpenAqParams


class AirQualityApi(AirQualityRepositoryInterface):
    def fetch_by_city(self, date_to, city):
        date_from = self.date_from(date_to)
        params = {OpenAqParams.CITY.value: city,
                  OpenAqParams.FROM.value: date_from,
                  OpenAqParams.TO.value: date_to}
        aq = requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                          params=params).json()
        return self.parse_source(aq)

    @staticmethod
    def date_from(date_to):
        delta = timedelta(days=1)
        datetime_to = datetime.strptime(date_to, '%Y-%m-%d')
        datetime_from = datetime_to - delta
        return datetime_from.strftime('%Y-%m-%d')

    @staticmethod
    def parse_source(source):
        return json.dumps(source, indent=2)

    def format_data(self, data):
        pass

    def insert_field(self, obj, field):
        pass


