import abc


class Mappings(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_pollution_level') and
                callable(subclass.get_pollution_level))

    def get_pollution_level(self, measurement):
        pass
