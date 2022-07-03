#!/usr/bin/env python3
""" DB setup functions for the DT FL DB Application. """

# Imports - Python Standard Library
from sqlite3 import OperationalError
import sqlite3

# Imports - Local
from _81.DTFLDB.db_data import (
    DB_EXTENSION, DB_NAME, DB_TABLE_NAME, DB_COLUMN_SQL
)


def check_db_suffix(
    db_name: str
) -> None:
    """ Check for the correct DB file name extension

        Args:
            db_name (str):
                Name of the db file.

        Returns:
            db_name (str):
                Name of the db file.
    """

    # Check for and, if needed add the DB_EXTENSION to the end of the db_name
    if not db_name.endswith(DB_EXTENSION):
        db_name += DB_EXTENSION

    return db_name


def create_connect_db(
    db_name: str = DB_NAME
) -> None:
    """ Create and/or connect to a database file.

        Args:
            db_name (str, optional):
                Name of the db file.  Automatically adds the ".db"
                extension, if not found.  Default value is the value of
                the DB_NAME constant.

        Returns:
            db_name (str):
                Name of the db file.
    """

    # Check for and, if needed add the DB_EXTENSION to the end of the db_name
    db_name = check_db_suffix(
        db_name=db_name
    )

    # Connect to a SQLite3 DB and create a DB file, if it doesn't already exist
    with sqlite3.connect(
        database=db_name
    ):
        print(f'Successfully connected to "{db_name}".')

    return db_name


def create_db_tables(
    db_name: str = DB_NAME
) -> str:
    """ Create DB tables.

        Args:
            db_name (str, optional):
                Name of the db file.  Automatically adds the ".db"
                extension, if not found.  Default value is the value of
                the DB_NAME constant.

        Returns:
            msg (str):
                Database transaction status message to write to STDOUT.
    """

    # Check for and, if needed add the DB_EXTENSION to the end of the db_name
    db_name = check_db_suffix(
        db_name=db_name
    )

    # Connect to a SQLite3 DB, and create tables, if not already present
    try:
        with sqlite3.connect(
            database=db_name
        ) as db_conn:

            # Create a cursor object
            cursor = db_conn.cursor()

            # Run the SQL command to create a DB table
            cursor.execute(
                f'''
                    CREATE TABLE {DB_TABLE_NAME}
                    {DB_COLUMN_SQL};
                '''.strip()
            )

            # Display a success message.
            msg = (
                f'\n\n** Successfully created the table "{DB_TABLE_NAME}" **.'
            )

    # Handle exceptions when the DB table already exists
    except OperationalError:

        # Display an informational message
        msg = f'\nDB table "{DB_TABLE_NAME}" is available.'

    return msg
