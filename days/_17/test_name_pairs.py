#!/usr/bin/env pytest
""" Tests for name_pairs.py

    Usage:
        pytest test_name_pairs.py
"""

# Imports
from name_pairs import *

# Constants


# Test for a list of names:
def test_name_pairs() -> None:
    """ Test for a list of imported names.

        Args:
            None.

        Returns:
            None.
    """

    # Confirm the NAMES variable is a list
    assert type(NAMES) == list

    # Confirm the list is not blank
    assert NAMES


def test_title_case_names() -> None:
    """ Test for a a list of title case names.

        Args:
            None.

        Returns:
            None.
    """

    # Call the function to get a return object
    titled_names = title_case_names(NAMES)

    # Create a list of names from titled_names that are not in title case
    wrong_case_names = [name for name in titled_names if not name.istitle()]

    # Assert that the list is empty
    assert not wrong_case_names


def test_switch_name_order() -> None:
    """ Test for a a list of names for a switched order of names
        where last name is before first name.

        Args:
            None.

        Returns:
            None.
    """

    # Call the function to get a return object
    reversed_names = switch_name_order(NAMES)

    # Check for names in reversed_names that are not reversed
    for index, name in enumerate(reversed_names):
        """ Convert each item in the wrong_order_names list from a string to a
            list of strings, using the default ' ' separator.

            Get the value for the 0 index of the current name and compare it to
            the 1 index of the NAMES list; the two should match, if the name
            order is reversed.
        """

        wrong_order_names_count = 0
        if name.split()[0] != NAMES[index].split()[1]:
            wrong_order_names_count += 1

    # Assert that wrong_order_names_count is 0
    assert wrong_order_names_count == 0


def test_title_case_names_gen() -> None:
    """ Test for a a list of title case names, produced by a generator.

        Args:
            None.

        Returns:
            None.
    """

    # Call the function to get a return object
    titled_names = title_case_names_gen(NAMES)

    # Assert that titled_names is a generator
    assert type(titled_names) == GeneratorType

    # Create a list of names from titled_names that are not in title case. from the generator
    wrong_case_names = [name for name in list(titled_names) if not name.istitle()]

    # Assert that the list is empty
    assert not wrong_case_names
