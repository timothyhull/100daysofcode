#!/usr/bin/env pytest
""" Docstring """

# Imports - Python Standard Library
from unittest.mock import patch

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
    user_input,
    capsys: _pytest.capture.capsys,
) -> None:
    """ Docstring """

    #
    for keyword in INPUT_KEYWORDS:
        program.main()
        out = capsys.readouterr().out
        assert keyword in out

    return None
