#!/usr/bin/env pytest

# Imports
from _15.ultimate_rps.ultimate_rps import CSV_FILE, import_csv
from csv import reader

# Constants
CSV_FILE = '../data/battle-table.csv'


def test_import_csv():
    assert import_csv() is not None
