#!/usr/bin/env pytest
""" Test the program.py application. """

# Imports - Python Standard Library
from unittest.mock import MagicMock, patch

# Imports - Third-Party
import _pytest.capture

# Imports - Local
from _43.movie_search import program

# Constants
INPUT_KEYWORDS = [
    'terminator',
    'run',
    'home'
]


@patch(
    'builtins.input',
    side_effect=INPUT_KEYWORDS
)
def test_main_program_output(
    user_input: MagicMock,
    capsys: _pytest.capture.capsys,
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
