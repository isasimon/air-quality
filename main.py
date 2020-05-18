from beans.repository import RepositoryBeans
from usecases.get_city_air_quality import GetCityAirQuality


def main():
    date_from = '2020-03-03'
    date_to = '2020-03-04'
    city = 'Madrid'
    repo = RepositoryBeans.API.value
    get_city_aq = GetCityAirQuality(repo)
    metrics = get_city_aq.get_city_air_quality(date_from,
                                               date_to, city)
    print(metrics)


if __name__ == '__main__':
    main()



"""def s3_read():
    bucket = S3("openaq-fetches")
    files = bucket.get_object_list('realtime/2013-11-26/')
    [print(i.key) for i in files]"""