#!/usr/bin/env python3
""" Bad Driver application. """

# Imports - Python Standard Library
from csv import DictReader
from os import path
from pathlib import Path

# Imports - Third-Party

# Imports - Local

# Constants
CSV_BASE_DIR = Path(path.dirname(__file__))
CSV_ABSOLUTE_DIR = CSV_BASE_DIR.parent.absolute()
CSV_DATA_DIR = 'data'
CSV_FILE_NAME = 'bad-drivers.csv'
CSV_FULL_PATH = path.join(CSV_ABSOLUTE_DIR, CSV_DATA_DIR, CSV_FILE_NAME)


class BadDrivers:
    """ BadDrivers class """

    def __init__(self) -> None:
        """ BadDrivers __init__ method.

            Args:
                None.

            Returns:
                None.
        """

        # Open the CSV file
        with open(
            file=CSV_FULL_PATH,
            mode='rt',
            encoding='utf-8'
        ) as file:

            # Read the file with the csv.DictReader method
            csv_data = DictReader(file)

            # Convert the csv_data to a list and store as an attribute
            self.data = list(csv_data)
