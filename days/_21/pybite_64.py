#!/usr/bin/env python3
""" Fix the output of a zip() operation on the combination of 'names',
    'locations', and 'confirmed' such that no names are truncated, instead
    replacing incomplete locations and confirmations with a - character
"""

# Imports
from itertools import zip_longest

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in zip_longest(
        names,
        locations,
        confirmed,
        fillvalue='-'
    ):
        print(participant)


if __name__ == '__main__':
    get_attendees()
