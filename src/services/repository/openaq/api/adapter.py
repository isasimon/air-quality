from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import requests
from ..params import RequestParams
from ...endpoints import OpenAqEndpoints
from services.repository.openaq.operations.geojson_treatment \
    import GeaojsonTreatment
from services.repository.openaq.params import DataFields


class OpenAqApi(AirQualityRepositoryInterface):
    def __init__(self):
        self.geojson_service = GeaojsonTreatment()

    def fetch_by_city(self, date_from, date_to, city):
        params = {RequestParams.CITY.value: city,
                  RequestParams.FROM.value: date_from,
                  RequestParams.TO.value: date_to}
        raw_data = requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                                params=params).json()
        results = self.get_field(raw_data,
                                 DataFields.RESULTS.value)
        return self.geojson_service.geojson(results)

    def fetch_by_country(self, date_from, date_to, country):
        params = {RequestParams.COUNTRY.value: country,
                  RequestParams.FROM.value: date_from,
                  RequestParams.TO.value: date_to}
        raw_data = requests.get(OpenAqEndpoints.MEASUREMENTS.value,
                                params=params).json()
        return self.geojson_service.geojson(raw_data)

    @staticmethod
    def get_field(source, field):
        return source[field]

