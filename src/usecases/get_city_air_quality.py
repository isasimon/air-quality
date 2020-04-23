from class_configuration import ClassConfiguration


class GetCityAirQuality:
    def __init__(self, configuration: ClassConfiguration):
        self.repo = configuration.REPOSITORY.value

    def get_city_air_quality(self, date, city):
        return self.repo.fetch_by_city(date, city)

