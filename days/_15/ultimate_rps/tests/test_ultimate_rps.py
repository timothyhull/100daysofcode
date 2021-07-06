#!/usr/bin/env pytest
""" Test functions for Ultimate Rock, Paper, Scissors (Ultimate RPS).

    Usage:
        pytest ultimate_rps.py
"""

# Imports
from _15.ultimate_rps.UltimateRPS import UltimateRPS
from pytest import fixture
from random import randint


@fixture
def battle_table():
    """ pytest fixture to read data from the CSV file with
        the 'battle-table.csv' matrix.

        Args:
            None.

        Returns:
            battle_table (list): Ultimate Rock, Paper, Scissors
                                 game object.
    """

    ultimate_rps = UltimateRPS()
    battle_table = ultimate_rps.battle_table

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


def test_play_result():
    ultimate_rps = UltimateRPS()
    player_play = 'Scissors'
    computer_play = 'Rock'

    turn_result = ultimate_rps.get_turn_result(
            player_play=player_play,
            computer_play=computer_play
        )
    assert turn_result == 'win'
