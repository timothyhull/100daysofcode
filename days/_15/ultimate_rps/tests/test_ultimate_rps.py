#!/usr/bin/env pytest
""" Test functions for Ultimate Rock, Paper, Scissors (Ultimate RPS).

    Usage:
        pytest ultimate_rps.py
"""

# Imports
from _15.ultimate_rps.UltimateRPS import UltimateRPS
from pytest import fixture, mark
from random import randint

# Constants
PLAYER_PLAYS = [
    'Scissors',
    'Paper',
    'Rock',
    'Air',
    'Devil',
    'Tree',
    'Snake',
    'Wolf',
    'Fire',
    'Sponge'
]
COMPUTER_PLAYS = [
    'Rock',
    'Paper',
    'Scissors',
    'Dragon',
    'Human',
    'Lightning',
    'Snake',
    'Water',
    'Gun',
    'Sponge'
]
EXPECTED_RESULTS = [
    'lose',
    'draw',
    'win',
    'win',
    'win',
    'lose',
    'draw',
    'win',
    'lose',
    'draw'
]
GAMEPLAY_ARGS = zip(
    PLAYER_PLAYS,
    COMPUTER_PLAYS,
    EXPECTED_RESULTS
)


@fixture
def ultimate_rps_object():
    """ pytest figture to instantiate a full UltimateRPS object.

        Args:
            None.

        Returns:
            ultimate_rps (class UltimateRPS): Ultimate Rock, Paper, Scissors,
                                              game object.
    """
    ultimate_rps = UltimateRPS()

    return ultimate_rps


@fixture
def battle_table(ultimate_rps_object):
    """ pytest fixture to read data from the CSV file with
        the 'battle-table.csv' matrix.

        Args:
            ultimate_rps_object (class UltimateRPS): Ultimate Rock, Paper,
                                                     Scissors game object.

        Returns:
            battle_table (list): Ultimate Rock, Paper, Scissors
                                 UltimateRPS.battle_table game object.
    """

    battle_table = ultimate_rps_object.battle_table

    return battle_table


def test_import_csv_type(battle_table):
    """ Test the Python object with the CSV data and assert the
        object type is a list.

        Args:
            battle_table (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    assert type(battle_table) == list


def test_import_csv_len(battle_table):
    """ Test the Python object with the CSV data and assert the
       list length is greater than zero.

        Args:
            battle_table (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    assert len(battle_table) > 0


def test_import_csv_sub_type(battle_table):
    """ Test the Python object with the CSV data and assert that the
        object type for a randomly-chosen list item is a dict.

        Args:
            csv_data (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    data_len = len(battle_table)
    rand_index = randint(0, data_len) - 1
    assert type(battle_table[rand_index]) == dict


@mark.parametrize(
    'player_play, computer_play, expected_result',
    list(GAMEPLAY_ARGS)
)
def test_play_result(
    ultimate_rps_object,
    player_play,
    computer_play,
    expected_result
):
    """ Test the result of a single game play (turn) to determine the
        result of the player's play vs the computer's play

        Args:
            ultimate_rps_object (class UltimateRPS): Ultimate Rock, Paper,
                                                     Scissors game object.
            player_play (str):
                Player's play choice (e.g. 'Rock').
            computer_play (str):
                Computer's play choice (e.g. 'Scissors').
            expected_result (str):
                Expected player result for the matchup against computer's
                play (e.g. 'Win').

        Returns:
            None.
    """

    # Call the 'get_turn_result' function with parameterized play arguments
    turn_result = ultimate_rps_object.get_turn_result(
            player_play=player_play,
            computer_play=computer_play
        )

    # Compare the result of the function call to the parameterized turn_result
    assert turn_result == expected_result
