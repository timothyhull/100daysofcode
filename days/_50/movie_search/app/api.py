#!/usr/bin/env python3
""" Movie Search app API interface """

# Imports - Python Standard Library
from collections import namedtuple
from typing import List

# Imports - Third-Party
import requests

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

Movies = namedtuple(
    typename='Movies',
    field_names=[
        'imdb_code',
        'title',
        'director',
        'keywords',
        'duration',
        'genres',
        'rating',
        'year',
        'imdb_score'
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


def find_movie_by_title(keyword: str) -> List[Movies]:
    """ Search for movies by title.

        Args:
            keyword (str):
                Keyword search string.

        Returns:
            movies (List[Movies]):
                List of namedtuples with movie attributes.
    """

    # Setup URL string
    url = f'{BASE_URL}/{ENDPOINTS.name}/{keyword}'

    # Send the API request
    response = requests.get(
        url=url,
        timeout=5
    )

    # Raise a status exception for HTTP errors
    response.raise_for_status()

    # Create a movies list and insert namedtuples for each movie
    movies = []
    for movie in response.json()['hits']:
        movies.append(Movies(**movie))

    return movies
