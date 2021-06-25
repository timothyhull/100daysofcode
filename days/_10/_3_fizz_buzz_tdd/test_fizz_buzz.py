#!/usr/bin/env pytest
"""Tests for fizz_buzz.py
"""

# Imports
import pytest
from fizz_buzz import fizz_buzz


# Test a set of arguments and return values with @pytest.mark.parametrize
@pytest.mark.parametrize(
    'arg_value, return_value',
    [
        (1, '1'),
        (2, '2'),
        (3, 'Fizz'),
        (4, '4'),
        (5, 'Buzz'),
        (6, 'Fizz'),
        (7, '7'),
        (8, '8'),
        (9, 'Fizz'),
        (10, 'Buzz'),
        (11, '11'),
        (12, 'Fizz'),
        (13, '13'),
        (14, '14'),
        (15, 'Fizz Buzz'),
        (16, '16')
    ]
)
def test_fizz_buzz(arg_value, return_value):
    assert fizz_buzz(arg_value) == return_value


# Test a set of values which should produce ValueErrors
def test_fizz_buzz_value_errors():
    with pytest.raises(ValueError):
        # Send a non-integer or value which can be converted to an integer
        fizz_buzz('a')
    with pytest.raises(TypeError):
        '''Send a list object, instead of an integer or value which can be
           converted to an integer
        '''
        fizz_buzz(list())
