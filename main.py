from beans.repository import RepositoryBeans
from usecases.get_city_air_quality import GetCityAirQuality
from framework.flask.app import get_date_boundaries, get_last_api_date

from services.repository.openaq.params import DateFormat
from datetime import datetime


def main():
    month = 12
    year = 2019
    city = 'Madrid'
    first_request_day, last_request_day = get_date_boundaries(year,
                                                              month)
    last_api_month, last_api_year = get_last_api_date(datetime
                                                      .now())
    last_api_day = get_date_boundaries(last_api_year, last_api_month)[1]

    if last_request_day <= last_api_day:
        repo = RepositoryBeans.S3.value
    else:
        repo = RepositoryBeans.API.value
    get_city_aq = GetCityAirQuality(repo)
    metrics = get_city_aq.get_city_air_quality(first_request_day.strftime(DateFormat.DATE_FROM.value),
                                               last_request_day.strftime(DateFormat.DATE_TO.value),
                                               city)

    print(metrics)


if __name__ == '__main__':
    main()


"""def s3_read():
    bucket = S3("api-fetches")
    files = bucket.get_object_list('realtime/2013-11-26/')
    [print(i.key) for i in files]"""