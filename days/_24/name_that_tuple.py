#!/usr/bin/env python3

# Imports
from collections import namedtuple
from collections.abc import Iterable
from functools import wraps

# Constants
TEST_DATA = {
    'first_name': 'Tim',
    'last_name': 'Hull',
    'age': 41,
    'hair_color': 'blonde',
    'eye_color': 'blue'
}


def tuple_converter(function):
    ''' Decorator function to convert an iterable into a namedtuple object.

        Args:
            function (function):
                Function to decorate.

        Returns:
            convert_to_namedtuple (function):
                Decorated function
    '''

    # Use @wraps to preserve the docstring of the function to decorate
    @wraps(function)
    def convert_to_namedtuple(*args, **kwargs):

        # Call the decorated function
        iterable_input = function(*args, **kwargs)

        # Convert the attribute_names argument value to a list object
        if kwargs.get('attribute_names') is not None:
            attribute_names = list(kwargs.get('attribute_names'))

        # Collect field names via input
        else:
            attribute_names = []
            for value in iterable_input:
                attribute_names.append(
                    input(f'Enter a field name for the value {value}: ')
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

        return named_tuple

    return convert_to_namedtuple


@tuple_converter
def tuple_tester(
    iterable_input: Iterable,
    attribute_names: Iterable[str] = None
):
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


def main():
    return tuple_tester(
        iterable_input=tuple(TEST_DATA.values())
    )


if __name__ == '__main__':
    print(main())
