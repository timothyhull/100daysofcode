#!/usr/bin/env pytest
""" Tests for the twilio_api.py application.

    Requirements:

    Usage:
        pytest test_twilio_api.py
"""

# Imports - Python Standard Library
from typing import Dict

# Imports - Third-Party
from pytest import raises
from requests import HTTPError
import _pytest.capture
import requests_mock.mocker

# Imports - Local
from _42.pybite_16.twilio_api import (
    TwilioAPI, BASE_URL, BASE_PATH, HTTP_ENCODING, HTTP_METHOD
)


def create_twilio_instance() -> Dict:
    """ Create mock instance of the TwilioAPI class.

        Sends mock argument values to support mocked HTTP requests.

        Args:
            None.

        Returns:
            twilio (Dict):
                Mocked requests.Response object JSON data.
    """

    twilio = TwilioAPI(
        account_sid='account_sid',
        auth_token='auth_token',
        api_sid='api_sid',
        api_secret='api_secret'
    )

    return twilio


def test_TwilioAPI_init(
    capsys: _pytest.capture.CaptureFixture,
    requests_mock: requests_mock.mocker.Mocker
) -> None:
    """ Tests the TwilioAPI._init_ method using mock HTTP requests.

        Tests the authentication, balance check, and text output with
        mock HTTP response data.

        Args:
            capsys (_pytest.capture.CaptureFixture):
                pytest fixture to capture writes to sys.stdout and
                sys.stderr.

            requests_mock (requests_mock.mocker.Mocker):
                pytest fixture to mock requests class HTTP requests.

        Returns:
            None.
    """

    # Setup API authentication mock HTTP request
    method = HTTP_METHOD.get
    url = f'{BASE_URL}{BASE_PATH}.{HTTP_ENCODING}'

    # Setup API authentication mock HTTP response body
    json = {
        'accounts': [
            {
                'status': 'active',
                'friendly_name': 'Test Account',
                'subresource_uris': {
                    'balance': '/Balance.json'
                }
            }
        ]
    }

    # Create the API authentication mock request/response object
    requests_mock.request(
        method=method,
        url=url,
        json=json
    )

    # Setup API authentication mock HTTP request
    method = HTTP_METHOD.get
    balance_endpoint = json['accounts'][0]['subresource_uris']['balance']
    url = f'{BASE_URL}{balance_endpoint}'

    # Setup account balance mock HTTP response body
    json = {
        'currency': 'USD',
        'balance': '15.00'
    }

    # Create the account balance mock request/response object
    requests_mock.request(
        method=method,
        url=url,
        json=json
    )

    # Create an instance of the TwilioAPI class
    twilio = create_twilio_instance()

    # Set variables from API authentication mock response object
    status = twilio.api_auth.json()['accounts'][0]['status']
    account_name = twilio.api_auth.json()['accounts'][0]['friendly_name']
    resource_uris = twilio.api_auth.json()['accounts'][0]['subresource_uris']

    # Test mock response variable contents
    assert 'active' in status
    assert 'Test Account' in account_name
    assert 'Balance' in resource_uris['balance']

    # Test sys.stdout contents
    stdout_contents = capsys.readouterr().out

    assert '** Authentication Successful **' in stdout_contents


def test_TwilioAPI_init_exception(
    requests_mock: requests_mock.mocker.Mocker
) -> None:
    """ Tests the TwilioAPI._init_ method for mock HTTP exceptions.

        Args:
            requests_mock (requests_mock.mocker.Mocker):
                pytest fixture to mock requests class HTTP requests.

        Returns:
            None.
    """

    # Setup API authentication mock HTTP request
    method = HTTP_METHOD.get
    url = f'{BASE_URL}{BASE_PATH}.{HTTP_ENCODING}'

    requests_mock.request(
        method=method,
        url=url,
        status_code=401
    )

    with raises(HTTPError):
        create_twilio_instance()

    return None
