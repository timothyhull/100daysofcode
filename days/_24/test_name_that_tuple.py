#!/usr/bin/env pytest
''' pytest tests for name_that_tuple.py

    Usage:
        pytest test_name_that_tuple.py name_that_tuple.py
'''

# Imports
from _24.name_that_tuple import TEST_DATA, tuple_tester, named_tuple_converter
from collections import namedtuple
from pytest import mark
from typing import Iterable
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
    '  4eye color !@'
)
TEST_AUTO_NAMED_ATTRIBUTED_DATA = (f'index_{i}' for i in range(5))


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
            TEST_DATA.keys()
        ]
    ]
)
def test_named_tuple_converter(
    iter_input,
    att_names,
    iter_return,
    att_return
) -> None:
    ''' Test of the named_tuple_converter decorator function to determine if
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
    ''' Test of the named_tuple_converter decorator function to determine if
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


@mark.parametrize(
    argnames=[
        'iter_input',
        'iter_return',
        'att_return'
    ],
    argvalues=[
        [
            TEST_DATA.values(),
            TEST_DATA.values(),
            TEST_AUTO_NAMED_ATTRIBUTED_DATA
        ]
    ]
)
def test_named_tuple_converter_custom_function_auto_name_attributes(
    iter_input,
    iter_return,
    att_return
) -> None:
    ''' Test of the named_tuple_converter decorator function using a custom
        function to determine if the function accepts a tuple argument
        and returns a namedtuple with the original tuple data, and if the
        decorator function automatically names the namedtuple attributes
        with the auto_attribute_names parameter set to True. Pass the
        namedtuple field names as an argument.

        Args:
            None.

        Returns:
            None.
    '''

    # Create a custom function decorated with named_tuple_converter
    @named_tuple_converter
    def custom_function(
        iterable_input: Iterable,
        auto_attribute_names: bool
    ) -> tuple:
        '''
        '''

        return tuple(iter_input)

    # Get a result to test
    test_result = custom_function(
        iterable_input=iter_input,
        auto_attribute_names=True
    )

    # Verify the result is of type NamedTuple
    assert 'NamedTuple' in str(test_result.__class__)

    # Verify the test tuple input data equals the namedtuple attribute values
    assert tuple(iter_return) == tuple(test_result._asdict().values())

    # Verify the field names input data equals the namedtuple attribute names
    assert tuple(att_return) == test_result._fields
