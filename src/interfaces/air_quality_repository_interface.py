import abc


class AirQualityRepositoryInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'fetch_by_city') and
                callable(subclass.fetch_by_city) and
                hasattr(subclass, 'fetch_by_coordinates') and
                callable(subclass.fetch_by_coordinates) and
                hasattr(subclass, 'parse_source') and
                callable(subclass.parse_source) and
                hasattr(subclass, 'format_data') and
                callable(subclass.calculate_level) and
                hasattr(subclass, 'insert_field') and
                callable(subclass.format_data))

    def fetch_by_city(self, date, city):
        pass

    def fetch_by_coordinates(self, date, x, y, z):
        pass

    @staticmethod
    def parse_source(source):
        pass

    def format_data(self, data):
        pass

    def insert_field(self, obj, field):
        pass