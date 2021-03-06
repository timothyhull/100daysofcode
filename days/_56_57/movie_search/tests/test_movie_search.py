#!/usr/bin/env pytest
""" pytest Tests for movie_search.py """

# Imports - Python Standard Library
from collections import namedtuple
from typing import Dict
from unittest.mock import MagicMock, patch

# Imports - Third-Party
from _pytest.capture import CaptureFixture
from pytest import raises
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker

# Imports - Local
from _56_57.movie_search.app.movie_search import (
    display_keyboard_interrupt_message, display_banner, invalid_input_error,
    select_menu_option, get_keyword_input, get_search_results,
    display_search_results
)

from _56_57.movie_search.app.api_client import (
    BASE_URL, MOVIE_ENDPOINT
)

# namedtuple Objects
KeywordInput = namedtuple(
    typename='KeywordInput',
    field_names=[
        'title',
        'director',
        'imdb_code',
    ]
)

# Constants
KEYBOARD_INTERRUPT_OUTPUT = '''
Read keyboard interrupt sequence, exiting program.
'''.strip()
BANNER_OUTPUT = '''
****************************
* Movie Search Application *
****************************
'''.strip()
MENU_INPUT = [
    1,
    2,
    3,
    0,
    'a',
    ''
]
MENU_ERROR_MSG = '** Invalid input, please try again **'
KEYWORD_INPUT = KeywordInput(
    title='term',
    director='cameron',
    imdb_code='tt0103064'
)
KEYWORD_OUTPUT = 'Searching for matches of'
MOVIE_KEYWORD = 'term'
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
RESULTS_OUTPUT = (
    f'1 result found for the keyword "{KEYWORD_INPUT.title}":\n'
    f'1. {MOVIE_JSON["hits"][0].get("title")}\n'
    f'\tDirector: {MOVIE_JSON["hits"][0].get("director")}\n'
    f'\tIMDB Code: {MOVIE_JSON["hits"][0].get("imdb_code")}\n'
)


# class objects
class MockResponse:
    """ Mock requests module response object. """

    def __init__(
        self,
        movie_json: Dict = MOVIE_JSON,
        ok: bool = True,
        status_code: int = 200,
        text: str = str(MOVIE_JSON)
    ) -> None:
        """ Initialize default values.

            Args:
                movie_json (Dict, optional):
                    JSON value to return from the json method. Default
                    value is MOVIE_JSON.

                ok (bool, optional):
                    Boolean value of the ok attribute. Default value
                    is True.

                status_code (int, optional):
                    Boolean value of the status_code attribute. Default value
                    is 200.

                text (str, optional):
                    String value of the text attribute. Default value
                    is a string of _movie_json.

            Returns:
                None.
        """

        # Set default values
        self._movie_json = movie_json
        self.ok = ok
        self.status_code = status_code
        self.text = str(movie_json)

        return None

    def json(self):
        """ Return self.movie_json value.

            Args:
                None.

            Returns:
                self._movie_json (Dict):
                    Value of self._movie_json
        """

        return self._movie_json


def test_display_keyboard_interrupt_message(
    capsys: CaptureFixture
) -> None:
    """ Test the display_keyboard_interrupt_message function.

        Args:
            capsys (_pytest.capture.CaptureFixture):
                pytest fixture to capture STDOUT contents.

        Returns:
            None.
    """

    # Call the function
    display_keyboard_interrupt_message()

    # Collect STDOUT output
    output = capsys.readouterr().out

    # Assert that the expected output displays
    assert KEYBOARD_INTERRUPT_OUTPUT in output


def test_display_banner(
    capsys: CaptureFixture
) -> None:
    """ Test the display_banner function.

        Args:
            capsys (_pytest.capture.CaptureFixture):
                pytest fixture to capture STDOUT contents.

        Returns:
            None.
    """

    # Call the display_banner function
    display_banner()

    # Collect STDOUT output
    output = capsys.readouterr().out

    # Assert the expected banner displays
    assert BANNER_OUTPUT in output


