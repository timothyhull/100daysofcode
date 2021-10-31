#!/usr/bin/env python3
""" Weather research data """

# Imports - Python Standard Library
from collections import namedtuple
from typing import Dict, List, NamedTuple
import csv
import os

# Constants
CSV_FILE = 'seattle.csv'
CSV_FOLDER = 'data'
CSV_BASE_PATH = os.path.dirname(__file__)
CSV_FULL_PATH = os.path.join(CSV_BASE_PATH, CSV_FOLDER, CSV_FILE)


def init_csv_data(csv_file: str) -> List:
    """ Convert a CSV to a dictionary.

        Args:
            csv_file (str):
                Path to a CSV file.

        Returns:
            Record (namedtuple):
                namedtuple with CSV field names as attribute names.

            csv_data (List):
                CSV data as a list of dictionaries
    """

    # Open the CSV file
    with open(
         file=csv_file,
         mode='rt',
         encoding='utf-8') as file:

        # Use csv.DictReader to read CSV data
        reader = csv.DictReader(file)

        # Convert csv.DictReader field names to namedtuple with CSV field names
        Record = namedtuple('Record', reader.fieldnames)

        # Convert csv.DictReader data to a list of dictionaries
        csv_data = list(reader)

    return Record, csv_data


def parse_row(Record: NamedTuple, row: Dict) -> NamedTuple:
    """ Parse the data from CSV rows and convert data types.

        Args:
            Record (namedtuple):
                namedtuple with CSV field names as attribute names.

            row (Dict):
                Dictionary row from a CSV list of dictionaries.

        Returns:
            record (NamedTuple):
                NamedTuple row from a CSV list of dictionaries with
                data types converted from strings to operational data.
    """

    # Loop over 'row' dictionary values and change strings to floats
    for key, value in row.items():
        if key != 'date':
            row[key] = float(value)

    # Unpack dictionary values to their matching CSV field/attribute names
    record = Record(*row.values())

    return record


def init() -> List:
    """ Initialize weather data. """

    # Initialize CSV file
    Record, csv_data = init_csv_data(CSV_FULL_PATH)

    # Convert CSV string data to types that support operations (int, float)
    # Store converted data in a list, using a list comprehension
    data = [parse_row(Record, row) for row in csv_data]

    return data
