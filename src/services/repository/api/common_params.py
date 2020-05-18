from enum import Enum


class RequestParams(Enum):
    COUNTRY = 'country'
    CITY = 'city'
    FROM = 'date_from'
    TO = 'date_to'
    MONTH = 'month'
    YEAR = 'year'


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
