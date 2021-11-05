#!/usr/bin/env pytest
""" Tests for bad_drivers.py application. """

# Imports - Python Standard Library
from random import randint

# Imports - Third-Party
from pytest import fixture

# Imports - Local
from _38.driver_csv_demo.app.bad_drivers import BadDrivers, DataSet, ResultSet

# Constants


@fixture
def bad_drivers() -> BadDrivers:
    """ pytest fixture to return a BadDrivers class instance. """

    # Instantiate an object from the BadDrivers class
    return BadDrivers()


def test_bad_drivers_init(bad_drivers) -> None:
    """ Test the BadDrivers __init__ method.

        The __init__ method should import CSV data from a default
        file, and return a list of dictionaries.

        Args:
            bad_drivers (pytest fixture):
                Instance of the BadDrivers class.

        Returns:
            None.
    """

    # Assert that bad_drivers contains a "csv_data" attribute
    assert bad_drivers.csv_data

    # Assert that bad_drivers.csv_data is a list object
    assert type(bad_drivers.csv_data) == list

    # Assert that bad_drivers.csv_data is not empty
    assert len(bad_drivers.csv_data) > 0

    return None


def test_bad_drivers_data_conversion(bad_drivers) -> None:
    """ Test the BadDrivers _data_conversion method.

        The data_conversion method should convert numeric string values
        to float objects, and produce a list of NamedTuple objects.

        Args:
            bad_drivers (pytest fixture):
                Instance of the BadDrivers class.

        Returns:
            None.
    """

    # Assert that bad_drivers contains a "data" attribute
    assert bad_drivers.data

    # Assert that bad_drivers.csv_data is a list object
    assert type(bad_drivers.data) == list

    # Assert that bad_drivers.data is not empty
    assert len(bad_drivers.data) > 0

    # Assert that bad_drivers.csv_data is a list of namedtuples
    assert type(bad_drivers.data[0]) == DataSet

    return None


def test_top_n_driver_fatal_states_no_alc(bad_drivers) -> None:
    """ Test the BadDrivers top_n_driver_fatal_states_no_alc method.

        The method should return the top N states for driver fatalities
        without alcohol involved.

        Args:
            bad_drivers (pytest fixture):
                Instance of the BadDrivers class.

        Returns:
            None.
    """

    # Choose a random number <= to the length of bad_drivers.data
    count = randint(1, len(bad_drivers.data))

    # Assign method results to a variable with a randomized count
    results = bad_drivers.top_n_driver_fatal_states_no_alc(count)

    # Assert that results returns a value
    assert results

    # Assert that results is a list object
    assert type(results) == list

    # Assert that results is not empty
    assert len(results) > 0

    # Assert the number of items in the result list matches the random count
    assert len(results) == count

    # Assert that items in the results list are ResultSet objects
    assert type(results[0]) == ResultSet

    return None


def test_top_n_driver_fatal_states_with_alc(bad_drivers) -> None:
    """ Test the BadDrivers top_n_driver_fatal_states_with_alc method.

        The method should return the top N states for driver fatalities
        with alcohol involved.

        Args:
            bad_drivers (pytest fixture):
                Instance of the BadDrivers class.

        Returns:
            None.
    """

    # Choose a random number <= to the length of bad_drivers.data
    count = randint(1, len(bad_drivers.data))

    # Assign method results to a variable with a randomized count
    results = bad_drivers.top_n_driver_fatal_states_with_alc(count)

    # Assert that results returns a value
    assert results

    # Assert that results is a list object
    assert type(results) == list

    # Assert that results is not empty
    assert len(results) > 0

    # Assert the number of items in the result list matches the random count
    assert len(results) == count

    # Assert that items in the results list are ResultSet objects
    assert type(results[0]) == ResultSet

    return None


def test_top_n_car_insurance_premium_states(bad_drivers) -> None:
    """ Test the BadDrivers top_n_car_insurance_premium_states method.

        The method should return the top N states for driver fatalities
        without alcohol involved.

        Args:
            bad_drivers (pytest fixture):
                Instance of the BadDrivers class.

        Returns:
            None.
    """

    # Choose a random number <= to the length of bad_drivers.data
    count = randint(1, len(bad_drivers.data))

    # Assign method results to a variable with a randomized count
    results = bad_drivers.top_n_car_insurance_premium_states(count)

    # Assert that results returns a value
    assert results

    # Assert that results is a list object
    assert type(results) == list

    # Assert that results is not empty
    assert len(results) > 0

    # Assert the number of items in the result list matches the random count
    assert len(results) == count

    # Assert that items in the results list are ResultSet objects
    assert type(results[0]) == ResultSet

    return None
