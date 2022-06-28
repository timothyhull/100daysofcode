#!/usr/bin/env python3
""" DT FL DB Application. """

# Imports - Python Standard Library
from sqlite3 import OperationalError
import sqlite3

# Constants
BANNER_START = '** DT FL DB Application **'
BANNER_EXIT = 'Application closed'
DB_EXTENSION = '.sqlite'
DB_NAME = f'dt_fail{DB_EXTENSION}'
DB_TABLE_NAME = 'history'
DB_COLUMN_SQL = (
    '('
    'name TEXT, '
    'outbound_interest_score INT, '
    'inbound_interest_score INT, '
    'num_tries INT ,'
    'fl_reason TEXT'
    ')'
)


def display_banner(
    banner_string: str
) -> None:
    """ Display a welcome banner.

        Args:
            banner_string (str):
                String for the banner display.

        Returns:
            None.
    """

    # Create horizontal and vertical rule strings
    horizontal_rule = f'{(len(banner_string) + 4) * "-"}'
    vertical_rule = f'| {banner_string} |'

    # Create and display full banner string
    banner = (
        f'\n{horizontal_rule}\n'
        f'{vertical_rule}\n'
        f'{horizontal_rule}\n'
    )

    print(banner)

    return None


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
) -> None:
    """ Create DB tables.

        Args:
            db_name (str, optional):
                Name of the db file.  Automatically adds the ".db"
                extension, if not found.  Default value is the value of
                the DB_NAME constant.

        Returns:
            None.
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
                    {DB_COLUMN_SQL}
                '''.strip()
            )

            # Display a success message.
            print(f'\nSuccessfully created the table "{DB_TABLE_NAME}".')

    # Handle exceptions when the DB table already exists
    except OperationalError:

        # Display an informational message
        print(f'\nDB table "{DB_TABLE_NAME}" already exists.')

    return None


def main() -> None:
    """ Main application.

        Args:
            None.

        Returns:
            None.
    """

    # Display a start banner
    display_banner(
        banner_string=BANNER_START
    )

    # Connect to the DB
    db_name = create_connect_db()

    # Create DB tables
    create_db_tables(
        db_name=db_name
    )

    # Display an exit banner
    display_banner(
        banner_string=BANNER_EXIT
    )

    return None


if __name__ == '__main__':
    main()
