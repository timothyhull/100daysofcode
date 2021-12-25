#!/usr/bin/env pytest
""" pytest tests for send_email.py """

# Imports - Python Standard Library
from unittest.mock import MagicMock, patch

# Imports - Third-Party

# Imports - Local
from _52_53_54.app.send_email import (
    EmailInfo, EmailBody, collect_email_info, create_email, send_email
)

# Constants
EMAIL_INFO = EmailInfo(
    address='test@gmail.com',
    password='password'
)

EMAIL_SUBJECT = (
    'News Releases from the U.S. Department of '
    'Veterans Affairs.'
)

EMAIL_BODY = '''
VA strengthens care for Veterans impacted by intimate partner violence and sexual assault
=========================================================================================
 - Timestamp: Tue, 14 Dec 2021 16:00:00 EST
 - Link: https://www.va.gov/opa/pressrel/PressArtInternet.cfm?id=5747
'''

EMAIL_DATA = EmailBody(
    email_info=EMAIL_INFO,
    email_subject=EMAIL_SUBJECT,
    email_body=EMAIL_BODY
)


@patch(
    target='builtins.input',
    side_effect=[
        EMAIL_INFO.address
    ]
)
@patch(
    target='getpass.getpass',
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
    formatted_email_body = create_email(
        email_info=EMAIL_INFO,
        parsed_body=EMAIL_DATA
    )

    # Assert the email headers and body match expected outputs.
    assert formatted_email_body.email_info == EMAIL_INFO
    assert formatted_email_body.email_body == EMAIL_BODY

    return None


@patch(
    target='smtplib.SMTP.sendmail',
    return_value={}
)
@patch(
    target='smtplib.SMTP.login',
    side_effect=[
        EMAIL_INFO.address,
        EMAIL_INFO.password
    ]
)
@patch(
    target='smtplib.SMTP.starttls'
)
@patch(
    target='smtplib.SMTP.ehlo'
)
@patch(
    target='smtplib.SMTP'
)
def test_send_email(
    SMTP: MagicMock,
    ehlo: MagicMock,
    starttls: MagicMock,
    login: MagicMock,
    sendmail: MagicMock
) -> None:
    """ Test the send_email function.

        Args:
            sendmail (MagicMock):
                Mocked data for sendmail result. An empty
                dictionary ({}) indicates a successful message send.

        Returns:
            None.
    """

    # print(f'SMTP: {SMTP}\n')
    # print(f'ehlo: {ehlo}\n')
    # print(f'starttls: {starttls}\n')
    # print(f'login: {login}\n')
    # print(f'sendmail: {sendmail}\n')

    email_status = send_email(
        email_body=EMAIL_DATA
    )

    assert email_status == {}

    return None
