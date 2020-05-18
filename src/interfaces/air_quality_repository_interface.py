import abc


class AirQualityRepositoryInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'fetch_by_city') and
                callable(subclass.fetch_by_city) and
                hasattr(subclass, 'fetch_by_city_month') and
                callable(subclass.fetch_by_city_month) and
                hasattr(subclass, 'fetch_by_country') and
                callable(subclass.fetch_by_country) and
                hasattr(subclass, 'generate_geojson') and
                callable(subclass.to_geojson_feature))

    def fetch_by_city(self, date_from, date_to, city):
        pass

    def fetch_by_city_month(self, month, year, city):
        pass

    def fetch_by_country(self, date_from, date_to, city):
        pass

    def generate_geojson(self, raw_data):
        pass


