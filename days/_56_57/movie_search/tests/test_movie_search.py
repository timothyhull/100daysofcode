#!/usr/bin/env pytest
""" pytest Tests for movie_search.py """

# Imports - Python Standard Library
from collections import namedtuple
from unittest.mock import MagicMock, patch

# Imports - Third-Party
from _pytest.capture import CaptureFixture

# Imports - Local
from _56_57.movie_search.app.movie_search import (
    display_keyboard_interrupt_message, display_banner, invalid_input_error,
    select_menu_option, keyword_input
)

# namedtuple Objects
KeywordInput = namedtuple(
    typename='KeywordInput',
    field_names=[
        'title',
        'director',
        'imdb_code',
        'bad_input'
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
    'a'
    ''
]
MENU_ERROR_MSG = '** Invalid input, please try again **'
KEYWORD_INPUT = KeywordInput(
    title='term',
    director='cameron',
    imdb_code='tt0103064',
    bad_input=''
)
KEYWORD_OUTPUT = 'Searching for matches of'
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
def test_keyword_input(
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
        keyword_input(
            # pytest=True
        )

        # Capture STDOUT contents
        output = capsys.readouterr().out

        # Create required response message
        response_message = f'{KEYWORD_OUTPUT} "{keyword}"...'

        # Assert the required response is present
        assert response_message in output

    return None
