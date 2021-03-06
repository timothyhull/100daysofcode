#!/usr/bin/env python3
""" Use list comprehensions and generator functions

    Usage:
        python3 name_pairs.py
"""

# Imports
from copy import copy
from random import choice
from types import GeneratorType

# Constants
NAMES = [
    'arnold schwarzenegger', 'alec baldwin', 'lord garmadon',
    'julian sequeira', 'sandra bullock', 'keanu reeves',
    'julbob pybites', 'bob belderbos', 'forky spork',
    'al pacino', 'brad pitt', 'matt damon', 'dead pool'
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
                Generator of title cased names
    """

    # Loop through the names list and yield one name
    for name in names:
        yield name.title()


def random_name_pairs(names: list = NAMES) -> GeneratorType:
    """ Converts a list of first and last names to a generator that
        pairs two first names randomly.

        Args:
            names (list):
                A list of names.

        Returns:
            name_pair (GeneratorType).
                Generator of random name pairings
    """

    # Create a copy of names, to avoid impacting the global NAMES
    names = copy(names)
    while len(names) > 1:
        name_1 = choice(names)
        names.remove(name_1)

        name_2 = choice(names)
        names.remove(name_2)

        print(f'{name_1.split()[0]} is paired with {name_2.split()[0]}')

        # yield the first name from name_1, name_2
        yield name_1.split()[0], name_2.split()[0]


def main():
    pass


if __name__ == '__main__':
    main()
