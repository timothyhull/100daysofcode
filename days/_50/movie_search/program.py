#!/usr/bin/env python3
""" Movie Search application user interface program. """

# Imports - Python Standard Library
from cProfile import Profile
from sys import argv
from typing import List

# Imports - Local
from _50.movie_search.app import api

# Create profiler object and disable profiling
profile = Profile()
profile.disable()


def keyword_argument_check(
    sys_args: List = argv
) -> str:
    """ Check for search keyword CLI arguments.

        Check the sys.argv list object to determine if any arguments
        exist, then validate and return an the value of an argument
        as keyword search input.

        Args:
            sys_args (List, optional):
                List of arguments, defaults to sys.argv.

        Returns:
            keyword (str):
                Valid keyword search input.
    """

    # Set a default value for keyword
    keyword = ''

    # Check for arguments
    if len(sys_args) > 1:
        # Check for at least one character
        if len(sys_args[1]) > 0:
            # Set the keyword variable to all but the first element in sys.argv
            keyword = ' '.join(sys_args[1:])

    return keyword


def main() -> None:
    """ Main program run.

        Args:
            None.

        Returns:
            None.
    """

    # Check for keywords passed in sys.argv
    keyword = keyword_argument_check()

    # Collect user input
    if len(keyword) == 0:
        keyword = input(
            'Search for movies by title: '
        )

    # Pass the user input to the function as an argument
    response = api.find_movie_by_title(keyword)

    # Count the number of responses
    hit_count = len(response)

    # Assemble the appropriate message based on the number of results
    if hit_count < 1:
        message = f'No results found for "{keyword}"'
    if hit_count == 1:
        message = f'1 result found for "{keyword}"'
    else:
        message = f'{hit_count} results found for "{keyword}"'

    # Display the message with a header banner
    print(
        f'\n{message}'
        f'\n{"-" * len(message)}'
    )

    # Enable profiler
    profile.enable()

    # Display the results
    for index, movie in enumerate(response, 1):
        print(
            f'{index}. {movie.title} ({movie.year})\n'
            f'\tRating: {movie.rating}\n'
            f'\tIMDB Score: {movie.imdb_score}\n'
            f'\tIMDB Code: {movie.imdb_code}'
        )
    print()

    # Disable profiler
    profile.disable()
    profile.print_stats(sort='cumtime')

    return None


if __name__ == '__main__':
    main()
