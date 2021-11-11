#!/usr/bin/env python3
""" Docstring """

# Imports - Python Standard Library
from collections import namedtuple

# Imports - Third-Party
import requests

# Imports - Local

# namedtuples
# namedtuple of API endpoints
APIEndpoints = namedtuple(
    typename='APIEndpoints',
    field_names=[
        'name',
        'director',
        'imdb'
    ]
)

HTTPMethods = namedtuple(
    typename='HTTPMethods',
    field_names=[
        'get',
        'post'
    ]
)

# Constants
BASE_URL = 'https://movieservice.talkpython.fm/api'
ENDPOINTS = APIEndpoints(
    name='search',
    director='director',
    imdb='movie'
)
HTTP_METHODS = HTTPMethods(
    get='GET',
    post='POST'
)
HTTP_TIMEOUT = 5


def find_movie_by_title(keyword):
    """ Docstring """

    #
    url = f'{BASE_URL}/{ENDPOINTS.name}/{keyword}'

    response = requests.get(
        url=url,
        timeout=5
    )

    #
    response.raise_for_status()

    return response
