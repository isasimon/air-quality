from enum import Enum


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


class DataFields(Enum):
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


class DateFormat(Enum):
    DATE_TO = '%Y-%m-%d'
    DATE_FROM = '%Y-%m-%d'
    RESPONSE = '%Y-%m-%dT%H:%M:%S.%fZ'
    FINAL_RESULT = '%Y-%m-%d'


class S3Params(Enum):
    bucket_name = 'openaq-fetches'
    realtime_objects_folder = 'realtime'
    data_format = '.ndjson'
    realtime_data_body = 'Body'
    path_sep = '/'
    aws_key_id = 'AKIAXK5MI4A3DS7SBIFT'
    aws_secret_id = 'D7EgiB6o5RDvV7rNWBdtcmhcPC1HBKoBrgWCz6KI'



