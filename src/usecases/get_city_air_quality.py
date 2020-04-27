from class_configuration import ClassConfiguration


class GetCityAirQuality:
    def __init__(self, configuration: ClassConfiguration):
        self.repo = configuration.REPOSITORY

    def get_city_air_quality(self, date_from, date_to, city):
        return self.repo.fetch_by_city(date_from, date_to, city)
