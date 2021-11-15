#!/usr/bin/env python3
""" Talk Python to Me Program Application.  """

# Imports - Python Standard Library
from webbrowser import open as web_open

# Imports - Local
from _44_45.talk_python.api.api import talkpython_search


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
    num_results = len(results.results)

    # Display banner message
    if num_results < 1:
        result_header = 'No search results'
    elif num_results == 1:
        result_header = '1 search result'
    else:
        result_header = f'{num_results} search results'

    display_banner(f'{result_header} for "{" ".join(results.keywords)}"')

    # Display search results
    for index, result in enumerate(results.results, 1):
        print(
            f'{index}. {result.get("title")}\n'
            f'\tURL: {result.get("url")}'
        )
    print()

    # Prompt user to select a link to open
    url_prompt = input(f'Choose a URL to open (1-{num_results}): ')

    # Construct the URL based on user input
    url = f'https://talkpython.fm{results.results[int(url_prompt) + 1]}'

    # Open a browser to the selected result
    web_open(
        url=url,
        new=2
    )


if __name__ == '__main__':
    main()
