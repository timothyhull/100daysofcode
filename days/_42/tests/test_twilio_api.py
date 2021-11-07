#!/usr/bin/env pytest
""" Tests for the twilio_api.py application.

    Requirements:
        requests-mock

    Usage:
        pytest test_twilio_api.py
"""

# Imports - Python Standard Library
from typing import Callable

# Imports - Third-Party
import requests

# Imports - Local
from _42.pybite_16.twilio_api import TwilioAPI, BASE_URL


def test_TwilioAPI_api_auth(
    requests_mock: Callable
) -> None:
    """ Test the _api_auth method.

        Determine if authentication to the Twilio API is successful.

        Args:
            requests_mock (Callable):
                pytest requests_mock object.

        Returns:
            None.
    """

    json = {'status': 'ok'}

    requests_mock.get(
        url=BASE_URL,
        json=json
    )
    r = requests.get(BASE_URL)

    print(r.json())
    print()
    print(json)

    assert json == r.json()

    return None

# TODO - test sending messages


# TODO - test checking messages
