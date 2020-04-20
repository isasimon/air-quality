from usecases.get_city_air_quality import GetCityAirQuality
from services.repository.air_quality_bdd import AirQualityBdd


def main():
    repository = AirQualityBdd()
    get_city_aq = GetCityAirQuality(repository)
    metrics = get_city_aq.get_city_air_quality("2020-03-03", "Madrid")
    print(metrics)


if __name__== "__main__" :
    main()