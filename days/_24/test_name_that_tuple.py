#!/usr/bin/env pytest
''' pytest tests for name_that_tuple.py
'''

# Imports
from _24.name_that_tuple import TEST_DATA, tuple_tester
from collections import namedtuple
from unittest.mock import patch

# Constants
TEST_PERSON_INFO = namedtuple(
    typename='NamedTuple',
    field_names=TEST_DATA.keys()
)
TEST_EXPECTED_RESULT = TEST_PERSON_INFO(**TEST_DATA)


def test_tuple_converter() -> None:
    ''' Test of the tuple_namer decorator function to determine if
        the function accepts a tuple argument and returns a namedtuple
        with the original tuple data. Pass the namedtuple field names
        as an argument.

        Args:
            None.

        Returns:
            None.
    '''

    # Get a result to test
    test_result = tuple_tester(
        iterable_input=TEST_DATA.values(),
        attribute_names=TEST_DATA.keys()
    )

    # Verify the result is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the test tuple input data equals the namedtuple attribute values
    assert tuple(TEST_DATA.values()) == tuple(test_result._asdict().values())

    # Verify the field names input data equals the namedtuple attribute names
    assert tuple(TEST_DATA.keys()) == test_result._fields


@patch(
    'builtins.input',
    side_effect=TEST_DATA.keys()
)
def test_tuple_converter_input(side_effects) -> None:
    ''' Test of the tuple_namer decorator function to determine if
        the function accepts a tuple argument and returns a namedtuple
        with the original tuple data. Collect the field names with the
        input() function.

        Args:
            None.

        Returns:
            None.
    '''

    # Get a result to test
    test_result = tuple_tester(
        iterable_input=TEST_DATA.values(),
    )

    # Verify the result is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the test tuple input data equals the namedtuple attribute values
    assert tuple(TEST_DATA.values()) == tuple(test_result._asdict().values())

    # Verify the field names input data equals the namedtuple attribute names
    assert tuple(TEST_DATA.keys()) == test_result._fields
