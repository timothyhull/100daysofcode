#!/usr/bin/env python3
""" Docstring """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from _43.movie_search.app import api


def main() -> None:
    """ Docstring """

    #
    keyword = input(
        'Search for movies by title: '
    )

    #
    response = api.find_movie_by_title(keyword)
    hit_count = len(response)

    #
    if hit_count < 1:
        message = f'No results found for "{keyword}"'
    if hit_count == 1:
        message = f'1 result found for "{keyword}"'
    else:
        message = f'{hit_count} results found for "{keyword}"'

    #
    print(
        f'\n{message}'
        f'\n{"-" * len(message)}'
    )

    #
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
