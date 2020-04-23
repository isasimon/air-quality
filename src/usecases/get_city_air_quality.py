from class_configuration import ClassConfiguration


class GetCityAirQuality:
    def __init__(self, configuration: ClassConfiguration):
        self.repo = configuration.REPOSITORY.value
        self.transform = configuration.TRANSFORM.value

    def get_city_air_quality(self, date, city):
        data = self.repo.fetch_by_city(date, city)
        return self.transform.parse_source(data)
