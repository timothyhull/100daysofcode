#!/usr/bin/env pytest
""" Tests the for api.py application. """

# Imports - Third-Party
from pytest import raises
from requests import HTTPError
import requests_mock.mocker

# Imports - Local
from _43.movie_search.app.api import (
    BASE_URL, ENDPOINTS, HTTP_METHODS, find_movie_by_title
)

# Constants
SEARCH_NAME = 'chicken'
JSON = {
    'keyword': 'chicken run',
    'hits': [
        {
            'imdb_code': 'tt0120630',
            'title': 'Chicken Run',
            'director': 'Peter Lord',
            'keywords': [
                'rooster',
                'escape',
                'chicken',
                'freedom',
                'farm'
            ],
            'duration': 84,
            'genres': [
                'adventure',
                'animation',
                'drama',
                'comedy',
                'family'
            ],
            'rating': 'G',
            'year': 2000,
            'imdb_score': 7.0
        }
    ],
    'truncated_results': False
}


def test_find_movie_by_title(
    requests_mock: requests_mock.mocker
) -> None:
    """ Test the find_movie_by_title function.

        Args:
            requests_mock (requests_mock.mocker):
                pytest requests mocker fixture.

        Returns:
            None
    """

    # Setup mock HTTP request and response values
    method = HTTP_METHODS.get
    url = f'{BASE_URL}/{ENDPOINTS.name}/{SEARCH_NAME}'
    json = JSON

    # Create the mock HTTP request
    requests_mock.request(
        method=method,
        url=url,
        json=json
    )

    # Call the function under test, requests_mock will replace the HTTP request
    response = find_movie_by_title(
        keyword=SEARCH_NAME
    )

    # Assert the keyword is found in the title attribute of the response
    assert SEARCH_NAME in response[0].title.lower()

    return None


def test_find_movie_by_title_exception(
    requests_mock: requests_mock.mocker
) -> None:
    """ Test the find_movie_by_title function for an exception.

        Args:
            requests_mock (requests_mock.mocker):
                pytest requests mocker fixture.

        Returns:
            None
    """

    # Setup mock HTTP request and response values
    method = HTTP_METHODS.get
    url = f'{BASE_URL}/{ENDPOINTS.name}/{SEARCH_NAME}'
    json = JSON

    # Create the mock HTTP request
    requests_mock.request(
        method=method,
        url=url,
        json=json,
        status_code=404
    )

    # Assert a 404 status code raises an HTTPError exception
    with raises(HTTPError):
        find_movie_by_title(
            keyword=SEARCH_NAME
        )

    return None
