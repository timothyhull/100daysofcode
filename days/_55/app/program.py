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

    # Check for HTTP errors
    response.raise_for_status()

    return response


def write_entries():
    """ TODO """

    pass


def get_user_input() -> None:
    """ Collect user input to read or write API entry data.

        Args:
            None.

        Returns:
            None.
    """

    # Display a banner
    print('\nWhat would you like to do next?\n')

    # Collect user input
    user_input = input(
        '[w]rite a post, or [r]ead posts? '
    ).lower().strip()

    # Handle input with conditionals
    if user_input == 'r':
        print('Read posts...\n')

    if user_input == 'w':
        print('Write a post...\n')

    print(
        f'\n\n** Invalid input "{user_input}", Please try again. **\n'
    )

    return None


def main() -> None:
    """ Main program.

        Runs prescribed functions in order.

        Args:
            None.

        Returns:
            None.
    """

    # Collect user input
    # Define a try/except block to catch keyboard interrupts gracefully
    try:
        user_input = get_user_input()

        # Process valid user input
        if user_input == 'r':
            pass
        elif user_input == 'w':
            pass

    # Handle KeyboardInterrupt exceptions
    except KeyboardInterrupt:
        print('\nEscape sequence read, exiting program.\n')


if __name__ == '__main__':
    main()
