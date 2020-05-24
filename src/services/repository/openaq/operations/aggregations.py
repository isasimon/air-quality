from functools import reduce
from ..params import DataFields


class Aggregations:
    @staticmethod
    def calculate_mean(data_list):
        s = reduce(lambda x, y: x + y[DataFields.VALUE.value],
                   data_list, 0.0)
        return s / len(data_list)
