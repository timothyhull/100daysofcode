#!/usr/bin/env python3
""" Talk Python to Me Program Application.  """

# Imports - Python Standard Library

# Imports - Third-Party Modules

# Imports - Local
from _44.talk_python.api.api import talkpython_search


def display_banner(message: str) -> None:
    """ Display a message with a banner.

        Args:
            message (str):
                String message to display as a banner.
    """

    print(
        f'\n{message}\n'
        f'{"-" * len(message)}'
    )

    return None


def main() -> None:
    """ Main program. """

    # Display input banner message
    display_banner('TalkPython API Search')

    # Collect search keyword input
    keyword = input('Enter search keywords: ')

    # Send search request
    results = talkpython_search(keyword)

    # Display banner message
    display_banner(f'Search Results for "{" ".join(results["keywords"])}"')

    # Display search results
    for index, result in enumerate(results['results'], 1):
        if result['category'] == 'Episode':
            print(f'{index}. {result["title"]}')


if __name__ == '__main__':
    main()
