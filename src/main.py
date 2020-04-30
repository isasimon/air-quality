from usecases.get_city_air_quality import GetCityAirQuality
from services.repository.beans import RepositoryBeans
import json


def main():
    repo = RepositoryBeans.API.value
    get_city_aq = GetCityAirQuality(repo)
    metrics = get_city_aq.get_city_air_quality("2020-03-01", "2020-03-30", "Madrid")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__" :
    main()
