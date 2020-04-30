from interfaces.air_quality_repository_interface import AirQualityRepositoryInterface


class GetCityAirQuality:
    def __init__(self, repo: AirQualityRepositoryInterface):
        self.repo = repo

    def get_city_air_quality(self, date_from, date_to, city):
        return self.repo.fetch_by_city(date_from, date_to, city)
