from enum import Enum
from services.repository.openaq.api.adapter import OpenAqApi
from services.repository.openaq.s3.adapter import OpenaqS3
from services.repository.openaq.params import S3Params


class RepositoryBeans(Enum):
    API = OpenAqApi()
    S3 = OpenaqS3(S3Params.bucket_name)
