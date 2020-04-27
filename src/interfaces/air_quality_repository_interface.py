import abc


class AirQualityRepositoryInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'fetch_by_city') and
                callable(subclass.fetch_by_city) and
                hasattr(subclass, 'fetch_by_coordinates'))

    def fetch_by_city(self, date_from, date_to, city):
        pass

    def fetch_by_coordinates(self, date, x, y, z):
        pass

