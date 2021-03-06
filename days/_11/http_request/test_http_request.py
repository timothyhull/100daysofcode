#!/usr/bin/env pytest

# Imports
from requests import exceptions
from http_request import http_request
from json import loads
from pytest import raises
from unittest.mock import patch
import requests

# Constants
JSON = '{"Test": "Value"}'
URL = 'http://test.io'


def test_valid_http_request(requests_mock):
    """Test function which mocks an HTTP request using the
       requests module. 'requests_mock' automatically becomes a pytest
       fixture when installed by pip (pip install requests-mock). Use the
       'requests_mock' fixture by supplying 'requests_mock' as a parameter.
    """

    """Create a mock get request, supply the necessary arguments,
       based on whatever the function under test requires.
    """
    requests_mock.get(
        url=URL,
        json=JSON,
        status_code=200
    )

    """With the request mocked, call the function under test.
       The function under test will use the mocked (not the actual) request.
    """
    r = http_request(url=URL)
    assert r.ok
    assert r.status_code == 200
    assert r.json()
    assert loads(r.json()).get('Test') == 'Value'


def test_http_request_raise_for_status_exception(requests_mock):
    """Test function which mocks an invalid status code to make sure
       the function under test raises an HTTP exception.
    """
    requests_mock.get(
        url=URL,
        status_code=400
    )

    with raises(requests.exceptions.HTTPError):
        http_request(url=URL)


# def test_request_with_context_manager():
#     with requests_mock.Mocker() as m:
#         m.get(
#             url=URL,
#             exc=requests.exceptions.ConnectTimeout
#         )

#         with raises(requests.exceptions.ConnectTimeout) as e:
#             print(dir(e._excinfo))
#             http_request(url=URL)
#             # print(dir(e))


# def test_api():
#     with patch('http_request.http_request', side_effect=requests.exceptions.ConnectTimeout):
#         with raises(Exception) as excinfo:
#             # print(dir(excinfo))
#             r = http_request(url=URL)


# @patch('requests.get')
# def test_request_get_exception(self, requests_mock):
#     requests_mock.side_effect = requests.exceptions.ConnectionError
#     http_request(url=URL)


def test_http_connect_timeout_exception(requests_mock):
    # Test function which mocks a connection timeout exception.
    requests_mock.get(
        url=URL,
        exc=requests.exceptions.ConnectTimeout
    )

    """Use the pytest.raises() function to determine if the function
       under test raises the ConnectTimeout exception.
    """
    with raises(requests.exceptions.ConnectTimeout):
        http_request(url=URL)
