#!/usr/bin/env python3
""" DB objects for the DT FL DB Application. """

# Imports - Python Standard Library
from collections import namedtuple

# namedtuple objects
DBData = namedtuple(
    typename='DBData',
    field_names=[
        'name',
        'outbound_interest_score',
        'inbound_interest_score',
        'num_tries',
        'fl_reason'
    ]
)
