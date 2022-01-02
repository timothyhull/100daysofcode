#!/usr/bin/env python3
""" User interface to consume blog_client.BlogClient. """

# Imports - Python Standard Library
from sys import exit
from typing import Dict

# Imports - Third-party
from requests.models import Response

# Imports - Local
from _55.app.blog_client import BlogClient


def select_entry(
    response: Response
) -> int:
    """ Prompt user to select a blog entry from a list.

        Args:
            response (requests.models.Response):
                requests response object returned by the HTTP API call.

        Returns:
            user_choice (int):
                Valid user choice.
    """

    # Define a try/except block to catch keyboard interrupts gracefully
    try:
        # Start validation loop
        while True:
            # Prompt for user input
            try:
                # Collect input and subtract 1, to pair with list index numbers
                user_choice = int(
                    input('Which blog entry would you like to read? ')
                ) - 1
            except ValueError:
                print(
                    '\n** Invalid input. Please try again. **\n'
                )
                continue

            # Validate user choice:
            if user_choice in range(len(response.json())):
                break
            else:
                print(
                    f'\n** No blog entry "{user_choice + 1}" found. '
                    'Please try again. **\n'
                )

    except KeyboardInterrupt:
        print('\nEscape sequence read, exiting program.\n')
        exit()

    return user_choice


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

    # Display blog entry header
    header = '** Blog Entries **'
    print(header)
    print('-' * len(header))

    # Display a list of blog entries for selection
    for index, entry in enumerate(response.json()):
        print(
            f'{index + 1}. {entry.get("title")} '
            f'[{entry.get("view_count", "Unknown"):,} views]'
        )
    print()

    # Prompt user for blog entry selection
    blog_entry_number = select_entry(
        response=response
    )

    # Assign the blog entry data to a variable
    blog_entry = client.get_entry(
        entry_id=response.json()[blog_entry_number]['id']
    )

    # Display the blog entry title
    blog_entry = blog_entry.json()
    blog_title = f'** {blog_entry.get("title", "Unknown")} **'
    print(f'\n{blog_title}')
    print("-" * len(blog_title))

    # Display the blog entry
    print(f'{blog_entry.get("content", "Unknown")}\n')
    print(f'Published on {blog_entry.get("published", "Unknown")}\n')

    return response


def get_write_entry_input() -> Dict:
    """ TODO """

    pass


def write_entries() -> Response:
    """ TODO """

    print(
        # TODO - this will eventually be response.json().get('id')
        f'\nSuccessfully created a new post with the id "{True}".'
    )

    pass


def get_user_input() -> None:
    """ Collect user input to read or write API entry data.

        Args:
            None.

        Returns:
            user_input (str):
                Either 'r' or 'w'.
    """

    # Define a try/except block to catch keyboard interrupts gracefully
    try:
        # Display a banner
        print('\nWhat would you like to do next?\n')

        # Collect user input
        user_input = input(
            '[w]rite a post, or [r]ead posts? '
        ).lower().strip()

        # Handle input with conditionals
        if user_input == 'r':
            print('Read posts...\n')
        elif user_input == 'w':
            print('Write a post...\n')
        else:
            print(
                f'\n** Invalid input "{user_input}", Please try again. **\n'
            )
    except KeyboardInterrupt:
        print('\nEscape sequence read, exiting program.\n')
        exit()

    return user_input


def main() -> None:
    """ Main program.

        Runs prescribed functions in order.

        Args:
            None.

        Returns:
            None.
    """

    # Collect user input
    user_input = get_user_input()

    # Call a blog read function
    if user_input == 'r':
        read_entries()

    elif user_input == 'w':
        write_entries

    return None


if __name__ == '__main__':
    main()
