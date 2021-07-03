#!/usr/bin/env pytest

# Imports
from _15.ultimate_rps.ultimate_rps import import_csv
from csv import reader

# Constants
csv_file = '../data/battle-table.csv'


def test_import_csv():
    assert import_csv() is not None
