#!/usr/bin/env python3
""" DB delete functions for the DT FL DB Application. """

# Imports - Python Standard Library
from typing import List
import sqlite3

# Imports - Local
from _81.DTFLDB.db_data import (
    DB_NAME, DB_TABLE_NAME, DBData
)
from _81.DTFLDB.display_banner import display_banner


def delete_db_record(
    db_name: str = DB_NAME,
    db_record: DBData = None
) -> List[str]:
    """ Delete DB row records based on user input.

        Args:
            db_name (str, optional):
                Name of the DB file. Default value is the value of
                the DB_NAME constant.'

            db_record (DBData):
                DBData object with the DB record data for the record
                to delete.

        Returns:
            db_delete (List):
                List object with raw DB record data.
    """

    # If the response object is a list, insert the new record
    if db_record is not None:

        # Unpack the user input data
        db_delete_record = DBData(*db_record)

        # Build the SQL command to delete the DB record
        db_delete = f'''
            DELETE FROM {DB_TABLE_NAME}
            WHERE id = {db_delete_record.id}
            '''.strip()

        # Connect to a SQLite3 DB and delete the record, if it exists
        with sqlite3.connect(
            database=DB_NAME
        ) as conn:

            # Create a cursor object
            cursor = conn.cursor()

            # Run the SQL command to delete the DB record
            db_delete = cursor.execute(db_delete)

        # Display a success message.
        msg = display_banner(
            banner_string=(
                '** Successfully deleted the record '
                f'"{db_record.name}" **'
            )
        )
        print(msg)

    # If the DB record is None, return an empty list
    else:
        db_delete = []

    return db_delete
