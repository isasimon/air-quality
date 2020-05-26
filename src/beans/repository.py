from enum import Enum
from services.repository.openaq.api.adapter import OpenAqApi
from services.repository.openaq.s3.adapter import OpenaqS3


class RepositoryBeans(Enum):
    API = OpenAqApi()
    S3 = OpenaqS3()
