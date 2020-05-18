from flask import Flask
from flask import request
import json

from usecases.get_city_air_quality import GetCityAirQuality
from beans.repository import RepositoryBeans
from services.repository.api.common_params import RequestParams

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return '{\'ping\':\'pong\'}'


@app.route('/city', methods=['POST'])
def city():
    date_from = request.args.get(RequestParams.FROM.value, '')
    date_to = request.args.get(RequestParams.TO.value, '')
    city = request.args.get(RequestParams.CITY.value, '')
    repo = RepositoryBeans.API.value
    get_city_aq = GetCityAirQuality(repo)
    metrics = get_city_aq.get_city_air_quality(date_from,
                                               date_to, city)
    return json.dumps(metrics, indent=2)


if __name__ == '__main__':
    app.run()