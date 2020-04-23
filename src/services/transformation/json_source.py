from interfaces.air_quality_transform_interface import AirQualityTransformationInterface
import json


class JsonSource(AirQualityTransformationInterface):
    def parse_source(self, source):
        return json.dumps(source, indent=2)

    def format_data(self, data):
        pass

    def insert_field(self, obj, field):
        pass

