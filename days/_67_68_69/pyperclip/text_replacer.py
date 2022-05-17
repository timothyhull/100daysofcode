#!/usr/bin/env python3
""" Text replacement demo app for Pyperclip """

# Imports - Python Standard Library

# Imports - Third-Party
from os import system
import pyperclip

# Imports - Local

# Create a virtual display with Xvfb
system('Xvfb :99 -screen 0 1280x720x16 & export DISPLAY=:99')

# Read data from the OS clipboard into Python
clipboard_data = pyperclip.paste()

# Write data to the OS clipboard from Python
pyperclip.copy(clipboard_data.upper())
