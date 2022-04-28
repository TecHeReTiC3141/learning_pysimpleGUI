from bs4 import BeautifulSoup
from pprint import pprint
import requests
import json

def get_weather_data(city: str):
    req = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': city, 'type': 'like', 'units': 'metric',
                         'APPID': '6979adb973aad6a1cba63e2f6291165d'})
    assert req.status_code == 200, f'Problem with request: {req.status_code}'
    pprint(json.loads(req.text))

get_weather_data('Chusovoy')