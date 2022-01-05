#!/usr/bin/env pytest
""" pytest Tests for api_client.py """

# Imports - Python Standard Library

# Imports - Third-Party
from pytest import fixture
from requests_mock.mocker import Mocker

# Imports - Local
from _56.movie_search.app.api_client import (
    MovieSearchClient, BASE_URL, MOVIE_ENDPOINT
)

# Constants
MOVIE_KEYWORD = 'term'
DIRECTOR_ENDPOINT = 'cameron'
IMDB_CODE_ENDPOINT = 'tt0103064'
MOVIE_JSON = {
    'keyword': 'run',
    'hits': [
        {
            'imdb_code': 'tt0103064',
            'title': 'Terminator 2: Judgment Day',
            'director': 'James Cameron',
            'keywords': [
                'future',
                'sexy woman',
                'multiple cameos',
                'liquid metal',
                'time travel'
            ],
            'duration': 153,
            'genres': [
                'sci-fi',
                'action'
            ],
            'rating': 'R',
            'year': 1991,
            'imdb_score': 8.5
        }
    ]
}
DIRECTOR_JSON = {
    'keyword': 'cameron',
    'hits': [
        {
            'imdb_code': 'tt0103064',
            'title': 'Terminator 2: Judgment Day',
            'director': 'James Cameron',
            'keywords': [
                'future',
                'sexy woman',
                'multiple cameos',
                'liquid metal',
                'time travel'
            ],
            'duration': 153,
            'genres': [
                'sci-fi', 'action'
            ],
            'rating': 'R',
            'year': 1991,
            'imdb_score': 8.5
        }
    ]
}
IMDB_CODE_JSON = {
    'imdb_code': 'tt0103064',
    'title': 'Terminator 2: Judgment Day',
    'director': 'James Cameron',
    'keywords': [
        'future',
        'sexy woman',
        'multiple cameos',
        'liquid metal',
        'time travel'
    ],
    'duration': 153,
    'genres': [
        'sci-fi',
        'action'
    ],
    'rating': 'R',
    'year': 1991,
    'imdb_score': 8.5
}


@fixture
def movie_search_client() -> MovieSearchClient:
    """ pytest fixture to instantiante the class.

        Args:
            None.

        Returns:
            movie_search_client (MovieSearchClient):
                Object derrived from the MovieSearchClient class.
    """

    # Create and return an instance of the MovieSearchClient class
    movie_search_client = MovieSearchClient()

    return movie_search_client


def test_title_search(
    movie_search_client: MovieSearchClient,
    requests_mock: Mocker
) -> None:
    """ Test the title_search method in api_client.py.

        Args:
            movie_search_client (MovieSearchClient):
                Instance of the MovieSearchClient class.

            requests_mock (Mocker):
                Mock HTTP API request

        Returns:
            None

    """

    # Setup mock request
    url = f'{BASE_URL}{MOVIE_ENDPOINT}/{MOVIE_KEYWORD}'

    # Create the mock requests object
    requests_mock.get(
        url=url,
        status_code=200,
        json=MOVIE_JSON
    )

    # Call the title_search method
    response = movie_search_client.title_search(
        keyword=MOVIE_KEYWORD
    )

    assert response.json() == MOVIE_JSON

    return None
