from enum import Enum
from services.repository.openaq.api import AirQualityApi
from services.transformation.json_source import JsonSource


class ClassConfiguration(Enum):
    REPOSITORY = AirQualityApi()
    TRANSFORM = JsonSource()
