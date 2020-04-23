from enum import Enum
from services.repository.openaq.api import AirQualityApi


class ClassConfiguration(Enum):
    REPOSITORY = AirQualityApi()
