#!/usr/bin/env python3
""" Email Parsed RSS Data """

# Imports - Python Standard Library
from collections import namedtuple
from os import getenv
# from smtplib import SMTP
import getpass

# Imports - Third-Party
from dotenv import load_dotenv

# Imports - Local

# namedtuples
EmailInfo = namedtuple(
    typename='EmailInfo',
    field_names=[
        'address',
        'password'
    ]
)

EmailBody = namedtuple(
    typename='EmailBody',
    field_names=[
        'email_info',
        'email_subject',
        'email_body'
    ]
)

# Constants


def collect_email_info(
    load_env_vars: bool = True
) -> EmailInfo:
    """ Collect information required to send email.

        Args:
            load_env_vars (bool, optional):
                Determines whether or not to run the load_dotenv
                function.  Default is True.

        Returns:
            email_info (EmailInfo):
                namedtuple object with required email information.
    """

    # Load environment files from a .env file
    if load_env_vars is True:
        load_dotenv()

    # Check for environment variables and request user input, if necessary
    if getenv('ADDRESS') is not None:
        address = getenv('ADDRESS')
    else:
        while True is True:
            print()
            address = input('Enter the destination email address: ')
            if address == '':
                print('\n** Email address is blank, please try again **')
            else:
                break

    if getenv('PASSWORD') is not None:
        password = getenv('PASSWORD')
    else:
        while True is True:
            print()
            password = getpass.getpass(
                f'Enter the email password for {address}: '
            )
            if password == '':
                print('\n** Password is blank, please try again **')
            else:
                break

    email_info = EmailInfo(
        address=address,
        password=password
    )

    print('\nEmail information collected.\n')

    return email_info


def create_email(
    email_info: EmailInfo,
    parsed_body: EmailBody
) -> EmailBody:
    """ Build a namedtuple object with attributes for email
        headers and a message body.

        Args:
            email_info (EmailInfo):
                namedtuple with email address and password.

            parsed_body (EmailBody):
                namedtuple with email subject and parsed RSS data.

        Returns:
            email_body (EmailBody):
                namedtuple with attributes for the email headers
                and body.
    """

    # Create a namedtuple with all required information, in the correct format.
    email_body = EmailBody(
        email_info=email_info,
        email_subject=f'Subject: {parsed_body.email_subject}\n\n',
        email_body=parsed_body.email_body
    )

    return email_body


# TODO - Send email


def main() -> None:
    """ Main program.

        Run the required functions in the correct order.

        Args:
            None.

        Returns:
            None.
    """

    return None


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram interrupted by CTRL-C escape sequence.\n')
