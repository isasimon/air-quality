from enum import Enum
from services.repository.api.openaq.adapter import AirQualityApi


class RepositoryBeans(Enum):
    API = AirQualityApi()