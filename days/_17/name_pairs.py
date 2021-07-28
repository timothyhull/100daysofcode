#!/usr/bin/env python3
""" Use list comprehensions and generator functions

    Usage:
        python3 name_pairs.py
"""

# Imports
from types import GeneratorType

# Constants
NAMES = [
    'arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
    'julian sequeira', 'sandra bullock', 'keanu reeves',
    'julbob pybites', 'bob belderbos', 'julian sequeira',
    'al pacino', 'brad pitt', 'matt damon', 'brad pitt'
]


def title_case_names(names: list = NAMES) -> list:
    """ Converts a list of names to title case using a list comprehension.

        Args:
            names (list):
                A list of names.

        Returns:
            titled_names (list).
                List of title cased names
    """

    titled_names = [name.title() for name in names]

    return titled_names


def switch_name_order(names: list = NAMES) -> list:
    """ Converts a list of names to a list of first and last names in
        reversed order, using a list comprehension.

        Args:
            names (list):
                A list of names.

        Returns:
            reversed_names (list).
                List of reversed order names.
    """

    reversed_names = [f'{name.split()[1]} {name.split()[0]}' for name in names]

    return reversed_names


def title_case_names_gen(names: list = NAMES) -> GeneratorType:
    """ Converts a list of names to title case using a list comprehension.
        Uses a generator instead of building a list.

        Args:
            names (list):
                A list of names.

        Returns:
            titled_names (GeneratorType).
                Generator of of title cased names
    """

    # Loop through the names list and yield one name
    for name in names:
        yield name.title()


def main():
    pass


if __name__ == '__main__':
    main()
