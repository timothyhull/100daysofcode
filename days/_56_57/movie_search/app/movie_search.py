#!/usr/bin/env python3
""" User interface for the Movie Search application. """

# Imports - Python Standard Library
from sys import exit
from typing import Union

# Imports - Third-Party
from requests.exceptions import HTTPError
from requests.models import Response

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
            response (requests.models.Response):
                requests module response object.
    """

    # Instantiate a copy of the MovieSearchClient class
    movie_search_client = MovieSearchClient()

    # Send the search request
    try:
        response = movie_search_client.__getattribute__(
            API_MAPPING.get(api_target)
        )(
            keyword=keyword_input
        )
    except HTTPError:
        if api_target == 3:
            print(f'\nInvalid IMDB code "{keyword_input}"')
            exit(1)
        else:
            raise

    return response


def display_search_results(
    response: Response
) -> None:
    """ Display search results from a Movie Search API response object.

        Args:
            response (requests.models.Response):
                requests module response object.

        Returns:
            None.
    """

    # Assign the json method result to the response variable
    response = response.json()

    # Determine the response count, if there is more than one result
    result_count = response.get('hits', None)
    if result_count is None:
        result_count = 1
        result_verb = 'result'
        hits = [response]
    else:
        result_count = len(response.get('hits', None))
        if result_count == 1:
            result_verb = 'result'
        else:
            result_verb = 'results'
        hits = response.get('hits')

    # Set an output message for 0 results
    if result_count == 0:
        output = '\nNo results found\n'

    # Set a plural or non-plural result verb and the hits variable
    else:
        # Set the results count display output
        result_header = (
            f'\n{result_count} {result_verb} found for the '
            f'keyword "{response.get("keyword", response.get("imdb_code"))}":'
        )

        # Create a list placeholder for individual result display output
        results = []

        # Add each individual result display to the results list
        for index, hit in enumerate(hits):
            results.append(
                f'{index + 1}. {hit.get("title", "Unknown")}\n'
                f'\tDirector: {hit.get("director", "Unknown")}\n'
                f'\tIMDB Code: {hit.get("imdb_code", "Unknown")}\n'
            )

        # Add the results set to the results count
        output = '\n'.join([result_header, '\n'.join(results)])

    # Display the output
    print(output)

    return None


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
        exit(0)

    # Collect a user search keyword
    try:
        keyword_input = get_keyword_input()
    except KeyboardInterrupt:
        display_keyboard_interrupt_message()
        exit(0)

    # Get search results
    response = get_search_results(
        api_target=menu_choice,
        keyword_input=keyword_input
    )

    # Display search results
    display_search_results(
        response=response
    )

    return None


if __name__ == '__main__':
    main()
