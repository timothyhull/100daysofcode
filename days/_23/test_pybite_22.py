#!/usr/bin/env pytest
''' Tests for pybite_22.py

    Usage:
        pytest test_pybite_22.py pybite_22.py
'''

# Imports
from _23.pybite_22 import get_text
from re import compile, VERBOSE
from pytest import mark
from unittest.mock import patch

# Constants
HTML_PATTERN = r'''
    ^       # Search from the beginning of the line text
    <\w+>   # Opening HTML tag syntax, e.g. <div>
    .+      # All text between the opening and closing HTML tags
    <\/\w+>   # Closing HTML tag syntax, e.g. </div>
    $       # End of the line text
'''
HTML_TAG = compile(
    HTML_PATTERN,
    VERBOSE
)
TEXT_INPUT = ['This is a test']
TEXT_EXPECTED_RESULTS = [f'<p><strong>{t}</strong></p>' for t in TEXT_INPUT]
TEXT_TESTS = list(zip(TEXT_INPUT, TEXT_EXPECTED_RESULTS))


@mark.parametrize(
    'arg_value, return_value',
    TEXT_TESTS
)
def test_get_text(arg_value, return_value) -> None:
    ''' Test the decorated get_text function to determine if it returns
        text in HTML format.

        Args:
            arg_value (str):
                Argument to pass into function.
            return_value (str):
                Expexted return value based on argument value.

        Returns:
            None.
    '''

    assert get_text(arg_value) == return_value


@patch(
    'builtins.input',
    side_effect=TEXT_INPUT
)
def test_get_text_input(side_effects) -> None:
    ''' Test the decorated get_text function to determine if it returns
        text provided by an input() function in HTML format.

        Args:
            side_effects (list):
                List of values to pass to the input prompt.

        Returns:
            None.
    '''

    for text in TEXT_EXPECTED_RESULTS:
        assert get_text() == text
