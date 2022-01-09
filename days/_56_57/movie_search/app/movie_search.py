#!/usr/bin/env python3
""" User interface for the Movie Search application. """

# Imports - Python Standard Library
from sys import exit
from typing import Union

# Imports - Third-Party
from requests.adapters import Response

# Imports - Local
from _56_57.movie_search.app.api_client import MovieSearchClient

# Constants
API_MAPPING = {
    1: 'title_search',
    2: 'director_search',
    3: 'imdb_code_search'
}


def display_keyboard_interrupt_message() -> None:
    """ Display an invalid input error message.

        Args:
            None.

        Returns:
            None.
    """

    print(
        '\nRead keyboard interrupt sequence, exiting program.\n'
    )

    return None


def display_banner() -> None:
    """ Display an application banner.

        Args:
            None.

        Returns:
            None.
    """

    # Create a banner message
    msg = '* Movie Search Application *'
    border = f'{"*" * len(msg)}'
    banner = (
        f'\n{border}\n'
        f'{msg}\n'
        f'{border}\n'
    )

    # Display the banner message
    print(banner)

    return None


def invalid_input_error() -> None:
    """ Display an invalid input error message.

        Args:
            None.

        Returns:
            None.
    """

    print(
        '\n** Invalid input, please try again **\n'
    )

    return None


def select_menu_option(
    pytest: bool = False
) -> Union[int, bool]:
    """ Display a menu and collect user selection input.

        Args:
            pytest (bool, optional):
                Only required for pytest test.  Breaks the input loop
                after invalid input.

        Returns:
            menu_choice (int or bool (False), optional):
                User input choice from the menu.  False only for pytest
                input error checks.
    """

    # Create an input loop
    while True:
        # Display menu
        print(
            '1. Search for a movie by title.\n'
            '2. Search for a movie by director name.\n'
            '3. Search for a movie by IMDB code.\n'
        )

        # Prompt for menu selection input
        menu_choice = input('Choose a search option (1-3): ')

        # Attempt to convert the input to an integer
        try:
            menu_choice = int(menu_choice)
        except ValueError:
            invalid_input_error()
            if pytest is True:
                menu_choice = False
                break
            else:
                continue

        if menu_choice in range(1, 4):
            break
        else:
            invalid_input_error()
            if pytest is True:
                menu_choice = False
                break
            else:
                continue

    return menu_choice


def get_keyword_input(
    pytest: bool = False
) -> Union[str, bool]:
    """ Collect user keyword search input.

        Args:
            pytest (bool, optional):
                Only required for pytest test.  Breaks the input loop
                after invalid input.

        Returns:
            keyword_input (str or bool (False), optional):
                User-entered keyword to search with.  False only for
                pytest input error checks.
    """

    # Create an input loop
    while True:

        # Prompt for input
        keyword_input = input('Enter the text to search for: ')

        # Break the loop if input exists
        if keyword_input:
            print(f'\nSearching for matches of "{keyword_input}"...')
            break
        else:
            if pytest is True:
                keyword_input = False
                break

    return keyword_input


def get_search_results(
    api_target: int,
    keyword_input: str
) -> Response:
    """ Request search results from the MovieSearchClient class.

        Args:
            api_target (int):
                Menu input value that maps to an API target, via the
                API_MAPPING constant.

            keyword_input (str):
                Keyword to search for.

        Returns:
            response (requests.adapters.Response):
                requests module response object.
    """

    # Instantiate a copy of the MovieSearchClient class
    movie_search_client = MovieSearchClient()

    # Send the search request
    response = movie_search_client.__getattribute__(
        API_MAPPING.get(api_target)
    )(
        keyword=keyword_input
    )

    return response


def main() -> None:
    """ Main program function.

        Runs application functions in the proper sequence.

        Args:
            None.

        Returns:
            None
    """

    # Display the banner when the program starts
    display_banner()

    # Collect a user search menu selection
    try:
        menu_choice = select_menu_option()
    except KeyboardInterrupt:
        display_keyboard_interrupt_message()
        exit()

    # Collect a user search keyword
    try:
        keyword_input = get_keyword_input()
    except KeyboardInterrupt:
        display_keyboard_interrupt_message()
        exit()

    # Get search results
    response = get_search_results(
        api_target=menu_choice,
        keyword_input=keyword_input
    )
    print(len(response.json().get('hits')))

    # TODO - Display search results

    return None


if __name__ == '__main__':
    main()
