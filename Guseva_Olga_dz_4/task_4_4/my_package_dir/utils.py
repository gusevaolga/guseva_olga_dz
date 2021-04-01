import requests
import json

def currency_rates (code):
    upper_code = code.upper()
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    result_dict = json.loads(response.content)
    valute = result_dict['Valute'].get(upper_code)
    if valute:
        value = valute['Value']
        return value
    return None