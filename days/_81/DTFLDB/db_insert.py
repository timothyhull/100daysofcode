#!/usr/bin/env python3
""" DB query functions for the DT FL DB Application. """

# Imports - Python Standard Library
from typing import List
import sqlite3

# Imports - Local
from _81.DTFLDB.db_data import DBData
from _81.DTFLDB.display_banner import display_banner
from _81.DTFLDB.get_new_record_input import get_new_record_input

# Constants
DB_EXTENSION = '.sqlite'
DB_NAME = f'dt_fail{DB_EXTENSION}'
DB_TABLE_NAME = 'history'


def add_db_entry(
    db_name: str,
) -> List[str]:
    """ Add DB row entries based on user input.

        Args:
            db_name (str):
                Name of the db file.  Automatically adds the ".db"
                extension, if not found.  Default value is the value of
                the DB_NAME constant.'

        Returns:
            db_entry (List):
                List object with raw DB entry data.
    """

    # Collect user input
    new_record_input = get_new_record_input()

    # If the response object is a list, insert the new record
    if new_record_input is not None:

        # Unpack the user input data
        new_record_input = DBData(*new_record_input)

        # Connect to a SQLite3 DB and add entries, if not already present
        with sqlite3.connect(
            database=DB_NAME
        ) as conn:

            # Create a cursor object
            cursor = conn.cursor()

            # Run the SQL command to add a DB entry
            db_entry = cursor.execute(
                f'''
                    INSERT INTO {DB_TABLE_NAME}
                    VALUES (
                        "{new_record_input.name}",
                        {new_record_input.outbound_interest_score},
                        {new_record_input.inbound_interest_score},
                        {new_record_input.num_tries},
                        "{new_record_input.fl_reason}"
                    );
                '''.strip()
            )

        # Display a success message.
        msg = display_banner(
            banner_string=(
                '** Successfully added the record '
                f'"{new_record_input.name}" **'
            )
        )
        print(msg)

    # If the response object is None, return an empty list
    else:
        db_entry = []

    return db_entry
