#!/usr/bin/env pytest
""" Tests for the twilio_api.py application.

    Requirements:
        requests-mock

    Usage:
        pytest test_twilio_api.py
"""

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from _42.pybite_16.twilio_api import TwilioAPI


def test_api_auth() -> None:
    """ Test the _api_auth method.

        Determine if authentication to the Twilio API is successful.

        Args:
            None.

        Returns:
            None.
    """

    twilio = TwilioAPI(
        user_sid='abc',
        secret_key='abc'
    )

    assert twilio.auth
