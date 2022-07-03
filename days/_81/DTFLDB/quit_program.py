#!/usr/bin/env python3
""" Quit function for the DT FL DB Application. """

# Imports - Python Standard Library
from sys import exit

# Imports - Local
from _81.DTFLDB.db_data import (
    BANNER_EXIT
)
from _81.DTFLDB.display_banner import display_banner


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
