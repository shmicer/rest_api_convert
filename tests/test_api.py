import pytest
import requests
from rest_framework import status

ENDPOINT = 'https://test2py.ru/api/convert/'


@pytest.mark.parametrize('data', [
    {
        'from_currency': 'AED',
        'to_currency': 'EUR',
        'amount': 150.00,
    },
    {
        'from_currency': 'USD',
        'to_currency': 'EUR',
        'amount': 100.00,
    }, {
        'from_currency': 'USD',
        'to_currency': 'RUB',
        'amount': 200,
    }])
def test_currency_conversion(data):
    convert_response = requests.get(ENDPOINT + f'?from_currency={data["from_currency"]}'
                                               f'&to_currency={data["to_currency"]}'
                                               f'&amount={data["amount"]}')

    assert convert_response.status_code == status.HTTP_200_OK

    assert convert_response.json()['detail'] == (f'{data["from_currency"]}\n '
                                                 f'to {data["to_currency"]}\n'
                                                 f'is successfully converted.')


@pytest.mark.parametrize('data', [
    {
        'from_currency': 'AED',
        'to_currency': '',
        'amount': 150.00,
    },
    {
        'from_currency': '',
        'to_currency': 'EUR',
        'amount': 100.00,
    }, {
        'from_currency': 'USD',
        'to_currency': 'RUB',
        'amount': '',
    }])
def test_missing_parameters(data):
    convert_response = requests.get(ENDPOINT + f'?from_currency={data["from_currency"]}'
                                               f'&to_currency={data["to_currency"]}'
                                               f'&amount={data["amount"]}')

    assert convert_response.status_code == status.HTTP_400_BAD_REQUEST

    assert convert_response.json()['detail'] == 'Missing required parameters.'
