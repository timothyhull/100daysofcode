#!/usr/bin/env pytest
""" Tests for successful error handling in program.py
"""

# Imports
from _27.dnd_error_handling.actors import *
from pytest import raises
from unittest.mock import patch

from _27.dnd_error_handling.program import game_loop


def test_program_invalid_import() -> None:
    """ Test for proper exception handling of a module import exception.
        Attempt to import a bogus module, to determine if exception handling
        catches the problem.

        Args:
            None.

        Returns:
            None.
    """

    # Check import of bogus module 'Dragons' for ImportError
    with raises(ImportError):
        from _27.dnd_error_handling.actors import Dragons


@patch(
    target='builtins.input',
    side_effect=[
        'a',
        'bogus_1'
    ]
)
def test_game_loop_invalid_entry(inputs) -> None:
    """ Test for proper exception handling of invalid user input.

        Args:
            inputs (patch):
                pytest patch values placeholder variable.

        Returns:
            None.
    """

    with raises(ValueError):
        game_loop()
