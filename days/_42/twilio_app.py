#!/usr/bin/env python3
""" Twilio SMS API Application.

    Requirements:
        requests

    Optional:
        python-dotenv

    Usage:
        from pybite_16.twilio_api import TwilioAPI
"""

# Imports - Third-Party
import dotenv

# Imports - Local
from _42.pybite_16.twilio_api import TwilioAPI

# Load Environmental Variables
dotenv.load_dotenv()

# Constants


def main() -> TwilioAPI:
    """ Main program.

        Creates an instance of the TwilioAPI  class.  Run this
        function in an interactive Python shell for testing:

        python3 -i twilio_api.py

        Args:
            None.

        Returns:
            twilio (TwilioAPI):
                Instance of the TwilioAPI class.
    """

    twilio = TwilioAPI(**dotenv.dotenv_values())

    return twilio


if __name__ == '__main__':
    twilio = main()
