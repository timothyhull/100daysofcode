#!/usr/bin/env python3
""" Emailer app for day 66 of 100DaysOfCode. """

# Imports - Python Standard Library
from collections import namedtuple
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
import smtplib

# Imports - Third-Party
from dotenv import load_dotenv

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
        'body'
    ]
)

# Constants
EMAIL_OBJECT = EmailObject(
    from_addr=getenv('FROM_ADDR'),
    to_addr=getenv('TO_ADDR'),
    bcc_list=getenv('BCC_LIST').split(),
    subject=getenv('SUBJECT'),
    body=getenv('BODY')
)
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587

# Create MIME header
mime_message = MIMEMultipart()
mime_message['To'] = EMAIL_OBJECT.from_addr
mime_message['From'] = EMAIL_OBJECT.to_addr
mime_message['Subject'] = EMAIL_OBJECT.subject

# Create and attach MIME body
mime_message.attach(
    payload=MIMEText(
        _text=EMAIL_OBJECT.body,
        _subtype='plain'
    )
)

# Create smtplib object
print(f'Connecting to {SMTP_HOST}:{SMTP_PORT}...', end='')
with smtplib.SMTP(
    host=SMTP_HOST,
    port=SMTP_PORT
) as smtp_object:
    print('done.')

    # Send EHLO message
    print('\nSending EHLO message...', end='')
    smtp_object.ehlo()
    print('done.')

    # Start TLS session
    print('\nStarting TLS session...', end='')
    smtp_object.starttls()
    print('done.')

    # Perform SMTP login
    print('\nLogging on to server...', end='')
    smtp_object.login(
        user=EMAIL_OBJECT.from_addr,
        password=getenv('APP_PW')
    )
    print('done.')

    # Send the email message
    print('\nSending email messsage...', end='')
    smtp_object.sendmail(
        from_addr=EMAIL_OBJECT.from_addr,
        to_addrs=[EMAIL_OBJECT.to_addr] + EMAIL_OBJECT.bcc_list,
        msg=mime_message.as_string()
    )
    print('done.')
