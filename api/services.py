from django.core.cache import cache

from api.tasks import get_currency_rates_dict_task


def convert(from_currency, to_currency):
    data = cache.get('currency_data')
    if not data:
        data = get_currency_rates_dict_task()
    return data[from_currency][to_currency]['value']
