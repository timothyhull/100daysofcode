#!/usr/bin/env python3
""" Twilio SMS API Class.

    Requirements:
        requests

    Usage:
        from twilio_api import TwilioAPI
"""

# Imports - Python Standard Library
from collections import namedtuple
from typing import Dict, Tuple

# Imports - Third-Party
import requests

# Imports - Local

# Constants
BASE_URL = 'https://api.twilio.com'
BASE_PATH = '/2010-04-01/Accounts'
HTTP_ENCODING = 'json'
HTTP_TIMEOUT = 5
FROM_NUMBER = '+15034863861'
TO_NUMBER = '+15037248461'

# namedtuple for simplified HTTP method selection
HTTPMethod = namedtuple(
    typename='HTTPMethod',
    field_names=['get', 'post', 'put', 'delete']
)
HTTP_METHOD = HTTPMethod(
    get='GET',
    post='POST',
    put='PUT',
    delete='DELETE'
)

# Currency symbol lookup dictionary
CURRENCY = {
    'USD': '$'
}


class TwilioAPI:
    """ TwilioAPI class. """

    def __init__(
        self,
        account_sid: str,
        auth_token: str,
        api_sid: str,
        api_secret: str,
        **kwargs
    ) -> None:
        """ Twilio API __init__ method.

            Args:
                None.

            Returns:
                None.
        """

        # Perform API authentication test
        self._api_auth(
            account_sid=account_sid,
            auth_token=auth_token
        )

        # Display authentication message
        auth_msg = '** Authentication Successful **'
        print(f'\n{auth_msg}')
        print(f'{"-" * len(auth_msg)}')

        # Display account details
        accounts = self.api_auth.json()["accounts"][0]
        print(
            'Account name: '
            f'{accounts["friendly_name"]}'
        )

        print(
            'Account status: '
            f'{accounts["status"].title()}'
        )

        # Get account balance
        self._get_balance(
            account_sid=account_sid,
            api_sid=api_sid,
            api_secret=api_secret
        )

        # Display account balance
        balance = self.balance.json()
        print(
            'Account balance: '
            f'{CURRENCY.get(balance["currency"])}{balance["balance"]}\n'
        )

        return None

    def _api_helper(
        self,
        method: str,
        url: str,
        auth: Tuple,
        **kwargs
    ) -> requests.Response:
        """ Pass """

        # Send HTTP request
        response = requests.request(
            method=method,
            url=url,
            auth=auth,
            timeout=HTTP_TIMEOUT,
            **kwargs
        )

        response.raise_for_status()

        return response

    def _api_auth(
        self,
        account_sid: str,
        auth_token: str,
        **kwargs
    ) -> None:
        """ Pass """

        # HTTP request setup
        method = HTTP_METHOD.get
        url = f'{BASE_URL}{BASE_PATH}.{HTTP_ENCODING}'
        auth = (account_sid, auth_token)

        # HTTP request
        response = self._api_helper(
            method=method,
            url=url,
            auth=auth,
            **kwargs
        )

        self.api_auth = response
        self.api_uris = self.api_auth.json()['accounts'][0]['subresource_uris']

        return None

    def _get_balance(
        self,
        account_sid: str,
        api_sid: str,
        api_secret: str,
        **kwargs
    ) -> None:
        """ Pass. """

        # HTTP request setup
        endpoint = self.api_uris['balance']
        method = HTTP_METHOD.get
        url = f'{BASE_URL}{endpoint}'
        auth = (api_sid, api_secret)

        # HTTP request
        response = self._api_helper(
            method=method,
            url=url,
            auth=auth,
            **kwargs
        )

        self.balance = response

        return None

    def send_msg(
        self,
        account_sid: str,
        api_sid: str,
        api_secret: str,
        message_body: str,
        from_number: str = FROM_NUMBER,
        to_number: str = TO_NUMBER
    ) -> Dict:
        """ Pass. """

        # URL setup
        endpoint = f'/{account_sid}/Messages.json'
        url = f'{BASE_URL}{endpoint}'

        # HTTP Basic Authentication tuple
        auth = (api_sid, api_secret)

        # HTTP POST body
        payload = {
            'Body': message_body,
            'From': from_number,
            'To': to_number
        }

        # Send request
        self.response = requests.post(
            url=url,
            auth=auth,
            data=payload,
            timeout=HTTP_TIMEOUT
        )

        self.response.raise_for_status()

        return self.response
