#!/usr/bin/env python3
""" Get user input for the DT FL DB Application. """

# Imports - Local
from _81.DTFLDB.quit_program import quit_program


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
