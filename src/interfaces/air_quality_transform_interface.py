import abc


class AirQualityTransformationInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'parse_source') and
                callable(subclass.parse_source) and
                hasattr(subclass, 'format_data') and
                callable(subclass.calculate_level) and
                hasattr(subclass, 'insert_field') and
                callable(subclass.format_data))

    def parse_source(self, source):
        pass

    def format_data(self, data):
        pass

    def insert_field(self, obj, field):
        pass
