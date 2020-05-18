from beans.repository import RepositoryBeans
from usecases.get_city_month_air_quality import GetCityMonthAirQuality


def main():
    month = 3
    year = 2020
    city = 'Madrid'
    repo = RepositoryBeans.API.value
    get_city_month_aq = GetCityMonthAirQuality(repo)
    metrics = get_city_month_aq.get_city_month_air_quality(month, year, city)
    print(metrics)


if __name__ == '__main__':
    main()


"""def s3_read():
    bucket = S3("openaq-fetches")
    files = bucket.get_object_list('realtime/2013-11-26/')
    [print(i.key) for i in files]"""