def test_invalid_input_error(
    capsys: CaptureFixture
) -> None:
    """ Test the invalid_input_error function.

        Args:
            capsys (_pytest.capture.CaptureFixture):
                pytest fixture to capture STDOUT contents.

        Returns:
            None.
    """

    # Call the function
    invalid_input_error()

    # Collect STDOUT output
    output = capsys.readouterr().out

    # Assert that the expected output displays
    assert MENU_ERROR_MSG in output


@patch(
    target='builtins.input',
    side_effect=MENU_INPUT
)
def test_select_menu_option(
    menu_input: MagicMock,
    capsys: CaptureFixture
) -> None:
    """ Test the display_banner function.

        Args:
            menu_input (unittest.mock.MagicMock):
                Mock input values for user input prompts.

            capsys (_pytest.capture.CaptureFixture):
                pytest fixture to capture STDOUT contents.

        Returns:
            None.
    """

    # Function call #1 - mocked user input "1"
    assert select_menu_option() == 1

    # Function call #2 - mocked user input "2"
    assert select_menu_option() == 2

    # Function call #3  - mocked user input "3"
    assert select_menu_option() == 3

    # Function calls #4, #5, #6 - mocked user input "4, 0, ''"
    for _ in MENU_INPUT[3:]:
        select_menu_option(
            pytest=True
        )

        # Capture STDOUT contents and assert input error message is present
        output = capsys.readouterr().out
        assert MENU_ERROR_MSG in output

    return None


@patch(
    target='builtins.input',
    side_effect=KEYWORD_INPUT._asdict().values()
)
def test_get_keyword_input(
    user_keyword_input: MagicMock,
    capsys: CaptureFixture
) -> None:
    """ Test the keyword_input function.

        Args:
            user_keyword_input (unittest.mock.MagicMock):
                Mock input values for user input prompts.

            capsys (_pytest.capture.CaptureFixture):
                pytest fixture to capture STDOUT contents.

        Returns:
            None.
    """

    # Loop over side_effect values
    for keyword in KEYWORD_INPUT._asdict().values():

        # Call the keyword_input function
        get_keyword_input(
            pytest=True
        )

        # Capture STDOUT contents
        output = capsys.readouterr().out

        # Create required response message
        response_message = f'{KEYWORD_OUTPUT} "{keyword}"...'

        # Assert the required response is present
        assert response_message in output

    return None


def test_get_search_results(
    requests_mock: Mocker
) -> None:
    """ Test the keyword_input function.

        Args:
            requests_mock (request.mocker.Mocker):
                Mock HTTP client requests object.

        Returns:
            None.
    """

    # Setup mock HTTP request
    url = f'{BASE_URL}{MOVIE_ENDPOINT}/{MOVIE_KEYWORD}'

    # Create mock HTTP request
    requests_mock.get(
        url=url,
        json=MOVIE_JSON,
        status_code=200
    )

    # Call the get_search_results function
    response = get_search_results(
        api_target=1,
        keyword_input=MOVIE_KEYWORD
    )

    assert MOVIE_JSON == response.json()

    return None


def test_get_search_results_error(
    requests_mock: Mocker
) -> None:
    """ Test the keyword_input function.

        Args:
            requests_mock (request.mocker.Mocker):
                Mock HTTP client requests object.

        Returns:
            None.
    """

    # Setup mock HTTP request
    url = f'{BASE_URL}{MOVIE_ENDPOINT}/{MOVIE_KEYWORD}'

    # Create mock HTTP request
    requests_mock.get(
        url=url,
        status_code=404
    )

    # Call the get_search_results function, check for HTTPError
    with raises(HTTPError):
        get_search_results(
            api_target=1,
            keyword_input=MOVIE_KEYWORD
        )

    return None


def test_display_search_results(
    capsys: CaptureFixture
) -> None:
    """
    Test the display_search_results function.

        Args:
            capsys (_pytest.capture.CaptureFixture):
                pytest fixture to capture STDOUT contents.

        Returns:
            None.
    """

    # Instantiate a copy of the mock_response class
    mock_response = MockResponse()

    # Call the display_search_results function
    display_search_results(
        response=mock_response
    )

    # Collect STDOUT output
    output = capsys.readouterr().out

    assert RESULTS_OUTPUT in output

    return None
