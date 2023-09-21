import os

import requests
from django.core.cache import cache

from api.tasks import get_currency_rates_task

API_KEY = os.environ.get('CURRENCY_API_KEY')


def convert(from_currency, to_currency):
    if 'currency_data' in cache:
        data = cache.get('currency_data')
    else:
        data = get_currency_rates_task()
    return data[from_currency][to_currency]['value']


def get_currency_rate(currency):
    url = f'https://api.currencyapi.com/v3/latest?apikey={API_KEY}&base_currency={currency}'
    response = requests.get(url).json()
    result = response['data']
    return cache.set('currency_data', result)
