from interfaces.air_quality_repository_interface import AirQualityRepositoryInterface


class GetCityMonthAirQuality:
    def __init__(self, repo: AirQualityRepositoryInterface):
        self.repo = repo

    def get_city_month_air_quality(self, month, year, city):
        return self.repo.fetch_by_city_month(month, year, city)
