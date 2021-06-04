#!/usr/bin/env pytest

# Imports
from http_request import http_request
from pytest import raises
from requests.exceptions import RequestException

# Constants
JSON = '{}'
URL = 'http://test.io'
BAD_URL = 'http://172.16.20.5:8099'


def test_http_request(requests_mock):
    """Test function which mocks an HTTP requests using the
       requests module.
    """

    """Create a mock get request, supply the necessary arguments,
       based on whatever the function under test requires.
    """
    requests_mock.get(
        url=URL,
        json=JSON
    )

    """With the request mocked, call the function under test.
       The function under test will use the mocked (not the actual) request.
    """
    r = http_request(url=URL)
    assert r.json() == '{}'


def test_bad_http_request(requests_mock):
    # Test function which mocks an HTTP requests exception.
    requests_mock.get(
        url=BAD_URL
    )

    # Use the pytest.raises() function to catch a specific exception.
    with http_request(url=BAD_URL):
        raises(RequestException)
