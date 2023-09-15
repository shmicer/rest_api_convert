import os

from celery import shared_task
import time
import requests

currencies = ['AED', 'USD', 'EUR', 'RUB', 'TRY', 'CNY', 'HKD']


API_KEY = os.environ.get('CURRENCY_API_KEY')

@shared_task
def get_currency_rates_dict_task():
    currencies_dict = {}
    for base in currencies:
        url = f'https://api.currencyapi.com/v3/latest?apikey={API_KEY}&base_currency={base}'
        response = requests.get(url).json()
        time.sleep(0.5)
        currencies_dict[base] = response['data']
    return currencies_dict


