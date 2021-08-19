#!/usr/bin/env pytest
''' pytest tests for name_that_tuple.py
'''

# Imports
from _24.name_that_tuple import tuple_tester
from collections import namedtuple

# Constants
TEST_DATA = {
    'first_name': 'Tim',
    'last_name': 'Hull',
    'age': 41,
    'hair_color': 'blonde',
    'eye_color': 'blue'
}
TEST_PERSON_INFO = namedtuple(
    typename='PersonInfo',
    field_names=tuple(TEST_DATA.keys())
)
TEST_EXPECTED_RESULT = TEST_PERSON_INFO(**TEST_DATA)


def test_tuple_converter() -> None:
    ''' Test of the tuple_namer decorator function to determine if
        the function accepts a tuple argument and returns a namedtuple
        with the original tuple data.

        Args:
            None.

        Returns:
            None.
    '''

    # Get a result to test
    test_result = tuple_tester(
        tuple_input=tuple(TEST_DATA.values())
    )

    # Verify the result is of type namedtuple
    assert type(test_result) == namedtuple

    # Verify the tuple data is present in the namedtuple
    assert tuple(TEST_DATA.values()) == tuple(test_result)
