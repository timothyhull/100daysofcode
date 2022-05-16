#!/usr/bin/env python3
""" Example code to paste a tag on an affiliate URL. """

# Imports - Python Standard Library
# from os import system
from sys import argv

# Imports - Third-Party
import pyperclip

# Imports - Local

# Constants
TAG = '?tag=thpybites'

# Create a virtual display with Xvfb
# system('Xvfb :99 -screen 0 1280x720x16 > /dev/null & export DISPLAY=:99')


def usage_msg() -> None:
    """ Display a usage message.

        Args:
            None.

        Returns:
            None.
    """

    print(
        '\nUsage: affiliate.py https://wwt.com\n'
    )

    return None


def create_tagged_link() -> None:
    """ Add a tag to a valid link

        Args:
            None.

        Returns:
            None.
    """

    # Create mock clipboard data with argument data
    if len(argv) == 2:
        pyperclip.copy(argv[1])

        # Read data from the OS clipboard into Python
        clipboard_data = pyperclip.paste()

        # Add a tag to valid links
        if clipboard_data.startswith('https://wwt.com'):
            new_link = f'{clipboard_data}/{TAG}'

            # Write data to the OS clipboard from Python
            pyperclip.copy(new_link)

            # Display a new link confirmation
            print(
                f'\nCopied "{new_link}" to the clipboard.\n'
            )

        else:
            usage_msg()

    else:
        usage_msg()


def main() -> None:
    """ Main application.

        Args:
            None.

        Returns:
            None.
    """

    create_tagged_link()

    return None


if __name__ == '__main__':
    main()
