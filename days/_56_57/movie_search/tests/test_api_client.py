#!/usr/bin/env pytest
""" pytest Tests for api_client.py """

# Imports - Python Standard Library

# Imports - Third-Party
from pytest import fixture, raises
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker

# Imports - Local
from _56_57.movie_search.app.api_client import (
    MovieSearchClient, BASE_URL, MOVIE_ENDPOINT, DIRECTOR_ENDPOINT,
    IMDB_CODE_ENDPOINT
)

# Constants
MOVIE_KEYWORD = 'term'
DIRECTOR_KEYWORD = 'cameron'
IMDB_CODE_KEYWORD = 'tt0103064'
MOVIE_JSON = {
    'keyword': 'term',
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


def test_title_search_error(
    movie_search_client: MovieSearchClient,
    requests_mock: Mocker
) -> None:
    """ Test for HTTP errors int title_search method, in api_client.py.

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
        status_code=401,
    )

    # Call the title_search method within a context manager
    with raises(HTTPError):
        movie_search_client.title_search(
            keyword=MOVIE_KEYWORD
        )

    return None


def test_director_search(
    movie_search_client: MovieSearchClient,
    requests_mock: Mocker
) -> None:

    """ Test the director_search method in api_client.py.

        Args:
            movie_search_client (MovieSearchClient):
                Instance of the MovieSearchClient class.

            requests_mock (Mocker):
                Mock HTTP API request

        Returns:
            None
    """

    # Setup mock request
    url = f'{BASE_URL}{DIRECTOR_ENDPOINT}/{DIRECTOR_KEYWORD}'

    # Create the mock requests object
    requests_mock.get(
        url=url,
        json=DIRECTOR_JSON,
        status_code=200
    )

    # Call the director_search method
    response = movie_search_client.director_search(
        keyword=DIRECTOR_KEYWORD
    )

    assert response.json() == DIRECTOR_JSON


def test_director_search_error(
    movie_search_client: MovieSearchClient,
    requests_mock: Mocker
) -> None:
    """ Test for HTTP errors int director_search method,
        in api_client.py.

        Args:
            movie_search_client (MovieSearchClient):
                Instance of the MovieSearchClient class.

            requests_mock (Mocker):
                Mock HTTP API request

        Returns:
            None
    """

    # Setup mock request
    url = f'{BASE_URL}{DIRECTOR_ENDPOINT}/{DIRECTOR_KEYWORD}'

    # Create the mock requests object
    requests_mock.get(
        url=url,
        status_code=403,
    )

    # Call the title_search method within a context manager
    with raises(HTTPError):
        movie_search_client.director_search(
            keyword=DIRECTOR_KEYWORD
        )

    return None


def test_imdb_code_search(
    movie_search_client: MovieSearchClient,
    requests_mock: Mocker
) -> None:

    """ Test the imdb_code_search method in api_client.py.

        Args:
            movie_search_client (MovieSearchClient):
                Instance of the MovieSearchClient class.

            requests_mock (Mocker):
                Mock HTTP API request

        Returns:
            None
    """

    # Setup mock request
    url = f'{BASE_URL}{IMDB_CODE_ENDPOINT}/{IMDB_CODE_KEYWORD}'

    # Create the mock requests object
    requests_mock.get(
        url=url,
        json=IMDB_CODE_JSON,
        status_code=200
    )

    # Call the imdb_code_search method
    response = movie_search_client.imdb_code_search(
        keyword=IMDB_CODE_KEYWORD
    )

    assert response.json() == IMDB_CODE_JSON


def test_imdb_code_search_error(
    movie_search_client: MovieSearchClient,
    requests_mock: Mocker
) -> None:
    """ Test for HTTP errors int imdb_code_search method,
        in api_client.py.

        Args:
            movie_search_client (MovieSearchClient):
                Instance of the MovieSearchClient class.

            requests_mock (Mocker):
                Mock HTTP API request

        Returns:
            None
    """

    # Setup mock request
    url = f'{BASE_URL}{IMDB_CODE_ENDPOINT}/{IMDB_CODE_KEYWORD}'

    # Create the mock requests object
    requests_mock.get(
        url=url,
        status_code=404,
    )

    # Call the imdb_code_search method within a context manager
    with raises(HTTPError):
        movie_search_client.imdb_code_search(
            keyword=IMDB_CODE_KEYWORD
        )

    return None
