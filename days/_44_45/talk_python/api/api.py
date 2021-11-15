#!/usr/bin/env python3
""" Talk Python to Me API Search Application.  """

# Imports - Python Standard Library
from collections import namedtuple

# Imports - Third-Party Modules
from typing import List
import requests

# namedtuple objects
SearchResults = namedtuple(
    typename='SearchResults',
    field_names=[
        'elapsed_ms',
        'keywords',
        'results'
    ]
)

# Constants
BASE_URL = 'https://search.talkpython.fm/api/search?q='
HTTP_TIMEOUT = 5


def talkpython_search(
    keyword: str
) -> List[SearchResults]:
    """ Search the Talk Python to Me API Application.

        Args:
            keyword (str):
                Keyword search string.

        Returns:
            TBD
    """

    # Setup the HTTP request
    url = f'{BASE_URL}{keyword}'

    # Send the HTTP request
    response = requests.get(
        url=url,
        timeout=HTTP_TIMEOUT
    )

    # Raise an HTTPError exception for a failed request
    response.raise_for_status()

    # Group results into a namedtuple
    r = response.json()
    search_results = SearchResults(
        elapsed_ms=r.get('elapsed_ms'),
        keywords=r.get('keywords'),
        results=r.get('results')
    )

    return search_results
