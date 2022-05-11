#!/usr/bin/env python3
""" TODO """

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
        'body'
    ]
)

# Constants
EMAIL_OBJECT = EmailObject(
    from_addr=getenv('FROM_ADDR'),
    to_addr=getenv('TO_ADDR'),
    body=getenv('BODY')
)
SMTP_SERVER = smtplib.SMTP(
    host='smtp.gmail.com',
    port=587
)

# Send an Enhanced Hello message to the SMTP server
SMTP_SERVER.ehlo()

# Start TLS session
SMTP_SERVER.starttls()

# Perform SMTP login
SMTP_SERVER.login(
    user=EMAIL_OBJECT.from_addr,
    password=getenv('APP_PW')
)

# Send an email
SMTP_SERVER.sendmail(
    from_addr=EMAIL_OBJECT.from_addr,
    to_addrs=EMAIL_OBJECT.to_addr,
    msg=EMAIL_OBJECT.body
)

# Close the connection to the SMTP server
SMTP_SERVER.quit()
