#!/usr/bin/env python3
""" Collect user input for a specific DB record. """

# Imports - Local
from _81.DTFLDB.output_messages import invalid_db_record_input
from _81.DTFLDB.quit_program import quit_program


def get_db_record_user_input(
    number_of_records: int
) -> int:
    """ Collect user input for DB record selection.

        Args:
            number_of_records (int):
                Number of records in the DB query results.

        Returns:
            menu_choice (int):
                Menu choice.
    """

    try:
        while True:
            # Get user input
            db_record_choice = input(
                'Enter the number of the record to update, '
                'or "m" for the Main Menu: '
            )

            # Validate record selection
            if not db_record_choice:
                print(invalid_db_record_input())
                continue
            else:
                if db_record_choice == 'm':
                    return None
                else:
                    try:
                        # Determine if the menu selection is an integer
                        db_record_choice = int(db_record_choice)

                    except ValueError:
                        print(invalid_db_record_input())
                        continue

                    # Determine if the DB record is within the range of records
                    if not 1 <= db_record_choice <= number_of_records:
                        print(invalid_db_record_input())
                        continue

            return db_record_choice

    except KeyboardInterrupt:
        # Display a message and exit the application
        quit_program()
