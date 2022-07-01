#!/usr/bin/env python3
""" DT FL DB Application. """

# Imports - Python Standard Library
from collections import namedtuple
from sqlite3 import OperationalError
from sys import exit
from typing import List, Union
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
NO_RESULTS_FOUND = '** No results found **'


def display_banner(
    banner_string: str
) -> str:
    """ Display a welcome banner.

        Args:
            banner_string (str):
                String for the banner display.

        Returns:
            banner (str).
                Banner to write to STDOUT.
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

    return banner


def quit_program() -> None:
    """ Quit the program.

        Args:
            None.

        Returns:
            None.
    """

    # Display a quit banner
    msg = display_banner(
        banner_string=BANNER_EXIT
    )
    print(msg)

    # Exit the program
    exit(0)


def display_main_menu() -> int:
    """ Display a menu of options.

        Args:
            None.

        Returns:
            menu_choice (int):
                Menu choice.
    """

    try:
        while True:
            # Display a menu
            msg = display_banner(
                banner_string='** Main Menu **'
            )
            print(msg)

            print(
                '\n'
                '1. Display all DB entries\n'
                '2. Display a specific DB entry\n'
                '3. Add a new DB entry\n'
                '4. Update a specific DB entry\n'
                '5. Delete a specific DB entry\n'
                '6. Quit'
                '\n'
            )

            # Get menu selection
            menu_choice = input(
                'Enter a menu selection: '
            )

            # Validate menu selection
            if not menu_choice:
                print(
                    '\n* Invalid menu selection *'
                )
                continue
            else:
                try:
                    # Determine if the menu selection is an integer
                    menu_choice = int(menu_choice)
                except ValueError:
                    print(
                        '\n* Invalid menu selection *'
                    )
                    continue
                # Determine if the menu selection is within the range of 1-6
                if not 1 <= menu_choice <= 6:
                    print(
                        '\n* Invalid menu selection *'
                    )
                    continue

            return menu_choice

    except KeyboardInterrupt:
        # Display a message and exit the application
        quit_program()


def get_db_query_input() -> int:
    """ Get user DB query input.

        Args:
            None.

        Returns:
            query_choice (int):
                Query choice.
    """

    try:
        # Get user search input
        search_input = input(
            'Enter a name to search for, '
            'or press Enter/Return for the main menu: '
        ).lower()

        return search_input

    except KeyboardInterrupt:
        # Display a message and exit the application
        quit_program()


def get_new_record_input() -> Union[List[str], None]:
    """ Get user input.

        Args:
            None.

        Returns:
            new_record_input (List):
                namedtuple object containing user input.
    """

    try:
        while True:
            # Display an informational message
            display_banner(
                banner_string='** Add a new DB entry **'
            )

            # Create a list of user input data
            new_record_input = []

            # Collect name_input
            while True:
                name_input = input(
                    'Enter a name, or "m" for the Main Menu: '
                )

                # Validate name_input
                if name_input:
                    if name_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        new_record_input.append(name_input)
                        break
                else:
                    print(
                        '\n* Invalid name input *'
                    )
                    continue

            # Collect outbound_interest_score_input
            while True:
                outbound_interest_score_input = input(
                    'Enter an outbound interest score (1-5), '
                    'or "m" for the Main Menu: '
                )

                # Validate outbound_interest_score input
                if outbound_interest_score_input:
                    if outbound_interest_score_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        try:
                            outbound_interest_score_input = int(
                                outbound_interest_score_input
                            )
                        except ValueError:
                            print(
                                '\n* Invalid outbound interest score *'
                            )
                            continue
                        else:
                            if 1 <= outbound_interest_score_input <= 5:
                                new_record_input.append(
                                    outbound_interest_score_input
                                )
                                break
                            else:
                                print(
                                    '\n* Invalid outbound interest score *'
                                )
                                continue

            # Collect inbound_interest_score_input
            while True:
                inbound_interest_score_input = input(
                    'Enter an inbound interest score (1-5), '
                    'or "m" for the Main Menu: '
                )

                # Validate inbound_interest_score_input
                if inbound_interest_score_input:
                    if inbound_interest_score_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        try:
                            inbound_interest_score_input = int(
                                inbound_interest_score_input
                            )
                        except ValueError:
                            print('\n* Invalid inbound interest score *')
                            continue
                        else:
                            if 1 <= inbound_interest_score_input <= 5:
                                new_record_input.append(
                                    inbound_interest_score_input
                                )
                                break
                            else:
                                print(
                                    '\n* Invalid inbound interest score *'
                                )
                                continue

            # Collect num_tries input
            while True:
                num_tries_input = input(
                    'Enter a number of attempts, or "m" for the Main Menu: '
                )

                # Validate num_tries input
                if num_tries_input:
                    if num_tries_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        try:
                            num_tries_input = int(num_tries_input)
                        except ValueError:
                            print(
                                '\n* Invalid number of tries *'
                            )
                            continue
                        else:
                            if num_tries_input >= 0:
                                new_record_input.append(num_tries_input)
                                break
                            else:
                                print(
                                    '\n* Invalid number of tries *'
                                )
                                continue

            # Collect fl_reason input
            while True:
                fl_reason_input = input(
                    'Enter a fl reason, or "m" for the Main Menu: '
                )

                # Validate fl_reason input
                if fl_reason_input:
                    if fl_reason_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        new_record_input.append(fl_reason_input)
                        break

            return new_record_input

    except KeyboardInterrupt:
        # Display a message and exit the application
        quit_program()


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


def query_db(
    db_name: str = DB_NAME,
    get_all_records: bool = False,
    query_filter: str = ''
) -> List[DBData]:
    """ Query a DB table for a specific value.

        Args:
            db_name (str, optional):
                Name of the db file.  Automatically adds the ".db"
                extension, if not found.  Default value is the value of
                the DB_NAME constant.'

            get_all_records (bool, optional):
                Type of query to run.  Must be True or False.
                Default is True.

            query_filter (str, optional):
                Filter to apply to the query.  Default is an empty string.

        Returns:
            query_results (List):
                List object with raw DB entry data.
    """

    # Connect to a SQLite3 DB and query the DB table, if it exists
    with sqlite3.connect(
        database=db_name
    ) as conn:

        # Create a cursor object
        cursor = conn.cursor()

        # Run the SQL command to query the DB table for all records
        if get_all_records:
            db_query = cursor.execute(
                f'''
                    SELECT * FROM {DB_TABLE_NAME};
                '''.strip()
            )
        # Run the SQL command to query the DB table for a specific record
        else:
            db_query = cursor.execute(
                f'''
                    SELECT * FROM {DB_TABLE_NAME}
                    WHERE LOWER(name) = "{query_filter}";
                '''.strip()
            )

        # Build a list of DBData namedtuple objects for the query results
        if db_query.arraysize > 0:
            query_results = [
                DBData(
                    name=row[0],
                    inbound_interest_score=row[1],
                    outbound_interest_score=row[2],
                    num_tries=row[3],
                    fl_reason=row[4]
                )
                for row in db_query.fetchall()
            ]

        # If no records were found, return an empty list
        else:
            query_results = []

    return query_results


def display_query_results(
    query_results: List[DBData]
) -> None:
    """ Display query results.

        Args:
            query_results (List):
                List of DBData objects with raw DB entry data.
    """

    if query_results:
        msg = display_banner(
            banner_string=f'** {len(query_results)} results found **'
        )
        print(msg)

        for index, result in enumerate(
            query_results,
            start=1
        ):
            print(
                f'{index}. Name: {result.name}\n'
                f'   Inbound Score: {result.inbound_interest_score}\n'
                f'   Outbound Score: {result.outbound_interest_score}\n'
                f'   Number of Tries: {result.num_tries}\n'
                f'   Failure Reason: {result.fl_reason}\n'
            )

    return None


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


def main() -> None:
    """ Main application.

        Args:
            None.

        Returns:
            None.
    """

    # Display a start banner
    msg = display_banner(
        banner_string=BANNER_START
        )
    print(msg)

    # Connect to the DB
    db_name = create_connect_db()

    # Create DB tables
    msg = create_db_tables(
        db_name=db_name
    )
    print(msg)

    # Loop until the user quits
    while True:
        # Display menu
        menu_choice = display_main_menu()
        if menu_choice in range(1, 3):
            if menu_choice == 1:
                # Get all DB entries
                query_results = query_db(
                    db_name=db_name,
                    get_all_records=True
                )

            elif menu_choice == 2:
                # Search for a DB entry or entries
                query_results = query_db(
                    db_name=db_name,
                    get_all_records=False,
                    query_filter=get_db_query_input()
                )

            # Display the query results
            if query_results:
                display_query_results(
                    query_results=query_results
                )

            # If no results were found, display a message
            else:
                msg = display_banner(
                    banner_string=NO_RESULTS_FOUND
                )
                print(msg)

        elif menu_choice == 3:
            # Add DB entries
            add_db_entry(
                db_name=db_name,
            )

        elif menu_choice == 4:
            pass

        elif menu_choice == 5:
            pass

        elif menu_choice == 6:
            break

    # Display an exit banner and exit the application
    quit_program()

    return None


if __name__ == '__main__':
    main()
