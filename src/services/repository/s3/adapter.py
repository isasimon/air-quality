from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
import boto3


class S3(AirQualityRepositoryInterface):
    def __init__(self, bucket_name):
        aws_key_id = "AKIAXK5MI4A3DS7SBIFT"
        aws_secret_id = "D7EgiB6o5RDvV7rNWBdtcmhcPC1HBKoBrgWCz6KI"
        s3r = boto3.resource('s3', aws_access_key_id=aws_key_id,
                             aws_secret_access_key=aws_secret_id)
        self.bucket = s3r.Bucket(bucket_name)

    def fetch_by_city(self, date_from, date_to, city):
        pass

    def fetch_by_country(self, date_from, date_to, city):
        pass

    def generate_geojson(self, raw_data):
        pass

    def get_object_list(self, obj):
        return self.bucket.objects.filter(Prefix=obj)
