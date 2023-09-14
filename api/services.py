from django.core.cache import cache
from api.tasks import get_currency_rates_dict_task



# def convert(from_currency, to_currency):
#     pass

def convert(from_currency, to_currency):
    data = cache.get('currency_data')
    if data is None:
        data = get_currency_rates_dict_task()
        cache.set('currency_data', data, 60 * 60)
    return data[from_currency][to_currency]

