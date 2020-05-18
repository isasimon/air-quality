from enum import Enum


class OpenAqDataFields(Enum):
    RESULTS = 'results'
    PARAMETER = 'parameter'
    DATE = 'date'
    UTC = 'utc'
    CITY = 'city'
    VALUE = 'value'
    COORDINATES = 'coordinates'
    COUNTRY = 'country'
    LEVEL = 'level'
    MEAN = 'mean'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'


class OpenAqDateFormat(Enum):
    DATE_TO = '%Y-%m-%d'
    DATE_FROM = '%Y-%m-%d'
    RESPONSE = '%Y-%m-%dT%H:%M:%S.%fZ'
    FINAL_RESULT = '%Y-%m-%d'



