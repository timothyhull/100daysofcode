#!/usr/bin/env pytest
""" Test the program.py application. """

# Imports - Python Standard Library
from unittest.mock import MagicMock, patch

# Imports - Third-Party
import _pytest.capture

# Imports - Local
from _50.movie_search import program

# Constants
ARGUMENT_KEYWORDS = [
    'program.py',
    'the',
    'term'
]

ARGUMENT_RESULT = 'the term'

INPUT_KEYWORDS = [
    'terminator',
    'run',
    'home'
]


def test_keyword_argument_check() -> None:
    """ Test the keyword_argument_check function

        Args:
            None.

        Returns:
            None.
    """

    # Call the keyword_argument_check function with a custom list of arguments
    keywords = program.keyword_argument_check(
        sys_args=ARGUMENT_KEYWORDS
    )

    # Assert the keywords ARGUMENT_RESULT string is in STDOUT
    assert keywords == ARGUMENT_RESULT

    return None


@patch(
    'builtins.input',
    side_effect=INPUT_KEYWORDS
)
def test_main_program_output(
    user_input: MagicMock,
    capsys: _pytest.capture.capsys
) -> None:
    """ Test the main function.

        Args:
            user_input (MagicMock):
                Mocked user input.

            capsys (_pytest.capture.capsys):
                STDOUT output capture.
    """

    # Loop over the test mock input keywords and call the main function
    for keyword in INPUT_KEYWORDS:
        program.main()

        # Capture the STDOUT output
        out = capsys.readouterr().out

        # Assert the mocked input keyword is in the STDOUT capture
        assert keyword in out

    return None
