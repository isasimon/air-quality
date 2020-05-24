from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
from ..params import S3Params
import boto3
from os import sep


class OpenaqS3(AirQualityRepositoryInterface):
    def __init__(self, bucket_name):
        aws_key_id = "AKIAXK5MI4A3DS7SBIFT"
        aws_secret_id = "D7EgiB6o5RDvV7rNWBdtcmhcPC1HBKoBrgWCz6KI"
        s3r = boto3.resource('s3', aws_access_key_id=aws_key_id,
                             aws_secret_access_key=aws_secret_id)
        self.bucket = s3r.Bucket(bucket_name)

    def fetch_by_city(self, date_from, date_to, city):
        files = self.bucket.get_object_list(S3Params.realtime_objects_folder
                                            + sep + date_from + sep)
        [print(i.key) for i in files]
        return files

    def fetch_by_country(self, date_from, date_to, city):
        pass
