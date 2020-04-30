from interfaces.air_quality_repository_interface import AirQualityRepositoryInterface


class GetCountryAirQuality:
    def __init__(self, repo: AirQualityRepositoryInterface):
        self.repo = repo

    def get_country_air_quality(self, date_from, date_to, country):
        return self.repo.fetch_by_country(date_from, date_to, country)
