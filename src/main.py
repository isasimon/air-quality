from usecases.get_city_air_quality import GetCityAirQuality
from class_configuration import ClassConfiguration


def main():
    get_city_aq = GetCityAirQuality(ClassConfiguration)
    metrics = get_city_aq.get_city_air_quality("2020-03-02", "Madrid")
    print(metrics)


if __name__== "__main__" :
    main()
