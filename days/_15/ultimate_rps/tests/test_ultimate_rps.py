#!/usr/bin/env pytest
""" Test functions for Ultimate Rock, Paper, Scissors (Ultimate RPS).

    Usage:
        pytest ultimate_rps.py
"""

# Imports
from _15.ultimate_rps.ultimate_rps import import_csv
from pytest import fixture
from random import randint


@fixture
def csv_data():
    """ pytest fixture to read data from the CSV file with
        the 'battle-table.csv' matrix.

        Args:
            None.

        Returns:
            data (list): List of dictionaries with CSV file rows.
    """

    data = import_csv()

    return data


def test_import_csv_type(csv_data):
    """ Test the Python object with the CSV data and assert the
        object type is a list.

        Args:
            csv_data (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    assert type(csv_data) == list


def test_import_csv_len(csv_data):
    """ Test the Python object with the CSV data and assert the
       list length is greater than zero.

        Args:
            csv_data (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    assert len(csv_data) > 0


def test_import_csv_sub_type(csv_data):
    """ Test the Python object with the CSV data and assert that the
        object type for a randomly-chosen list item is a dict.

        Args:
            csv_data (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    data_len = len(csv_data)
    rand_index = randint(0, data_len) - 1
    assert type(csv_data[rand_index]) == dict
