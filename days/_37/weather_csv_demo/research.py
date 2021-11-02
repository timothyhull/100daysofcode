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

# Set the full CSV file path
if os.getenv('CSV_FULL_PATH') is not None:
    CSV_FULL_PATH = os.getenv('CSV_FULL_PATH')
else:
    CSV_FULL_PATH = os.path.join(CSV_BASE_PATH, CSV_FOLDER, CSV_FILE)


def init_csv_data(
    csv_file: str
):
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


def parse_row(
    Record: NamedTuple,
    row: Dict
) -> NamedTuple:
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


def sort_records(
    weather_data: List,
    sort_field: str
) -> List:
    """ Sort weather records based on a specific sort field.

        Args:
            weather_data (List):
                List of namedtuples with weather data converted from
                data in a CSV file.

            sort_field (str):
                Field name from a CSV file to sort records by.

        Returns:
            sorted_data (List):
                Sorted List of namedtuples with weather data converted
                from data in a CSV file.
    """

    # Created a list of sorted data using a lambda function keyed on sort_field
    sorted_data = sorted(
        weather_data,
        key=lambda x: getattr(x, sort_field),
        reverse=True
    )

    return sorted_data


def create_result_set(
    sorted_data: List,
    sort_field: str
) -> List:
    """ Create a namedtuple result set of top N days from sorted data.

        Args:
            sorted_data (List):
                Sorted List of namedtuples with weather data converted
                from data in a CSV file.

            sort_field (str):
                Field name from a CSV that records are sorted by.

        Returns:
            top_n_days (List):
                Sorted List of top N namedtuples containing only
                attributes for the date and the sorted field.
    """

    # Create a hot_days namedtuple object
    ResultSet = namedtuple(
        typename='ResultSet',
        field_names=['date', sort_field]
    )

    # Create a blank list slice for the top N days
    top_n_days = []

    # Loop over the top N sorted records, using a list slice
    for record in sorted_data:
        # Append a namedtuple item to hot_days for each top N record
        top_n_days.append(
            ResultSet(
                record.date,
                getattr(record, sort_field))
        )

    return top_n_days


def hot_days(
    weather_data: List,
    result_count: int = 10
) -> NamedTuple:
    """ Return the top N hottest days.

        Args:
            weather_data (List):
                List of namedtuples with weather data converted from
                data in a CSV file.

            result_count (int, optional):
                Number of results to return, default value is 10.

        Returns:
            result_set (NamedTuple):
                NamedTuple with 'date' and 'actual_max_temp' named
                attributes.
    """

    # Create a sort field for the function
    sort_field = 'actual_max_temp'

    # Sort the list of days, hottest to coldest
    sorted_data = sort_records(
        weather_data=weather_data,
        sort_field=sort_field
    )

    # Slice the top N results from the sorted data list
    sorted_data = sorted_data[:result_count]

    # Add the top N results to the attribute limited namedtuple result set
    result_set = create_result_set(
        sorted_data=sorted_data,
        sort_field=sort_field
    )

    return result_set


def cold_days(
    weather_data: List,
    result_count: int = 10
) -> NamedTuple:
    """ Return the top N coldest days.

        Args:
            weather_data (List):
                List of namedtuples with weather data converted from
                data in a CSV file.

            result_count (int, optional):
                Number of results to return, default value is 10.

        Returns:
            result_set (NamedTuple):
                NamedTuple with 'date' and 'actual_min_temp' named
                attributes.
    """

    # Create a sort field for the function
    sort_field = 'actual_min_temp'

    # Sort the list of days, hottest to coldest
    sorted_data = sort_records(
        weather_data=weather_data,
        sort_field=sort_field
    )

    # Slice the top N results from the sorted data list
    sorted_data = sorted_data[:result_count]

    # Add the top N results to the attribute limited namedtuple result set
    result_set = create_result_set(
        sorted_data=sorted_data,
        sort_field=sort_field
    )

    return result_set


def wet_days(
    weather_data: List,
    result_count: int = 10
) -> NamedTuple:
    """ Return the top N wettest days.

        Args:
            weather_data (List):
                List of namedtuples with weather data converted from
                data in a CSV file.

            result_count (int, optional):
                Number of results to return, default value is 10.

        Returns:
            result_set (NamedTuple):
                NamedTuple with 'date' and 'actual_precipitation' named
                attributes.
    """

    # Create a sort field for the function
    sort_field = 'actual_precipitation'

    # Sort the list of days, hottest to coldest
    sorted_data = sort_records(
        weather_data=weather_data,
        sort_field=sort_field
    )

    # Slice the top N results from the sorted data list
    sorted_data = sorted_data[:result_count]

    # Add the top N results to the attribute limited namedtuple result set
    result_set = create_result_set(
        sorted_data=sorted_data,
        sort_field=sort_field
    )

    return result_set
