from usecases.get_city_air_quality import GetCityAirQuality
from usecases.get_country_air_quality import GetCountryAirQuality
from beans.repository import RepositoryBeans
import json


def main():
    repo = RepositoryBeans.API.value
    get_city_aq = GetCityAirQuality(repo)
    get_country_aq = GetCountryAirQuality(repo)
    metrics = get_city_aq.get_city_air_quality("2020-02-01", "2020-02-28", "Berlin")
    country_metrics = get_country_aq.get_country_air_quality("2020-02-01",
                                                             "2020-02-28", "DE")
    f = open("../data/openapiq-feb-berlin.geojson", "w")
    f.write(json.dumps(metrics, indent=2))
    f.close()
    g = open("../data/openapiq-germany.geojson", "w")
    g.write(json.dumps(country_metrics, indent=2))
    g.close()


if __name__ == "__main__" :
    main()
