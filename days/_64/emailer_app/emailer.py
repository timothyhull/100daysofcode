#!/usr/bin/env python3
""" TODO """

# Imports - Python Standard Library
from os import getenv
import smtplib

# Imports - Third-Party
from dotenv import load_dotenv

# Imports - Local

# Load environment variables
load_dotenv()

# Constants
FROM_ADDR = getenv('FROM_ADDR')
TO_ADDR = getenv('FROM_ADDR')
