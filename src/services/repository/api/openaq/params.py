from enum import Enum


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
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'


class OpenAqDateFormat(Enum):
    DATE_TO = '%Y-%m-%d'
    DATE_FROM = '%Y-%m-%d'


class Skeletons(Enum):
    GEOJSONPARENT = {
        'type': 'FeatureCollection',
        'features': []
    }
    GEOJSONPOINT = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
        },
        'properties': {

        }
    }


class GeoJsonKeys(Enum):
    FEATURES = 'features'
    PROPERTIES = 'properties'
    GEOMETRY = 'geometry'
