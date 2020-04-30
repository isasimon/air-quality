import abc


class AirQualityRepositoryInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'fetch_by_city') and
                callable(subclass.fetch_by_city) and
                hasattr(subclass, 'to_geojson_feature') and
                callable(subclass.to_geojson_feature))

    def fetch_by_city(self, date_from, date_to, city):
        pass

    def to_geojson_feature(self, json):
        pass


