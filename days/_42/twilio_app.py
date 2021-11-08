#!/usr/bin/env python3
""" Twilio SMS API Application.

    Requirements:
        requests

    Optional:
        python-dotenv

    Usage:
        from pybite_16.twilio_api import TwilioAPI
"""

# Imports - Python Standard Library
from typing import Dict

# Imports - Third-Party
import dotenv

# Imports - Local
from _42.pybite_16.twilio_api import TwilioAPI

# Load Environmental Variables
dotenv.load_dotenv()

# Constants


def main() -> Dict:
    """ Main program.

        Args:
            None.

        Returns:
            None.
    """

    twilio = TwilioAPI(**dotenv.dotenv_values())

    return twilio


if __name__ == '__main__':
    twilio = main()
