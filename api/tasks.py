import os

from celery import shared_task
import time
import requests

currencies = ['USD', 'EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'HRK',
              'RUB', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD']

API_KEY = os.environ.get('API_KEY')

@shared_task()
def get_currency_rates_dict_task():
    currencies_dict = {}
    for base in currencies:
        url = f'https://exchange-rates.abstractapi.com/v1/live/?api_key={API_KEY}&base={base}'
        response = requests.get(url).json()
        time.sleep(1)
        currencies_dict[base] = response['exchange_rates']
    return currencies_dict


