import json
import requests
from pprint import pprint

def get_currency_info(currency: list) -> tuple:
    curr_info = requests.get(r'https://www.cbr-xml-daily.ru/daily_json.js')
    if curr_info.status_code == 200:
        try:
            curr_js = curr_info.json()
            curr_data = dict.fromkeys(currency, {})
            source_date, valutes = curr_js['Date'].split('T')[0], dict(curr_js['Valute'])
            used = ['Name', 'Nominal', 'Value']
            for val in currency:
                curr_data[val] = {i: valutes[val][i] for i in used}
            return source_date, curr_data
        except Exception as e:
            print(e)

    return 'Error with data'



