#!/usr/bin/env python3
""" User interface to consume blog_client.BlogClient. """

# Imports - Python Standard Library

# Imports - Third-party
from requests.models import Response

# Imports - Local
from _55.app.blog_client import BlogClient


def read_entries() -> Response:
    """ Read blog entries.

        Args:
            None.

        Returns:
            response (requests.models.Response):
                Response object from the requests package.
    """

    # Define an instance of the BlogClient class
    client = BlogClient()

    # Set the response value
    response = client.get_all_entries()

    return response


def write_entries():
    """ TODO """

    pass


def main() -> None:
    """ Main program.

        Runs prescribed functions in order.

        Args:
            None.

        Returns:
            None.
    """

    # Define a try/except block to catch keyboard interrupts gracefully
    try:
        # Create a prompt loop
        while True:

            # Display a banner
            print('\nWhat would you like to do next?\n')

            # Collect user input, and catch exceptions for non-alpha characters
            try:
                user_input = input(
                    '[w]rite a post, or [r]ead posts? '
                ).lower().strip()
            except SyntaxError:
                print(f'\n* Invalid entry "{user_input}" *\n')
                raise

            # Handle input with conditionals
            if user_input == 'w':
                continue

            if user_input == 'r':
                continue

            print(
                f'\n\n** Invalid input "{user_input}," Please try again. **\n'
            )

    # Handle KeyboardInterrupt exceptions
    except KeyboardInterrupt:
        print('\nEscape sequence read, exiting program.\n')

    return None


if __name__ == '__main__':
    main()
