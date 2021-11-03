#!/usr/bin/env pytest
""" Tests for bad_drivers.py application. """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from _38.driver_csv_demo.app.bad_drivers import BadDrivers

# Constants


def test_bad_drivers_init() -> None:
    """ Test the BadDrivers __init__ method.

        The __init__ method should import CSV data from a default file.

        Args:
            None.

        Returns:
            None.
    """

    # Instantiate an object from the BadDrivers class
    bad_drivers = BadDrivers()

    # Assert that bad_drivers contains a "data" attribute
    assert bad_drivers.data
