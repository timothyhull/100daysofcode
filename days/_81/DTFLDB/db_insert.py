#!/usr/bin/env python3
""" DB insert/updates functions for the DT FL DB Application. """

# Imports - Python Standard Library
from typing import List
import sqlite3

# Imports - Local
from _81.DTFLDB.db_data import (
    DB_NAME, DB_TABLE_NAME, DBData
)
from _81.DTFLDB.display_banner import display_banner
from _81.DTFLDB.get_new_record_input import get_new_record_input


def add_db_record(
    db_name: str = DB_NAME
) -> List[str]:
    """ Add DB row records based on user input.

        Args:
            db_name (str, optional):
                Name of the DB file.  Default value is the value of
                the DB_NAME constant.'

        Returns:
            db_record (List):
                List object with raw DB record data.
    """

    # Collect user input
    new_record_input = get_new_record_input()

    # If the response object is a list, insert the new record
    if new_record_input is not None:

        # Prepend the user input data with the DB record ID
        new_record_input.insert(0, None)

        # Unpack the user input data
        new_record_input = DBData(*new_record_input)

        # Connect to a SQLite3 DB and add records, if not already present
        with sqlite3.connect(
            database=DB_NAME
        ) as conn:

            # Create a cursor object
            cursor = conn.cursor()

            # Run the SQL command to add a DB record
            db_record = cursor.execute(
                f'''
                    INSERT INTO {DB_TABLE_NAME}
                    VALUES (
                        NULL,
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
        db_record = []

    return db_record


def update_db_record(
    db_name: str = DB_NAME,
    db_record: DBData = None
) -> List[str]:
    """ Update DB row records based on user input.

        Args:
            db_name (str, optional):
                Name of the DB file.  Default value is the value of
                the DB_NAME constant.'

            db_record (DBData):
                DBData object with the DB record data for the record
                to update.

        Returns:
            db_record (List):
                List object with raw DB record data.
    """

    # Collect user input
    new_record = get_new_record_input()

    # If the response object is a list, insert the new record
    if new_record is not None:

        # Prepend the user input data with the DB record ID
        new_record.insert(0, db_record.id)

        # Unpack the user input data
        new_record = DBData(*new_record)

        # Build the SQL command to update the DB record
        db_record = f'''
            UPDATE {DB_TABLE_NAME}
            SET id = {db_record.id},
                name = "{new_record.name}",
                outbound_interest_score = {new_record.outbound_interest_score},
                inbound_interest_score = {new_record.inbound_interest_score},
                num_tries = {new_record.num_tries},
                fl_reason = "{new_record.fl_reason}"
            WHERE id = "{db_record.id}";
        '''.strip()

        # Connect to a SQLite3 DB and update the record, if it exists
        with sqlite3.connect(
            database=DB_NAME
        ) as conn:

            # Create a cursor object
            cursor = conn.cursor()

            # Run the SQL command to update the DB record
            db_record = cursor.execute(db_record)

        # Display a success message.
        msg = display_banner(
            banner_string=(
                '** Successfully updated the record '
                f'"{new_record.name}" **'
            )
        )
        print(msg)

    # If the old record is None, return an empty list
    else:
        db_record = []

    return db_record
