#!/usr/bin/env pytest
''' pytest tests for name_that_tuple.py
'''

# Imports
from _24.name_that_tuple import TEST_DATA, tuple_tester
from collections import namedtuple
from pytest import mark
from unittest.mock import patch

# Constants
TEST_PERSON_INFO = namedtuple(
    typename='NamedTuple',
    field_names=TEST_DATA.keys()
)
TEST_EXPECTED_RESULT = TEST_PERSON_INFO(**TEST_DATA)
TEST_INVALID_ATTRIBUTE_NAMES_DATA = (
    '_first_name',
    '$1_las*t_nam)(e',
    '+_age',
    'hair color #',
    ''
)
TEST_INVALID_ATTRIBUTE_NAMES_RESULT = (
    'first_name',
    'last_name',
    'age',
    'haircolor',
    'index_4'
)


@mark.parametrize(
    argnames=[
        'iter_input',
        'att_names',
        'iter_return',
        'att_return'
    ],
    argvalues=[
        [
            TEST_DATA.values(),
            TEST_DATA.keys(),
            TEST_DATA.values(),
            TEST_DATA.keys()
        ],
        [
            TEST_DATA.values(),
            TEST_INVALID_ATTRIBUTE_NAMES_DATA,
            TEST_DATA.values(),
            TEST_INVALID_ATTRIBUTE_NAMES_RESULT
        ]
    ]
)
def test_named_tuple_converter(
    iter_input,
    att_names,
    iter_return,
    att_return
) -> None:
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
        iterable_input=iter_input,
        attribute_names=att_names
    )

    # Verify the result is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the test tuple input data equals the namedtuple attribute values
    assert tuple(iter_return) == tuple(test_result._asdict().values())

    # Verify the field names input data equals the namedtuple attribute names
    assert tuple(att_return) == test_result._fields


@patch(
    'builtins.input',
    side_effect=TEST_DATA.keys()
)
def test_named_tuple_converter_input(side_effects) -> None:
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
