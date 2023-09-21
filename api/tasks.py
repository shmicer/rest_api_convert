from celery import shared_task
from services import get_currency_rate


@shared_task()
def get_currency_rates_task():
    currencies = ['AED', 'USD', 'EUR', 'RUB', 'TRY', 'CNY', 'HKD']
    for base in currencies:
        get_currency_rate(base)
