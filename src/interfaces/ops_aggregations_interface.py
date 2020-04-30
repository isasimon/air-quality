import abc


class AggregationsInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'calculate_mean') and
                callable(subclass.calculate_mean))

    @staticmethod
    def calculate_mean(data_list):
        pass

