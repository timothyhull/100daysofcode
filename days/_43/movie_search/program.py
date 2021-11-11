#!/usr/bin/env python3
""" Docstring """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from _43.movie_search.app import api

# Constants
SEARCH_NAME = 'run'


def main() -> None:
    """ Docstring """

    #
    response = api.find_movie_by_title(SEARCH_NAME)
    hits = response.json()['hits']
    search_term = response.json()['keyword']
    count = len(hits)

    #
    if count < 1:
        message = f'No results found for "{search_term}"'
    if count == 1:
        message = f'1 result found for "{search_term}"'
    else:
        message = f'{count} results found for "{search_term}"'

    #
    print(
        f'\n{message}'
        f'\n{"-" * len(message)}'
    )

    #
    for index, hit in enumerate(hits, 1):
        print(f'{index}. {hit["title"]}')
    print()

    return False


if __name__ == '__main__':
    main()
