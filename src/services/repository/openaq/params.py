from enum import Enum


class OpenAqRequestParams(Enum):
    CITY = 'city'
    FROM = 'date_from'
    TO = 'date_to'


class OpenAqDataFields(Enum):
    RESULTS = 'results'
    PARAMETER = 'parameter'
    DATE = 'date'
    CITY = 'city'
    VALUE = 'value'
    COORDINATES = 'coordinates'
    COUNTRY = 'country'
    LEVEL = 'level'
    MEAN = 'mean'


class OpenAqDateFormat(Enum):
    DATE_TO = '%Y-%m-%d'
    DATE_FROM = '%Y-%m-%d'
