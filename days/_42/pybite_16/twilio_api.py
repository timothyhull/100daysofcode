#!/usr/bin/env python3
""" Twilio SMS API Class.

    Requirements:
        requests

    Usage:
        from twilio_api import TwilioAPI
"""

# Imports - Python Standard Library
from typing import Dict

# Imports - Third-Party
import requests

# Imports - Local

# Constants
BASE_URL = 'https://api.twilio.com/2010-04-01/Accounts'
HTTP_TIMEOUT = 5
FROM_NUMBER = '+15034863861'
TO_NUMBER = '+15037248461'


class TwilioAPI:
    """ TwilioAPI class. """

    def __init__(
        self
    ) -> None:
        """ Twilio API __init__ method.

            Args:
                None.

            Returns:
                None.
        """

        return None

    def send_msg(
        self,
        account_sid: str,
        user_sid: str,
        user_key: str,
        message_body: str,
        from_number: str = FROM_NUMBER,
        to_number: str = TO_NUMBER
    ) -> Dict:
        """ Pass. """

        # URL setup
        endpoint = f'/{account_sid}/Messages.json'
        url = f'{BASE_URL}{endpoint}'

        # HTTP Basic Authentication header
        auth = (
            user_sid,
            user_key
        )

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
