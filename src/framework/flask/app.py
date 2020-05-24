from flask import Flask
from flask_cors import CORS
from flask import request
import json

from usecases.get_city_air_quality import GetCityAirQuality
from beans.repository import RepositoryBeans
from services.repository.openaq.params import RequestParams
from services.repository.openaq.params import DateFormat
from datetime import datetime, timedelta
from calendar import monthrange

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def welcome():
    return '{ ping: pong }'


@app.route('/city-by-month', methods=['GET', 'POST'])
def city():
    month = int(request.args.get(RequestParams.MONTH.value, 1))
    year = int(request.args.get(RequestParams.YEAR.value, 1900))
    city = request.args.get(RequestParams.CITY.value, '')

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
    return json.dumps(metrics, indent=2)


def get_date_boundaries(year, month):
    first, last = monthrange(year, month)
    return (datetime(year, month, first),
            datetime(year, month, last))


def get_last_api_date(end_date):
    delta = timedelta(days=90)
    last_api_month = end_date - delta
    return (last_api_month.month,
            last_api_month.year)