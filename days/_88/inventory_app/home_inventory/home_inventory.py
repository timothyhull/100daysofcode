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


class HomeInventory:
    """ Home inventory application main object class. """

    def __init__(
        self,
        menu_items: Dict = MAIN_MENU
    ) -> None:
        """ Initialization function.

            Args:
                menu_items (Dict, optional):
                    Dictionary with numeric string input keys and
                    descriptive values for each key. Example:

                menu = {
                    '1': 'Option 1',
                    '2': 'Option 2',
                    '3': 'Option 3',
                    '4': 'Exit'
                }

            Returns:
                None.
        """

        # Create a main menu object during class object instantiation
        self.create_main_menu(
            menu_items=menu_items
        )

        return None

    def create_main_menu(
        self,
        menu_items: Dict
    ) -> None:
        """ Create a main menu object.

            This method provides the option of manipulating the
            data within the menu object.

            Args:
                menu_items (Dict):
                    Dictionary with numeric string input keys and
                    descriptive values for each key. Example:

                menu = {
                    '1': 'Option 1',
                    '2': 'Option 2',
                    '3': 'Option 3',
                    '4': 'Exit'
                }

            Returns:
                None.
        """

        # Create a dictionary object and populate it with default values.
        self.main_menu = dict(**menu_items)

        return None
