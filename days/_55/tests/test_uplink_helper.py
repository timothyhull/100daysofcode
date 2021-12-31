#!/usr/bin/env pytest
""" pytest tests for uplink_helper.py """

# Imports - Python Standard Library

# Imports - Third-party
from pytest import raises
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker

# Imports - Local
from _55.app.uplink_helper import (
    handle_http_error
)

# Constants


def test_handle_http_error(
    requests_mock: Mocker
) -> None:
    """ Test the handle_http_error function in uplink_helper.py.

        Args:
            requests_mock (MagicMock):
                Mocked HTTP client request.
    """

    # Setup mock HTTP request
    url = 'http://test.api.local'

    # Send the HTTP request with a 4XX response code
    mock_response = requests_mock.get(
        url=url,
        exc=HTTPError
    )

    with raises(
        expected_exception=HTTPError
    ):
        handle_http_error(mock_response)

    return None
