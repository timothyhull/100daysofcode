#!/usr/bin/env pytest
""" pytest tests for uplink_helper.py """

# Imports - Python Standard Library

# Imports - Third-party
from pytest import raises
from requests.exceptions import HTTPError
from requests.models import Response

# Imports - Local
from _55.app.uplink_helper import (
    handle_http_error
)


def test_handle_http_error() -> None:
    """ Test the handle_http_error function in uplink_helper.py.

        Args:
            None.

        Returns:
            None.
    """

    # Create a mock requests.models.Response object
    response = Response

    # Assign attribute values that will raise an HTTPError exception
    response.ok = False
    response.reason = 'Not Found'
    response.status_code = 404
    response.url = 'http://test.api.local'

    # Call pytest.raises for the requests.exceptions.HTTPError exception
    with raises(
        expected_exception=HTTPError
    ):
        # Call the handle_http_error function, and pass the response object
        test_response = handle_http_error(response)

        # Attempt to raise for status after calling handle_http_error
        response.raise_for_status(test_response)

    return None
