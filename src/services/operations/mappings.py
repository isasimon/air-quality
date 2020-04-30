class Mappings:
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

    def get_pollution_level(self, measurement):
        is_in = lambda x: measurement in x[1]
        if measurement <= 300:
            result = map(is_in, self.levels)
            level = self.levels[result is True][0]
        else:
            level = 'hazardous'
        return level
