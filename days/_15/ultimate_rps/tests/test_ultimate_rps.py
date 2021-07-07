#!/usr/bin/env pytest
""" Test functions for Ultimate Rock, Paper, Scissors (Ultimate RPS).

    Usage:
        pytest ultimate_rps.py
"""

# Imports
from _15.ultimate_rps.UltimateRPS import UltimateRPS, Player
from collections import namedtuple
from pytest import fixture, mark
from random import randint

# Constants
PLAYER_1_NAME = 'Tim'
PLAYER_2_NAME = 'Computer'
PLAYER_1_PLAYS = [
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
PLAYER_2_PLAYS = [
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

# Combine lists to form a 3-tuple object, for parameterize compatibility
GAMEPLAY_ARGS = zip(
    PLAYER_1_PLAYS,
    PLAYER_2_PLAYS,
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


@fixture
def player_objects():
    """ pytest fixture to instantiate Player objects.

        Args:
            None.

        Returns:
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.
    """

    # Create namedtuple object to store test player object data
    PlayerObjects = namedtuple('PlayerObjects', 'player_1 player_2')

    # Instantiate Players object for player_1 and player_2
    player_objects = PlayerObjects(
        player_1=Player(name=PLAYER_1_NAME),
        player_2=Player()
    )

    return player_objects


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
    'player_1_play, player_2_play, expected_result',
    list(GAMEPLAY_ARGS)
)
def test_play_result(
    ultimate_rps_object,
    player_1_play,
    player_2_play,
    expected_result
):
    """ Test the result of a single game play (turn) to determine the
        result of the player_1 play vs the player_2 play

        Args:
            ultimate_rps_object (class UltimateRPS): Ultimate Rock, Paper,
                                                     Scissors game object.
            player_1_play (str):
                Player 1's play choice (e.g. 'Rock').
            player_2_play (str):
                Player 2's play choice (e.g. 'Scissors').
            expected_result (str):
                Expected player result for the matchup against Player 2's
                play (e.g. 'Win').

        Returns:
            None.
    """

    # Call the 'get_turn_result' function with parameterized play arguments
    turn_result = ultimate_rps_object.get_turn_result(
            player_1_play=player_1_play,
            player_2_play=player_2_play
        )

    # Compare the result of the function call to the parameterized turn_result
    assert turn_result == expected_result


def test_player_instantion(player_objects):
    """ Test the ability to instantiate Player objects.

        Args:
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returs:
            None.
    """

    assert type(player_objects.player_1) == Player
    assert player_objects.player_1.name == PLAYER_1_NAME
    assert type(player_objects.player_2) == Player
    assert player_objects.player_2.name == PLAYER_2_NAME


def test_instantiated_player_attributes(player_objects):
    """ Test for the correct Player objects attribute default values

        Args:
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returs:
            None.
    """

    assert player_objects.player_1.score == 0
    # assert type(player_objects.player_1.plays) == list
    assert player_objects.player_1.plays == []
    assert player_objects.player_1.record.wins == 0
    assert player_objects.player_1.record.losses == 0
