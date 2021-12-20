#!/usr/bin/env pytest
""" pytest tests for send_email.py """

# Imports - Python Standard Library
from collections import namedtuple
from unittest.mock import MagicMock, patch

# Imports - Third-Party

# Imports - Local
from _52_53_54.app.send_email import (
    collect_email_info, create_email_body
)

# namedtuples
EmailInfo = namedtuple(
    typename='EmailInfo',
    field_names=[
        'address',
        'subject',
        'password'
    ]
)

# Constants
EMAIL_INFO = EmailInfo(
    address='test@gmail.com',
    subject='Test Message',
    password='password'
)

EMAIL_BODY = '''
VA strengthens care for Veterans impacted by intimate partner violence and sexual assault
=========================================================================================
 - Timestamp: Tue, 14 Dec 2021 16:00:00 EST
 - Link: https://www.va.gov/opa/pressrel/PressArtInternet.cfm?id=5747
'''

EMAIL_SUBJECT = (
    'Subject: News Releases from the U.S. Department of '
    'Veterans Affairs.'
)


# TODO - test mock value input
@patch(
    'builtins.input',
    side_effect=[
        EMAIL_INFO.address,
        EMAIL_INFO.subject,
    ]
)
@patch(
    'getpass.getpass',
    return_value=EMAIL_INFO.password
)
def test_collect_email_info(
    input: MagicMock,
    getpass: MagicMock
) -> None:
    """ Test the collect_email_info function for the correct values.

        Args:
            input (MagicMock):
                Mocked data for input function prompts.

            getpass (MagicMock):
                Mocked data for getpass.getpass prompts.

        Returns:
            None.
    """

    # Collect email info without loading values from a .env file
    email_info = collect_email_info(
        load_env_vars=False
    )

    assert email_info.address == EMAIL_INFO.address
    assert email_info.subject == EMAIL_INFO.subject
    assert email_info.password == EMAIL_INFO.password

    return None


def test_create_email_body() -> None:
    """ Test the create_email_body function.

        Args:
            None.

        Returns:
            None.
    """

    # Call the function
    formatted_email_body = create_email_body(
        email_info=EMAIL_INFO,
        body=EMAIL_BODY
    )

    # Assert the email headers and body match expected outputs.
    assert formatted_email_body.mail_info == EMAIL_SUBJECT
    assert formatted_email_body.subject == EMAIL_SUBJECT

    return None
