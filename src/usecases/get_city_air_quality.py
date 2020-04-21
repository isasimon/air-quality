from interfaces.air_quality_repository_interface import AirQualityRepositoryInterface


class GetCityAirQuality:
    def __init__(self, air_quality_repo: AirQualityRepositoryInterface):
        self.repo = air_quality_repo

    def get_city_air_quality(self, date, city):
        return self.repo.fetch_by_city(date, city)
