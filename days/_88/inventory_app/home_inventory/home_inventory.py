#!/usr/bin/env python3
""" Home inventory application main program """

# Imports - Python Standard Library
from typing import Dict

# Constants
MAIN_MENU = {
    '1': 'Add Room',
    '2': 'Add Inventory',
    '3': 'View Inventory List',
    '4': 'Total Value',
    '5': 'Exit'
}
MENU_WELCOME = 'Enter a menu option: '


def menu() -> Dict:
    """ Main menu function definition.

        Args:
            None.

        Returns:
            menu (Dict):
                Dictionary with numeric string input keys and
                descriptive values for each.
    """

    # Create a dictionary object and populate it with default values.
    menu = dict(**MAIN_MENU)

    return menu


def display_menu() -> None:
    """ TODO menu loop """

    # TODO
    while True:
        # Display menu and instructions:
        user_input = input(MENU_WELCOME)
        print(user_input)
        if user_input in user_input:
            pass
        break

    return None
