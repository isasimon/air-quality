import abc


class AirQualiryRepositoryInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'fetch_by_city') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'fetch_by_coordinates') and
                callable(subclass.extract_text))

    def fetch_by_city(self, date, city):
        pass

    def fetch_by_coordinates(self, date, x, y, z):
        pass