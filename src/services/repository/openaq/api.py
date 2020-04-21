from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import requests
from datetime import datetime, timedelta
from .endpoints import OpenAqEndpoints
from .params import OpenAqParams


class AirQualityBdd(AirQualityRepositoryInterface):
    def fetch_by_city(self, date_to, city):
        date_from = self.date_from(date_to)
        params = {OpenAqParams.CITY.value: city,
                  OpenAqParams.FROM.value: date_from,
                  OpenAqParams.TO.value: date_to}
        aq = requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                          params=params).json()
        return aq

    def fetch_by_coordinates(self, date, x, y, z):
        return "Date: {}. Coordinates: {}, {}, {}".format(date, x, y, z)

    def date_from(self, date_to):
        delta = timedelta(days=1)
        datetime_to = datetime.strptime(date_to, '%Y-%m-%d')
        datetime_from = datetime_to - delta
        return datetime_from.strftime('%Y-%m-%d')
