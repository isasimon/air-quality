from usecases.get_city_air_quality import GetCityAirQuality
from services.repository.openaq.api import AirQualityBdd
import json


def main():
    repository = AirQualityBdd()
    get_city_aq = GetCityAirQuality(repository)
    metrics = get_city_aq.get_city_air_quality("2020-03-02", "London")
    print(json.dumps(metrics, indent=2))


if __name__== "__main__" :
    main()