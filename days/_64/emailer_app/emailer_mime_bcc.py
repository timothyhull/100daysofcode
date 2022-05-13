#!/usr/bin/env python3
""" Application to send a MIME-based email with BCC addresses. """

# Imports - Python Standard Library
from collections import namedtuple
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
        'bcc_list',
        'subject',
        'body',
        'password'
    ]
)

# Constants
EMAIL_OBJECT = EmailObject(
    from_addr=getenv('FROM_ADDR'),
    to_addr=getenv('TO_ADDR'),
    bcc_list=getenv('BCC_LIST').split(),
    subject=getenv('SUBJECT'),
    body=getenv('BODY'),
    password=getenv('APP_PW')
)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EHLO_SUCCESS = 250
TLS_SUCCESS = 220
LOGIN_SUCCESS = 235
SENDMAIL_SUCCESS = {}


def create_mime_message() -> MIMEMultipart:
    """ Send a MIME-based email.

        Args:
            None.

        Returns:
            mime_messsage (MIMEMultipart):
                MIME message parts as type
                email.mime.multipart.MIMEMultipart.
    """

    # Create a MIME multi-part message object
    mime_messsage = MIMEMultipart()

    # Build a MIME header part
    mime_messsage['From'] = EMAIL_OBJECT.from_addr
    mime_messsage['To'] = EMAIL_OBJECT.to_addr
    mime_messsage['Subject'] = EMAIL_OBJECT.subject

    # Build a MIME body part
    mime_messsage.attach(
        payload=MIMEText(
            _text=EMAIL_OBJECT.body,
            _subtype='plain'
        )
    )

    return mime_messsage


def send_email(
    mime_message: MIMEMultipart
) -> None:
    """ Send a simple email with a BCC list.

        Args:
            mime_messsage (MIMEMultipart):
                MIME message parts as type
                email.mime.multipart.MIMEMultipart.

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

        # Attempt to send an Enhanced Hello message to the SMTP server
        print('\nSending EHLO...', end='')
        ehlo = smtp_object.ehlo()
        if ehlo[0] == EHLO_SUCCESS:
            print('done.')
        else:
            raise RuntimeError('\n** EHLO message failure **\n')

        # Attempt to start a TLS session
        print('\nStarting TLS...', end='')
        starttls = smtp_object.starttls()
        if starttls[0] == TLS_SUCCESS:
            print('done.')
        else:
            raise RuntimeError('\n** TLS setup failure **\n')

        # Attempt to perform an SMTP login
        print('\nLogging on...', end='')
        login = smtp_object.login(
            user=EMAIL_OBJECT.from_addr,
            password=EMAIL_OBJECT.password
        )
        if login[0] == LOGIN_SUCCESS:
            print('done.')
        else:
            raise RuntimeError('\n** Login failure **\n')

        # Attempt to send an email
        print('\nSending email...', end='')
        sendmail = smtp_object.sendmail(
            from_addr=EMAIL_OBJECT.from_addr,
            to_addrs=[EMAIL_OBJECT.to_addr] + EMAIL_OBJECT.bcc_list,
            msg=mime_message.as_string()
        )
        if sendmail == SENDMAIL_SUCCESS:
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

    # Call the create_mime_message function
    mime_message = create_mime_message()

    # Call the send_email function
    send_email(
        mime_message=mime_message
    )

    return None


if __name__ == '__main__':
    main()
