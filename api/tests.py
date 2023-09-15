import requests
import pytest

ENDPOINT = 'https://0.0.0.0:8000/'


def test_connect_api():
    connect_response = connect()
    assert connect_response.status_code == 200



def connect():
    return requests.get(ENDPOINT)


def create_url(payload):
    return requests.post(ENDPOINT + 'url', json=payload)


def get_url(short_url):
    return requests.get(ENDPOINT + f'{short_url}')


def create_payload():
    url = 'https://www.honeybadger.io/blog/django-test-github-actions/1'
    return {
        'url': url,
    }


def get_payload():
    url = 'https://www.honeybadger.io/blog/django-test-github-actions/'
    return {
        'url': url,
        'short_url': '1a9e2d'
    }
