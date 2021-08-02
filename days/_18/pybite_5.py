#!/usr/bin/env python3

# Imports
from pprint import pprint

# Constants
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names: list = NAMES) -> list:
    """Should return a list of title cased names,
       each name appears only once"""

    # Convert the list to a set (to remove duplicates) convert to title case
    names = {name.title() for name in names}

    # Convert the set to a list
    return list(names)


def sort_by_surname_desc(names: list = NAMES) -> list:
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)

    """ Use a lambda function that as a sort key:
            Convert every iteration (first_name last_name) to a list.
            Use the [1] list index to specify the last name as the sort key.
    """
    names.sort(
        key=lambda x: x.split()[1],
        reverse=True
    )

    return names


def shortest_first_name(names: list = NAMES) -> str:
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)

    # Remove all of the last names
    names = [name.split()[0] for name in names]

    # ## Original solution ## #
    # # Sort first names by length
    # names.sort(
    #     key=lambda x: len(x)
    # )

    # # Return the first index, which is the shortest name
    # return(names[0])

    # ## Updated solution ## #
    # Choose the name with the shortest length
    name = min(names, key=len)

    return name


def main():
    print('\nResult #1, remove duplicates and switch to title case:')
    pprint(dedup_and_title_case_names())

    print('\nResult #2, reverse sort list by last name:')
    pprint(sort_by_surname_desc())

    print('\nResult #3, shortest first name in the list:')
    print(shortest_first_name())


if __name__ == '__main__':
    main()
