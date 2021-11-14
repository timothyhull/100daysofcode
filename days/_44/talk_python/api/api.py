#!/usr/bin/env python3
""" Talk Python to Me API Search Application.  """

# Imports - Python Standard Library

# Imports - Third-Party Modules
from typing import Dict
import requests

# Imports - Local

# Constants
BASE_URL = 'https://search.talkpython.fm/api/search?q='
HTTP_TIMEOUT = 5


def talkpython_search(
    keyword: str
) -> Dict:
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

    return response.json()
