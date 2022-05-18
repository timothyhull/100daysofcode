#!/usr/bin/env python3

""" openpyxl automation script for day 70 of 100DaysOfCode. """

# Imports - Python Standard Library
from os import path
from pathlib import Path

# Imports - Third-Party
from openpyxl import load_workbook

# Imports - Local

# Constants
FILE_NAME = path.abspath(__file__)
LOCAL_DIR = Path(FILE_NAME).parent
DATA_FILE = 'data/Financial_Sample.xlsx'
DATA_FILE_PATH = path.join(LOCAL_DIR, DATA_FILE)


# Read the spreadsheet data
def import_workbook() -> None:
    """ Import Excel workbook.

        Args:
            None.

        Returns:
            None.
    """

    # Load the workbook file
    workbook = load_workbook(
        filename=DATA_FILE_PATH
    )

    # Display worksheet names
    print('\nWorksheet Names:')
    for index, worksheet in enumerate(workbook.sheetnames, 1):
        print(f'{index}. {worksheet}')

    return workbook


def main() -> None:
    """ Main program. """

    import_workbook()

    return None


if __name__ == '__main__':
    main()
