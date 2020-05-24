from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import requests
from datetime import datetime
from calendar import monthrange
from ..params import RequestParams, DateFormat
from ...endpoints import OpenAqEndpoints
from services.repository.openaq.operations.geojson_treatment import GeaojsonTreatment


class OpenAqApi(AirQualityRepositoryInterface):
    def __init__(self):
        self.geojson_service = GeaojsonTreatment()

    def fetch_by_city(self, date_from, date_to, city):
        params = {RequestParams.CITY.value: city,
                  RequestParams.FROM.value: date_from,
                  RequestParams.TO.value: date_to}
        raw_data = requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                                params=params).json()
        return self.geojson_service.geojson(raw_data)

    def fetch_by_country(self, date_from, date_to, country):
        params = {RequestParams.COUNTRY.value: country,
                  RequestParams.FROM.value: date_from,
                  RequestParams.TO.value: date_to}
        raw_data = requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                                params=params).json()
        return self.geojson_service.geojson(raw_data)

