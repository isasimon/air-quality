from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
from ..params import S3Params
import boto3
from os import sep


class OpenaqS3(AirQualityRepositoryInterface):
    def __init__(self):
        aws_key_id = S3Params.aws_key_id.value
        aws_secret_id = S3Params.aws_secret_id.value
        s3r = boto3.resource('s3', aws_access_key_id=aws_key_id,
                                   aws_secret_access_key=aws_secret_id)
        self.bucket = s3r.Bucket(S3Params.bucket_name.value)

    def fetch_by_city(self, date_from, date_to, city):
        files = self.bucket.objects.all()

        [print(i) for i in files]
        return files

    def fetch_by_country(self, date_from, date_to, city):
        pass
