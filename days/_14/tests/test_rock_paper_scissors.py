#!/usr/bin/env pytest

""" Test code for RPS_Objects.py.
"""

# Imports
from _14.rock_paper_scissors.rock_paper_scissors import display_banner, \
                                                        get_player_name, \
                                                        game_loop
from pytest import raises
from unittest.mock import patch

# Constants
BANNER_MSG = '** Let\'s Play Rock, Paper, Scissors **'
TEST_MSG = '** Test Message **'


# Tests
def test_display_banner(capfd):
    """ Test to confirm the printed output is correct (using 'capfd')
    """

    """ Call the function to test, 'display_banner' (required), by using
        an 'assert' statement to confirm the return value for the
        function is 'None'.
    """
    assert display_banner() is None

    # Assign the 'capfd.readouterr()[0]' value to a variable
    out = capfd.readouterr()[0]

    # Print the 'capfd' result
    print(out)

    # Verify the presence of the 'BANNER_MSG' value in the printed output
    assert BANNER_MSG in out

    # Perform a second test with a custom `msg` value
    assert display_banner(TEST_MSG) is None
    out = capfd.readouterr()[0]
    print(out)
    assert TEST_MSG in out


@patch(
    'builtins.input',
    side_effect=['Tim', '']
)
def test_get_player_name(side_effect):
    """ The 'side_effect' argument is a placeholder to send side_effect list
        values to the test function
    """

    # Test the first, valid side effect
    assert get_player_name() == 'Tim'

    # Test the second, invalid side effect raises the correct exception
    with raises(ValueError):
        get_player_name()


def test_game_loop():
    pass
