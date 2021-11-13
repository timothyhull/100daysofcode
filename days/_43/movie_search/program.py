#!/usr/bin/env python3
""" Movie Search application user interface program. """

# Imports - Local
from _43.movie_search.app import api


def main() -> None:
    """ Main program run.

        Args:
            None.

        Returns:
            None.
    """

    # Collect user input
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

    # Display the results
    for index, movie in enumerate(response, 1):
        print(
            f'{index}. {movie.title} ({movie.year})\n'
            f'\tRating: {movie.rating}\n'
            f'\tIMDB Score: {movie.imdb_score}\n'
            f'\tIMDB Code: {movie.imdb_code}'
        )
    print()

    return None


if __name__ == '__main__':
    main()
