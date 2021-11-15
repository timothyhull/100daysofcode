#!/usr/bin/env pytest
""" pytest tests for api.py  """

# Imports - Python Standard Library

# Imports - Third-Party Modules
from pytest import mark
import requests_mock.mocker

# Imports - Local
from _44.talk_python.api.api import (
    talkpython_search, BASE_URL
)

# Constants
JSON = {
    'elapsed_ms': 0.11299999999999999,
    'keywords': ['100daysofcode'],
    'results': [
        {
            'category': 'Episode',
            'description': 'How do you learn libraries or parts of Python '
                           "itself that you don't have actual work projects "
                           "involving them? Whether that's SQLAlchemy, Slack "
                           'bots, or map APIs, actually building projects '
                           '(small and large) with them is really the only '
                           'way to gain true competency.',
            'id': 140,
            'title': 'Level up your Python with #100DaysOfCode challenge',
            'url': (
                '/episodes/show/140/level-up-your-python-with-'
                '100daysofcode-challenge'
            )
        },
        {
            'category': 'Transcript',
            'description': 'How do you learn libraries or parts of Python '
                           "itself that you don't have actual work projects "
                           "involving them? Whether that's SQLAlchemy, Slack "
                           'bots, or map APIs, actually building projects '
                           '(small and large) with them is really the only '
                           'way to gain true competency.',
            'id': 140,
            'title': 'Level up your Python with #100DaysOfCode challenge',
            'url': (
                '/episodes/transcript/140/level-up-your-python-with-'
                '100daysofcode-challenge'
            )
        }
    ]
}
SEARCH_KEYWORDS = [
    '100daysofcode',
    'pytest',
    'requests'
]
EXPECTED_RESULTS = [
    'category',
    'description',
    'title'
]


@mark.parametrize(
    argnames=[
        'keyword',
        'expected_result'
    ],
    argvalues=zip(
            SEARCH_KEYWORDS,
            EXPECTED_RESULTS
        )
)
def test_api_talkpython_search(
    requests_mock: requests_mock.mocker,
    keyword: str,
    expected_result: str
) -> None:
    """ Test the talkpython_search function api.

        Args:
            requests_mock (requests_mock.mocker):
                pytest requests mocker fixture.

            keyword (str):
                Search keywords.

            expected_results (str):
                Expected test result dictionary key names.

        Returns:
            None.
    """

    # Setup mock requests object values
    url = f'{BASE_URL}{keyword}'
    json = JSON

    # Setup mock requests object
    requests_mock.get(
        url=url,
        json=json
    )

    # Send mock request
    response = talkpython_search(keyword)

    # Assert the response matches the expected value
    assert expected_result in response['results'][0].keys()

    return None
