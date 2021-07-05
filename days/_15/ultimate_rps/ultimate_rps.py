#!/usr/bin/env python3
""" Ultimate Rock, Paper, Scissors game (Ultimate RPS).

    Usage:
        python3 ultimate_rps.py
"""

# Imports
from csv import DictReader

# Constants
CSV_FILE = 'data/battle-table.csv'


def import_csv():
    """ Read data from the CSV file with the 'battle-table.csv' matrix.

        Args:
            None:

        Returns:
            data (list): List of dictionaries with CSV file rows.
    """
    with open(
        file=CSV_FILE,
        mode='rt',
        encoding='utf-8'
    ) as csv_data:
        csv_reader = DictReader(csv_data)
        data = list(csv_reader)

    return data


def main():
    """ Main program run.
    """
    import_csv()


if __name__ == '__main__':
    main()
