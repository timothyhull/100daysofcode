#!/usr/bin/env python3
''' Convert an iterable object into a named tuple using a decorator.
    Provide the namedtuple attribute names in a kwarg of the decorated
    function or enter attribute names at prompts.

    Usage:
        from name_that_tuple import named_tuple_converter

        @named_tuple_converter
        def your_function() -> Iterable:
            # your function code
'''

# Imports
from collections import namedtuple
from typing import Callable, Iterable
from functools import wraps
from re import compile, VERBOSE

# Constants
ATTRIBUTE_INPUT_START_CHARACTER = compile(
    r'''
    ^[^a-zA-Z]+   # Alphabet letter
    ''',
    VERBOSE
)
ATTRIBUTE_INPUT_INVALID_CHARACTERS = compile(
    r'''
    [^\w_-]       # Alphabet letter, integer, _, or -
    ''',
    VERBOSE
)
TEST_DATA = {
    'first_name': 'Tim',
    'last_name': 'Hull',
    'age': 41,
    'hair_color': 'blonde',
    'eye_color': 'blue'
}


def validate_attribute_input(
    attribute_names: list
) -> list:
    ''' Validate or generate attribute names for a namedtuple.

        Args:
            attribute_names (list):
                Raw list of namedtuple attribute names from user input.

        Returns:
            attribute_names (list):
                Refined list of namedtuple attribute names.
    '''

    # Loop over each attribute name
    for index, _ in enumerate(attribute_names):

        # Replace any invalid start characters
        attribute_names[index] = ATTRIBUTE_INPUT_START_CHARACTER.sub(
            repl='',
            string=attribute_names[index]
        )

        # Replace any invalid characters
        attribute_names[index] = ATTRIBUTE_INPUT_INVALID_CHARACTERS.sub(
            repl='',
            string=attribute_names[index]
        )

        # Create an attribute name for a blank string
        if attribute_names[index] == '':
            attribute_names[index] = f'index_{index}'

    return attribute_names


def named_tuple_converter(function: Callable) -> Callable:
    ''' Decorator function to convert an iterable into a namedtuple object.

        Args:
            function (Callable):
                Function to decorate.

        Returns:
            convert_to_namedtuple (Callable):
                Decorated function
    '''

    # Use @wraps to preserve the docstring of the function to decorate
    @wraps(function)
    def convert_to_namedtuple(*args, **kwargs) -> namedtuple:
        ''' Perform conversion of an iterable to a namedtuple.

            Args:
                kwargs:
                    iterable_input (Iterable):
                        Any iteraterable object class including, list, tuple,
                        dict_keys, dict_values, etc.
                    attribute_names (Iterable[str]):
                        Optional kwarg, aAny iteraterable object class
                        including, list, tuple, dict_keys, dict_values, etc.
                        with str values.

            Returns: named_tuple (namedtuple):
                Class NamedTuple instantiated from collections.namedtuple
        '''

        # Call the decorated function
        iterable_input = function(*args, **kwargs)

        # Convert the attribute_names argument value to a list object
        if kwargs.get('attribute_names') is not None:
            attribute_names = list(kwargs.get('attribute_names'))

        # Collect attribute names via input
        else:
            attribute_names = []
            for index, value in enumerate(iterable_input):

                # Get individual attribute names
                attribute_names.append(
                    input(
                        f'Enter an attribute name for the value "{value}": '
                    )
                )

        # Validate attribure names
        attribute_names = validate_attribute_input(
            attribute_names=attribute_names
        )

        # Check for an equal number of attribute names and input values
        if len(iterable_input) == len(attribute_names):
            # Define a namedtuple object
            NamedTuple = namedtuple(
                typename='NamedTuple',
                field_names=attribute_names
            )

            # Create a namedtuple from the attribute names and source iterable
            named_tuple = NamedTuple(
                *iterable_input
            )

        # Raise an exception for an unequal number of attributes and inputs
        else:
            raise ValueError(
                'Length of iterable_input and attribute_names must be equal:\n'
                f'iterable_input length = {len(iterable_input)}\n'
                f'attribute_names length = {len(attribute_names)}'
            )

        return named_tuple

    return convert_to_namedtuple


@named_tuple_converter
def tuple_tester(
    iterable_input: Iterable,
    attribute_names: Iterable[str] = None
) -> tuple:
    ''' Function to test the tuple_converter decorator function.

        Args:
            iterable_input (Iterable):
                Any iterable object to convert to a namedtuple.
            attribute_names (Iterable[str]):
                Any iterable object of strings to supply field names for
                a namedtuple.

        Returns:
            tuple_output (tuple):
                A tuple object of the iterable_input
    '''

    tuple_output = tuple(iterable_input)

    return tuple_output


def test_1() -> Callable:
    ''' Decorator test function #1
    '''

    return tuple_tester(
        iterable_input=tuple(TEST_DATA.values())
    )
