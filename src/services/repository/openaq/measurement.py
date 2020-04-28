from functools import reduce
from .params import OpenAqDataFields


class Measurement:
    def __init__(self):
        good = ('good', range(50))
        moderate = ('moderate', range(51, 100))
        unhealthy_sensitive_groups = ('unhealthy_sensitive_groups',
                                      range(101, 150))
        unhealthy = ('unhealthy', range(151, 200))
        very_unhealthy = ('very_unhealthy', range(201, 300))
        self.levels = [good,
                       moderate,
                       unhealthy_sensitive_groups,
                       unhealthy,
                       very_unhealthy]

    def calculate_level(self, measurement):
        is_in = lambda x: measurement in x[1]
        if measurement <= 300:
            result = map(is_in, self.levels)
            level = self.levels[result is True][0]
        else:
            level = 'hazardous'
        return level

    @staticmethod
    def calculate_mean(data_list):
        s = reduce(lambda x, y: x + y[OpenAqDataFields.VALUE.value],
                   data_list, 0.0)
        return s / len(data_list)
