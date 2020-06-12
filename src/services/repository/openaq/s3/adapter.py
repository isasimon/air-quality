from interfaces.air_quality_repository_interface \
    import AirQualityRepositoryInterface
from services.repository.openaq.operations.geojson_treatment \
    import GeaojsonTreatment
from ..params import S3Params, DataFields, DateFormat
import boto3
import json
from datetime import datetime, timedelta


class OpenaqS3(AirQualityRepositoryInterface):
    def __init__(self):
        aws_key_id = S3Params.aws_key_id.value
        aws_secret_id = S3Params.aws_secret_id.value
        self.s3c = boto3.client("s3", aws_access_key_id=aws_key_id,
                                aws_secret_access_key=aws_secret_id)
        self.s3r = boto3.resource('s3', aws_access_key_id=aws_key_id,
                                  aws_secret_access_key=aws_secret_id)
        self.geojson_service = GeaojsonTreatment()

    def fetch_by_city(self, date_from, date_to, city):
        datetime_from = datetime.strptime(date_from, DateFormat.DATE_FROM.value)
        datetime_to = datetime.strptime(date_to, DateFormat.DATE_TO.value)
        delta = datetime_to - datetime_from
        total_data = []
        for x in range(delta.days + 1):
            day = datetime_from + timedelta(x)
            sday = day.strftime(DateFormat.DATE_TO.value)
            day_data = self.fetch_data_single_date(sday, city)
            if day_data:
                total_data = total_data + day_data
            total_data
        return self.geojson_service.geojson(total_data)

    def fetch_by_country(self, date_from, date_to, city):
        pass

    def fetch_data_single_date(self, date, city):
        sep = S3Params.path_sep.value
        try:
            realtime_object = self.s3r.Object(S3Params.bucket_name.value,
                                              S3Params.realtime_objects_folder.value
                                              + sep + date + sep + date
                                              + S3Params.data_format.value)
            raw = realtime_object.get()[S3Params.realtime_data_body.value]._raw_stream.data
        except:
            return None
        else:
            sdata = raw.decode('utf8').split("\n")
            jdata = []
            for i in sdata:
                try:
                    j = json.loads(i)
                except:
                    pass
                else:
                    jdata.append(j)
            return self.belongs(city, jdata)

    @staticmethod
    def belongs(actual_city, data):
        return [i for i in data
                if i[DataFields.CITY.value] == actual_city]
