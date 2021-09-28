#!/usr/bin/env python3
""" Copied from 100DaysOfCode Repository.
"""

from program import init_logging
from time import time
from typing import List
import logbook
import requests
import collections
import random

api_log = logbook.Logger('API Log')

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords,'
                               ' duration, genres, rating, year, imdb_score')


def find_movie_by_title(keyword: str) -> List[Movie]:
    # Set start time
    t0 = time()

    # Write log message to indicate start of search
    api_log.trace(
        f'Starting search with keyword "{keyword}"'
    )

    if not keyword or not keyword.strip():

        # Write a log message when the keyword is blank
        api_log.warn(
            'No keyword found.'
        )
        raise ValueError('Must specify a search term.')

    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'

    resp = requests.get(url)

    # Write a log message with the HTTP status/reason
    api_log.trace(
        f'Server response: {resp.status_code} {resp.reason}.'
    )

    resp.raise_for_status()

    results = resp.json()
    results = create_random_errors(results)

    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))

    # Set end time
    t1 = time()

    # Write log message to indicate end of search
    api_log.trace(
        f'Completed search for keyword "{keyword}", '
        f'{len(movies)} results in {int(1000 * (t1 - t0))} ms.'
    )

    return movies


def create_random_errors(results):
    # This is a method to occasionally create some more
    # interesting errors other than simply network connectivity errors
    # which are the only "real" errors. This will let us test
    # more types.

    num = random.randint(1, 20)
    if 16 < num <= 18:
        return {}  # Whoops! No data.
    elif 18 < num <= 20:
        raise StopIteration()

    return results  # no errors here.
