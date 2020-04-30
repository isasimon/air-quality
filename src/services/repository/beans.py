from enum import Enum
from .openaq.api import AirQualityApi


class RepositoryBeans(Enum):
    API = AirQualityApi()