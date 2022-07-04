#!/usr/bin/env python3
""" Output messages for the DT FL DB Application. """

# Imports - Local
from _81.DTFLDB.db_data import (
    INVALID_DB_RECORD_INPUT,
    INVALID_MENU_INPUT
)


def invalid_menu_input() -> str:
    """ Display an invalid menu selection message.

        Args:
            None.

        Returns:
            msg (str):
                Message to display.

    """

    msg = f'\n{INVALID_MENU_INPUT}'

    return msg


def invalid_db_record_input() -> str:
    """ Display an invalid db record selection message.

        Args:
            None.

        Returns:
            msg (str):
                Message to display.
    """

    msg = f'\n{INVALID_DB_RECORD_INPUT}'

    return msg
