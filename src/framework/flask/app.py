from flask import Flask
from flask_cors import CORS
from flask import request
import json

from usecases.get_city_month_air_quality import GetCityMonthAirQuality
from beans.repository import RepositoryBeans
from services.repository.api.common_params import RequestParams

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def welcome():
    return '{ ping: pong }'


@app.route('/city-by-month', methods=['GET', 'POST'])
def city():
    month = request.args.get(RequestParams.MONTH.value, 1)
    year = request.args.get(RequestParams.YEAR.value, 1900)
    city = request.args.get(RequestParams.CITY.value, '')
    repo = RepositoryBeans.API.value
    get_month_city_aq = GetCityMonthAirQuality(repo)
    metrics = get_month_city_aq.get_city_month_air_quality(month,
                                                           year, city)
    return json.dumps(metrics, indent=2)
