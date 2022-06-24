#!/usr/bin/env python3
""" Script to generate SQLite3 test databases. """

# Imports - Python Standard Library
import sqlite3

# Constants
DB_COLUMNS = '(col1 TEXT, col2 TEXT, col3 TEXT, col4 INT)'
DB_FILE_EXTENSION = '.db'
DB_NAME_INPUT_PROMPT = (
    'What would you like to name the database? '
)
DB_TABLE_NAME = 'test_table'


def get_db_name() -> str:
    """ Collect a DB name from a user.

        Args:
            None.

        Returns:
            db_name (str):
                Database name user input.
    """

    # Collect user input
    db_name = input(DB_NAME_INPUT_PROMPT)

    return db_name


def create_db(
    db_name: str
) -> None:
    """ Create a new DB file.

        Args:
            db_name (str):
                Name of the database file.

        Returns:
            None.
    """

    # Create a DB file and connection
    conn = sqlite3.connect(
        database=f'{db_name}{DB_FILE_EXTENSION}'
    )

    # Create a DB cursor object
    cursor = conn.cursor()

    cursor_command = (f'''
        CREATE TABLE {DB_TABLE_NAME}
        {DB_COLUMNS}
        ''').strip()

    # Create test DB table
    cursor.execute(cursor_command)

    return None


def main() -> None:
    """ Main program

        Args:
            None.

        Returns:
            None.
    """

    db_name = get_db_name()
    create_db(
        db_name=db_name
    )

    return None


if __name__ == '__main__':
    main()
