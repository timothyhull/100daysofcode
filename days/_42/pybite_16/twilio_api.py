#!/usr/bin/env python3
""" Twilio SMS API.

    Contains the TwilioAPI class which provides methods that
    authenticate and interact with the Twilio REST API.  Use the
    TwilioAPI class to send SMS messages.

    Twilio SMS API reference:
        https://www.twilio.com/docs/sms/api


    Requirements:
        Python packages via pip:
            python-dotenv
            requests

        Twilio account, trial or paid:
            https://www.twilio.com/login

        Twilio API key, obtained from the Twilio account console:
            https://console.twilio.com/

        Environment variables file named .env with the
        following contents:
            account_sid=<Twilio_Account_SID>
            auth_token=<Twilio_Account_Auth_Token>
            api_sid=<Twilio_API_Key_SID>
            api_secret=<Twilio_API_Key_Secret>
            from_number=<+e.164_sender_phone_number>
            to_number=<+e.164_receiver_phone_number>

    Usage:
        1. Import the TwiloAPI class:
            from twilio_api import TwilioAPI

        2. Import the dotenv module:
            import dotenv

        3. Load environment variables from your .env file:
            dotenv.load_dotenv(<path_to_.env_file>)

        4. Create an instance of the TwilioAPI class:
            twilio = TwilioAPI(**dotenv.dotenv_values())

        5. Call TwilioAPI methods, for example:
            twilio.send_msg(
                message_body='This is a test SMS message."
            )
"""

# Imports - Python Standard Library
from collections import namedtuple
from copy import deepcopy
from typing import Dict, Tuple

# Imports - Third-Party
import requests

# Constants
BASE_URL = 'https://api.twilio.com'
BASE_PATH = '/2010-04-01/Accounts'
HTTP_ENCODING = 'json'
HTTP_TIMEOUT = 5
SMS_PAYLOAD_BODY = {
    'Body': None,
    'From': None,
    'To': None
}

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
    """ TwilioAPI class object.

        See individual method docstrings for help.
    """

    def __init__(
        self,
        account_sid: str,
        auth_token: str,
        api_sid: str,
        api_secret: str,
        **kwargs
    ) -> None:
        """ Twilio API __init__ method.

            Automatically attempts Twilio authentication, displays
            account details, and displays available account balance.

            Args:
                account_sid (str):
                    Twilio account SID.

                auth_token (str)
                    Twilio account auth token.

                api_sid (str):
                    Twilio API key SID.

                api_secret (str):
                    Twilio API key secret.

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
        self._display_balance()

        return None

    def _api_helper(
        self,
        method: str,
        url: str,
        auth: Tuple,
        **kwargs
    ) -> requests.Response:
        """ Twilio API helper method.

            Performs HTTP REST API interactions with the Twilio
            SMS API.

            Args:
                method (str):
                    HTTP method referencable using the HTTP_METHOD
                    namedtuple object (HTTP_METHOD.get)

                url (str):
                    Fully-qualified URL to the required Twilio API
                    endpoint.

                auth (Tuple):
                    Tuple of the Twilio API key SID and the Twilio API
                    key secret, used for HTTP basic authentication.

                **kwargs:
                    Other required keyword arguments from the
                    requests module.

            Returns:
                response (requests.Response:)
                    Response object returned from the REST API call.
        """

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
        """ Twilio API authentication method.

            Called by the __init__ method to perform initial
            authentication with the Twilio API.  Stores the response
            from Twilio in self.api_auth.  Stores the callable API
            endpoint URIs in self.api_uris.

            Args:
                account_sid (str):
                    Twilio account SID.

                auth_token (str)
                    Twilio account auth token.

                **kwargs:
                    Placeholder for any unused keyword arguments.

            Returns:
                None.
        """

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
        api_sid: str,
        api_secret: str,
        **kwargs
    ) -> None:
        """ Twilio API get available balance method.

            Calls the Twilio API 'balance' endpoint to determine the
            available account balance.  Stores the response in
            self.response.

            Args:
                api_sid (str):
                    Twilio API key SID.

                api_secret (str):
                    Twilio API key secret.

                **kwargs:
                    Placeholder for any unused keyword arguments.

            Returns:
                None.
        """

        # HTTP request setup
        endpoint = self.api_uris['balance']
        method = HTTP_METHOD.get
        url = f'{BASE_URL}{endpoint}'
        auth = (api_sid, api_secret)

        # HTTP request
        response = self._api_helper(
            method=method,
            url=url,
            auth=auth
        )

        self.balance = response

        return None

    def _display_balance(
        self,
        **kwargs
    ) -> None:
        """ Display available Twilio account balance.

            Prints the formatted account balance to STDOUT.

            Args:
                None.

            Returns:
                None.
        """

        # Display account balance
        balance = self.balance.json()
        print(
            'Account balance: '
            f'{CURRENCY.get(balance["currency"])}{balance["balance"]}\n'
        )

    def send_msg(
        self,
        account_sid: str,
        api_sid: str,
        api_secret: str,
        message_body: str,
        from_number: str,
        to_number: str,
        **kwargs
    ) -> Dict:
        """ Method to send an SMS message via the Twilio API.

            Args:
                account_sid (str):
                    Twilio account SID.

                api_sid (str):
                    Twilio API key SID.

                api_secret (str):
                    Twilio API key secret.

                message_body (str):
                    SMS message body to send.

                from_number (str):
                    SMS sending phone number in +e164 format:
                        +11235551212

                from_number (str):
                    SMS sending phone number in +e164 format:
                        +11235551212

            Returns:
                None.
        """

        # HTTP request setup
        endpoint = self.api_uris['messages']
        method = HTTP_METHOD.post
        url = f'{BASE_URL}{endpoint}'
        auth = (api_sid, api_secret)

        # HTTP payload setup
        data = deepcopy(SMS_PAYLOAD_BODY)
        data['Body'] = message_body
        data['From'] = from_number
        data['To'] = to_number

        # HTTP request
        response = self._api_helper(
            method=method,
            url=url,
            auth=auth,
            data=data
        )

        response.raise_for_status()

        # Refresh account balance
        self._get_balance(
            account_sid=account_sid,
            api_sid=api_sid,
            api_secret=api_secret
        )

        # Display account balance
        print()
        self._display_balance()

        return response
