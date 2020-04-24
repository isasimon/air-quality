from usecases.get_city_air_quality import GetCityAirQuality
from class_configuration import ClassConfiguration
import json


def main():
    config = ClassConfiguration()
    get_city_aq = GetCityAirQuality(config)
    metrics = get_city_aq.get_city_air_quality("2020-03-02", "Madrid")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__" :
    main()
