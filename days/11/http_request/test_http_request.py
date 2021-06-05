#!/usr/bin/env pytest

# Imports
from http_request import http_request
from pytest import raises
import requests

# Constants
JSON = '{}'
URL = 'http://test.io'


def test_http_request(requests_mock):
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
    assert r.json() == '{}'
    assert r.status_code == 200
    assert r.ok


def test_http_request_raise_for_status(requests_mock):
    """Test function which mocks an invalid status code to make sure
       the function under test raises an HTTP exception.
    """
    requests_mock.get(
        url=URL,
        status_code=400
    )

    with raises(requests.exceptions.HTTPError):
        http_request(url=URL)


def test_http_connect_timeout(requests_mock):
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


def test_http_too_many_redirects(requests_mock):
    # Test function which mocks a connection timeout exception.
    requests_mock.get(
        url=URL,
        exc=requests.exceptions.InvalidHeader
    )

    """Use the pytest.raises() function to determine if the function
       under test raises the TooManyRedirects exception.
    """
    with raises(requests.exceptions.InvalidHeader):
        http_request(url=URL)
