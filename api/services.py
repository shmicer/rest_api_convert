import requests
from django.views.decorators.cache import cache_page

@cache_page(60 * 2)
def convert(from_currency, to_currency):
    url = f'https://api.coingate.com/api/v2/rates/merchant/{from_currency}/{to_currency}'
    headers = {"accept": "text/plain"}
    response = requests.get(url, headers=headers)
    return response.text