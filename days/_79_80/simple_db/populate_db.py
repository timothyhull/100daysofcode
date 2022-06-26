#!/usr/bin/env python3
""" Script to populate a SQLite3 test database. """

# Imports - Python Standard Library
from typing import List
import sqlite3

# Constants
DB_NAME = 'address_book.db'
DB_TABLE_NAME = 'Details'
NAME_INPUT_PROMPT = (
    'What is your name? '
)
ADDRESS_INPUT_PROMPT = (
    'What is your address? '
)
PHONE_INPUT_PROMPT = (
    'What is your phone number? '
)


def get_name() -> str:
    """ Collect a name from a user.

        Args:
            None.

        Returns:
            name (str):
                Name user input.
    """

    # Collect user input
    name = input(NAME_INPUT_PROMPT)

    return name


def get_address() -> str:
    """ Collect an address from a user.

        Args:
            None.

        Returns:
            name (str):
                Address user input.
    """

    # Collect user input
    address = input(ADDRESS_INPUT_PROMPT)

    return address


def get_phone() -> str:
    """ Collect a phone number from a user.

        Args:
            None.

        Returns:
            name (str):
                Phone number user input.
    """

    # Collect user input
    phone = input(PHONE_INPUT_PROMPT)

    return phone


def insert_data(
    name: str,
    address: str,
    phone: str
) -> List:
    """ Create a new table row with user input data.

        Args:
            name (str):
                Name user input.

            address (str):
                Address user input.

            phone (str):
                Phone user input.

        Returns:
            result (List):
                Result of a query for the new DB row.
    """

    # Create a DB file and connection
    with sqlite3.connect(
            database=DB_NAME
         ) as conn:

        # Create a DB cursor object
        cursor = conn.cursor()

        # Prepare the SQL query
        cursor_command = (f'''
            INSERT INTO {DB_TABLE_NAME}
            VALUES ("{name}", "{address}", "{phone}")
            ''').strip()

        # Insert new row
        cursor.execute(cursor_command)
        conn.commit()

        # Prepare the SQL query
        cursor_command = (f'''
            SELECT name, address, phone_number
            FROM {DB_TABLE_NAME}
            WHERE name == "{name}"
            AND address == "{address}"
            AND phone_number == "{phone}"
            ''').strip()

        # Query the new row
        result = conn.execute(cursor_command).fetchall()

    return result


def main() -> None:
    """ Main program

        Args:
            None.

        Returns:
            None.
    """

    # Display instructions
    print('\n *** Insert DB Row Tool ***\n')

    # Prepare to catch KeyboardInterrupt exceptions
    try:
        # Loop over the row insertion process until user exit
        while True:
            menu_input = input(
                'Press "Enter/Return to insert a new row, '
                'or type "q" and press Enter/Return to exit: '
            )

            # Check menu_input value
            if menu_input.lower() == 'q':
                print('\nQuitting program.\n')
                break

            # Collect user input for a name
            name = get_name()

            # Collect user input for an address
            address = get_address()

            # Collect user input for a phone number
            phone = get_phone()

            # Insert a new DB row
            print(
                '\nInserting new DB row:\n'
                f'\tName: {name}\n'
                f'\tAddress: {address}\n'
                f'\tPhone: {phone}\n'
            )

            result = insert_data(
                name=name,
                address=address,
                phone=phone
            )

            print(
                'Successfully inserted new row:\n'
                f'{result}\n'
            )

    # Catch KeyboardInterrupt exceptions
    except KeyboardInterrupt:
        print('\nEscape sequence detected.\n')

    return None


if __name__ == '__main__':
    main()
