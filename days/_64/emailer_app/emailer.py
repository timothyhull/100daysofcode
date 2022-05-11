#!/usr/bin/env python3
""" Application to send a simple email. """

# Imports - Python Standard Library
from collections import namedtuple
from os import getenv
import smtplib

# Imports - Third-Party
from dotenv import load_dotenv

# Imports - Local

# Load environment variables
load_dotenv()

# namedtuple objects
EmailObject = namedtuple(
    typename='EmailObject',
    field_names=[
        'from_addr',
        'to_addr',
        'body',
        'password'
    ]
)

# Constants
EMAIL_OBJECT = EmailObject(
    from_addr=getenv('FROM_ADDR'),
    to_addr=getenv('TO_ADDR'),
    body=getenv('BODY'),
    password=getenv('APP_PW')
)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def send_email() -> None:
    """ Send a simple email.

        Args:
            None.

        Returns:
            None.
    """

    # Create an smtplib.SMTP object
    print('\nSetting up server connection...', end='')
    with smtplib.SMTP(
        host=SMTP_SERVER,
        port=SMTP_PORT
    ) as smtp_object:
        print('done.')

        # Send an Enhanced Hello message to the SMTP server
        print('\nSending EHLO...', end='')
        ehlo = smtp_object.ehlo()
        if ehlo[0] == 250:
            print('done.')
        else:
            raise RuntimeError('\n** EHLO message failure **\n')

        # Start TLS session
        print('\nStarting TLS...', end='')
        starttls = smtp_object.starttls()
        if starttls[0] == 220:
            print('done.')
        else:
            raise RuntimeError('\n** TLS setup failure **\n')

        # Perform SMTP login
        print('\nLogging on...', end='')
        login = smtp_object.login(
            user=EMAIL_OBJECT.from_addr,
            password=EMAIL_OBJECT.password
        )
        if login[0] == 235:
            print('done.')
        else:
            raise RuntimeError('\n** Login failure **\n')

        # Send an email
        print('\nSending email...', end='')
        sendmail = smtp_object.sendmail(
            from_addr=EMAIL_OBJECT.from_addr,
            to_addrs=EMAIL_OBJECT.to_addr,
            msg=EMAIL_OBJECT.body
        )
        if sendmail == {}:
            print('done.\n')
        else:
            raise RuntimeError('\n** Message send failure **\n')


def main():
    """ Main application.

        Args:
            None.

        Returns:
            None.
    """

    # Call the send_email function
    send_email()


if __name__ == '__main__':
    main()
