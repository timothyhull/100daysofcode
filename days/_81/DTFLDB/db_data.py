#!/usr/bin/env python3
""" DB objects for the DT FL DB Application. """

# Imports - Python Standard Library
from collections import namedtuple

# Shared Constants
BANNER_EXIT = 'Application closed'
DB_COLUMN_SQL = (
    '('
    'name TEXT, '
    'outbound_interest_score INT, '
    'inbound_interest_score INT, '
    'num_tries INT ,'
    'fl_reason TEXT'
    ')'
)
DB_EXTENSION = '.sqlite'
DB_NAME = f'dt_fail{DB_EXTENSION}'
DB_TABLE_NAME = 'history'


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
