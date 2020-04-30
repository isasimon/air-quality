from functools import reduce
from services.repository.openaq.params import OpenAqDataFields


class Aggregations:
    @staticmethod
    def calculate_mean(data_list):
        s = reduce(lambda x, y: x + y[OpenAqDataFields.VALUE.value],
                   data_list, 0.0)
        return s / len(data_list)
