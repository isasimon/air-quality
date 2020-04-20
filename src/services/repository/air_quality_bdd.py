from interfaces.air_quality_repository_interface \
    import AirQualiryRepositoryInterface


class AirQualityBdd(AirQualiryRepositoryInterface):
    def fetch_by_city(self, date, city):
        return "Date: {}. City: {}".format(date, city)

    def fetch_by_coordinates(self, date, x, y, z):
        return "Date: {}. Coordinates: {}, {}, {}".format(date, x, y, z)
