import json
import requests
from pprint import pprint
currency = {'USD': ('$', 83.59), 'EUR': ('€', 92.39), 'PLN': ("zł", 19.86), 'UAH': ('₴', 2.84)}
curr_info = requests.get(r'https://www.cbr-xml-daily.ru/daily_json.js')
if curr_info.status_code == 200:
    curr_js = curr_info.json()
    source_data, valutes = curr_js['Date'].split('T')[0], dict(curr_js['Valute'])
    print(source_data)
    used = ['Name', 'Nominal', 'Value']
    pprint(dict(valutes))
    for val in currency:
        currency[val] = {i: valutes[val][i] for i in used}

    pprint(currency)
