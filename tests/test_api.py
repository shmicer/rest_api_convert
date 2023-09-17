import requests
import pytest
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
    convert_response = requests.get(ENDPOINT +
                                    f'?from_currency={data["from_currency"]}'
                                    f'&to_currency={data["to_currency"]}'
                                    f'&amount={data["amount"]}')

    assert convert_response.status_code == status.HTTP_200_OK

    assert convert_response.json()['detail'] == f'{data["from_currency"]} to {data["to_currency"]} is successfully converted.'
    assert round(convert_response.json()['result'], 2) == 90.0  # Сравниваем с ожидаемым результатом с учетом погрешности
#
# def test_missing_parameters(api_client, api_url):
#     # Отправляем запрос без обязательных параметров
#     data = {
#         'from_currency': 'USD',
#     }
#     response = api_client.post(api_url, data, format='json')
#
#     # Проверяем, что ответ имеет статус 400 Bad Request
#     assert response.status_code == status.HTTP_400_BAD_REQUEST
#
#     # Проверяем, что в ответе есть сообщение об отсутствии обязательных параметров
#     assert response.json()['detail'] == 'Missing required parameters.'
