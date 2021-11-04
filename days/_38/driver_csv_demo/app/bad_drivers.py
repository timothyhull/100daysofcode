#!/usr/bin/env python3
""" Bad Driver application. """

# Imports - Python Standard Library
from collections import namedtuple
from csv import DictReader
from os import path
from pathlib import Path
from sys import stderr, exit
from typing import List

# Imports - Third-Party

# Imports - Local

# Constants
CSV_BASE_DIR = Path(path.dirname(__file__))
CSV_ABSOLUTE_DIR = CSV_BASE_DIR.parent.absolute()
CSV_DATA_DIR = 'data'
CSV_FILE_NAME = 'bad-drivers.csv'
CSV_FULL_PATH = path.join(CSV_ABSOLUTE_DIR, CSV_DATA_DIR, CSV_FILE_NAME)

# Create a namedtuple object for a CSV data set
DataSet = namedtuple(
    typename='DataSet',
    field_names=[
        'state',
        'num_drivers_in_fatal_collisions_per_bn_miles',
        'percent_of_drivers_in_fatal_collisions_while_speeding',
        'percent_of_drivers_in_fatal_collisions_while_alcohol_impaired',
        'percent_of_drivers_in_fatal_collisions_not_distracted',
        'percent_of_drivers_in_fatal_collisions_no_previous_accidents',
        'car_insurance_premiums',
        'losses_by_insurance_companies_for_collisions_per_insured_driver'
    ]
)

# Create a namedtuple object for a data result set
ResultSet = namedtuple(
    typename='ResultSet',
    field_names=[
        'state',
        'value'
    ]
)


def handle_exception(error: Exception):
    """ Gracefully handle exceptions and exit.

        Args:
            error (Exception):
                Named Exception object from 'except' keyword
                assignment.

        Returns:
            N/A

        Usage:
            try:
                # Code to try
            except Exception as error:
                handle_exception(error)
    """

    # Use shorthand for the repr function to write the error to STDERR
    print(
        '\nAn error occurred:'
        f'{error!r}',
        file=stderr
    )

    # Exit the application
    exit()


class BadDrivers:
    """ BadDrivers class """

    def __init__(self) -> None:
        """ BadDrivers __init__ method.

            Open the CSV data file and read the file with the
            csv.DictReader method.  Store the resulting object as a
            list of dictionaries.

            Args:
                self.

            Returns:
                None.
        """

        # Open the CSV file
        try:
            with open(
                file=CSV_FULL_PATH,
                mode='rt',
                encoding='utf-8'
            ) as file:

                # Read the file with the csv.DictReader method
                csv_data = DictReader(file)

                # Convert the csv_data to a list and store as an attribute
                self.csv_data = list(csv_data)

        except FileNotFoundError as error:
            # Display the error message and exit
            handle_exception(error)

        # Convert the CSV data to a more consumable format
        self._data_conversion()

        return None

    def _data_conversion(self):
        """ Convert self.csv_data to a more consumable format.

            Convert the numeric contents in the self.csv_data object
            to float objects, and create a list of NamedTuple objects.

            Args:
                self.

            Returns:
                None.
        """

        # Convert numeric string values in csv_data to float objects
        for record in self.csv_data:
            for key, value in record.items():
                try:
                    record[key] = float(value)
                except ValueError:
                    record[key] = str(value)

        # # Create a list of namedtuple objects with the CSV data
        self.data = []
        for record in self.csv_data:
            self.data.append(
                DataSet(
                    *record.values()
                )
            )

        return None

    def _create_result_set(
        self,
        attribute_field: str
    ) -> List:
        """ Creates a result set based on a specific value field.

            Args:
                self.

                attribute_field (str):
                    Attribute to create a result set from, defined by
                    the DataSet namedtuple

            Returns:
                result_set (List):
                    List of results.
        """

        # Create an empty list object
        result_set = []

        # Add a namedtuple of state and relevant value to the result_set list
        for row in self.data:
            result_set.append(
                ResultSet(
                    state=row.state,
                    value=getattr(row, attribute_field)
                )
            )

        # Sort the result_set list by the value in the ResultSet namedtuple
        result_set.sort(
            key=lambda x: x.value,
            reverse=True
        )

        return result_set

    def top_n_driver_fatal_states_no_alc(
        self,
        count: int = 5
    ) -> List:
        """ Top N states for driver fatalities, no alcohol involved.

            Args:
                self.

                count (int):
                    Number of records to return (N), default of 5.

            Returns:
                result_set (List):
                    List slice equal to the count parameter of sorted
                    results.
        """

        attribute_field = 'num_drivers_in_fatal_collisions_per_bn_miles'

        result_set = self._create_result_set(attribute_field)

        # Return a slice of the result_set list equal to the count (N)
        return result_set[:count]

    def top_n_driver_fatal_states_with_alc(
        self,
        count: int = 5
    ) -> List:
        """ Top N states for driver fatalities, with alcohol involved.

            Args:
                self.

                count (int):
                    Number of records to return (N), default of 5.

            Returns:
                result_set (List):
                    List slice equal to the count parameter of sorted
                    results.
        """

        attribute_field = (
            'percent_of_drivers_in_fatal_collisions_while_alcohol_impaired'
        )

        result_set = self._create_result_set(attribute_field)

        # Return a slice of the result_set list equal to the count (N)
        return result_set[:count]

    def top_n_car_insurance_premium_states(
        self,
        count: int = 5
    ) -> List:
        """ Top N states for highest car insurance premiums.

            Args:
                self.

                count (int):
                    Number of records to return (N), default of 5.

            Returns:
                result_set (List):
                    List slice equal to the count parameter of sorted
                    results.
        """

        attribute_field = 'car_insurance_premiums'

        result_set = self._create_result_set(attribute_field)

        # Return a slice of the result_set list equal to the count (N)
        return result_set[:count]
