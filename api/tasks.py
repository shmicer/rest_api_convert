import os
import time

import requests
from celery import shared_task
from django.core.cache import cache


API_KEY = os.environ.get('CURRENCY_API_KEY')


@shared_task()
def get_currency_rates_dict_task():
    currencies_dict = {}
    currencies = ['AED', 'USD', 'EUR', 'RUB', 'TRY', 'CNY', 'HKD']
    for base in currencies:
        url = f'https://api.currencyapi.com/v3/latest?apikey={API_KEY}&base_currency={base}'
        response = requests.get(url).json()
        currencies_dict[base] = response['data']
        time.sleep(0.5)
    data = cache.set('currency_data', currencies_dict)
    return data
