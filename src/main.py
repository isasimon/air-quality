from usecases.get_city_air_quality import GetCityAirQuality
from services.repository.beans import RepositoryBeans
import json


def main():
    repo = RepositoryBeans.API.value
    get_city_aq = GetCityAirQuality(repo)
    metrics = get_city_aq.get_city_air_quality("2020-03-01", "2020-03-30", "Madrid")
    f = open("../data/openapiq.geojson", "w")
    f.write(json.dumps(metrics, indent=2))
    f.close()


if __name__ == "__main__" :
    main()
