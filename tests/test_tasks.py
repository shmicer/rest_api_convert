from unittest.mock import patch

import pytest
from django.core.cache import cache

from api.tasks import get_currency_rates_dict_task


@pytest.mark.django_db
@patch('requests.get')
def test_get_currency_rates_dict_task(mock_get):
    # Мокируем запрос с помощью requests.get
    mock_response = {
        'data': {
            'USD': 1.0,
            'EUR': 0.9,
            'RUB': 75.0,
        }
    }
    mock_get.return_value.json.return_value = mock_response

    # Вызываем Celery задачу
    result = get_currency_rates_dict_task.apply()

    # Проверяем, что задача выполнена успешно
    assert result.successful()

    # Проверяем, что данные сохранены в кеше
    cached_data = cache.get('currency_data')
    assert cached_data is not None
    assert isinstance(cached_data, dict)

    # Проверяем, что данные в кеше соответствуют ожиданиям
    assert 'USD' in cached_data
    assert 'EUR' in cached_data
    assert 'RUB' in cached_data
