#!/usr/bin/env python3
""" DT FL DB Application. """

# Imports - Local
from _81.DTFLDB.db_data import (
    BANNER_START, NO_RESULTS_FOUND
)
from _81.DTFLDB.db_delete import (
    delete_db_record
)
from _81.DTFLDB.db_insert import (
    add_db_record, update_db_record
)
from _81.DTFLDB.db_setup import (
    create_connect_db, create_db_tables
)
from _81.DTFLDB.db_query import (
    display_query_results, query_db
)
from _81.DTFLDB.display_banner import display_banner
from _81.DTFLDB.display_main_menu import display_main_menu
from _81.DTFLDB.get_db_record_selection import get_db_record_user_input
from _81.DTFLDB.get_db_query_input import get_db_query_input
from _81.DTFLDB.quit_program import quit_program


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
                # Get all DB records
                query_results = query_db(
                    get_all_records=True
                )

            elif menu_choice == 2:
                # Search for a DB record or records
                query_results = query_db(
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
            # Add DB records
            add_db_record()

        elif menu_choice == 4:
            # Update a DB record

            # Get all DB records
            query_results = query_db(
                get_all_records=True
            )

            # Display the query results
            if query_results:
                display_query_results(
                    query_results=query_results
                )

                # Collect the number of the DB record to update
                db_record_number = get_db_record_user_input(
                    number_of_records=len(query_results)
                )

                # Update the DB record
                if db_record_number:
                    update_db_record(
                        db_record=query_results[db_record_number - 1]
                    )

                else:
                    continue

            # If no results were found, display a message
            else:
                msg = display_banner(
                    banner_string=NO_RESULTS_FOUND
                )
                print(msg)

        elif menu_choice == 5:
            # Delete a DB record

            # Get all DB records
            query_results = query_db(
                get_all_records=True
            )

            # Display the query results
            if query_results:
                display_query_results(
                    query_results=query_results
                )

                # Collect the number of the DB record to delete
                db_record_number = get_db_record_user_input(
                    number_of_records=len(query_results)
                )

                # Delete the DB record
                if db_record_number:
                    delete_db_record(
                        db_record=query_results[db_record_number - 1]
                    )

                else:
                    continue

            # If no results were found, display a message
            else:
                msg = display_banner(
                    banner_string=NO_RESULTS_FOUND
                )
                print(msg)

        elif menu_choice == 6:
            # Quit the program
            break

    # Display an exit banner and exit the application
    quit_program()

    return None


if __name__ == '__main__':
    main()
