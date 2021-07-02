#!/usr/bin/env pytest

""" Test code for RPS_Objects.py.
"""

# Imports
from _14.rock_paper_scissors.RPS_Objects import Player, Roll
from _14.rock_paper_scissors.rock_paper_scissors import display_banner, \
                                                        get_player_name, \
                                                        game_loop
from pytest import raises
from random import randint
from unittest.mock import patch

# Constants
BANNER_MSG = '** Let\'s Play Rock, Paper, Scissors **'
GAME_LOOPS = 3
PLAYER_1_NAME = 'Tim'
ROLLS = [
    'paper',
    'rock',
    'scissors'
]
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
    side_effect=[PLAYER_1_NAME, '']
)
def test_get_player_name(side_effect):
    """ The 'side_effect' argument is a placeholder to send side_effect list
        values to the test function
    """

    # Test the first, valid side effect
    assert get_player_name() == PLAYER_1_NAME

    # Test the second, invalid side effect raises the correct exception
    with raises(ValueError):
        get_player_name()


# Create a list of random numbers, to provide side_effect values
random_turns = []
for _ in range(1, GAME_LOOPS + 1):
    random_num_choice = randint(1, 3)
    random_turns.append(random_num_choice)


@patch(
    'builtins.input',
    side_effect=random_turns
)
def test_game_loop(side_effect):
    """ Test for a functional game loop
    """

    # Create player objects
    player_1 = Player(PLAYER_1_NAME)
    player_2 = Player()

    # Create a list of 3 rolls
    rolls = []
    for roll in ROLLS:
        rolls.append(Roll(roll))

    # Verify the game loop produces a result
    game_loop(
        player_1=player_1,
        player_2=player_2,
        rolls=rolls
    )
