#!/usr/bin/env pytest
""" Docstring """

# Imports - Python Standard Library

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
        'keyword': SEARCH_NAME,
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
                ]
            }
        ]
    }


def test_find_movie_by_title(
    requests_mock: requests_mock.mocker
) -> None:
    """ Docstring """

    #
    method = HTTP_METHODS.get
    url = f'{BASE_URL}/{ENDPOINTS.name}/{SEARCH_NAME}'
    json = JSON

    #
    requests_mock.request(
        method=method,
        url=url,
        json=json
    )

    #
    response = find_movie_by_title(
        keyword=SEARCH_NAME
    )

    #
    assert SEARCH_NAME in response.json()['hits'][0]['title'].lower()

    return None


def test_find_movie_by_title_exception(
    requests_mock: requests_mock.mocker
) -> None:
    """ Docstring """

    #
    method = HTTP_METHODS.get
    url = f'{BASE_URL}/{ENDPOINTS.name}/{SEARCH_NAME}'

    #
    requests_mock.request(
        method=method,
        url=url,
        status_code=404
    )

    #
    with raises(HTTPError):
        find_movie_by_title(
            keyword=SEARCH_NAME
        )

    return None
