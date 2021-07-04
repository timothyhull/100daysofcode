#!/usr/bin/env python3

# Imports
from csv import reader

# Constants
CSV_FILE = 'data/battle-table.csv'


def import_csv():
    with open(
        file=CSV_FILE,
        mode='rt',
        encoding='utf-8'
    ) as csv_data:
        data = reader(csv_data)

    return(data)


def main():
    game_data = import_csv()


if __name__ == '__main__':
    main()