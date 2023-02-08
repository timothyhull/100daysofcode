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

    def __init__(self) -> None:
        """ Initialization function.

            Args:
                None.

            Returns:
                None.
        """

        # Create a main menu object during class object instantiation
        self.create_main_menu()

        return None

    def create_main_menu(
        self,
        menu_items: Dict = MAIN_MENU
    ) -> None:
        """ Create a main menu object.

            No transformation between the start and end of the method
            take place at this time.  Method is capable of object
            manipulation within this function.

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

        # Create a dictionary object and populate it with default values.
        self.main_menu = dict(**menu_items)

        return None
