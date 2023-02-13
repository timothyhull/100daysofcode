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
MENU_PROMPT_DEFAULT = 'Enter a menu option: '
PROMPT_SUFFIX = ': '


class HomeInventory:
    """ Home inventory application main object class. """

    def __init__(
        self,
        menu_items: Dict = MAIN_MENU,
        input_prompt: str = MENU_PROMPT_DEFAULT
    ) -> None:
        """ Initialization function.

            Args:
                menu_items (Dict, optional):
                    Dictionary with numeric string input keys and
                    descriptive values for each key.
                    Default is MAIN_MENU.

                    Example:

                    menu = {
                        '1': 'Option 1',
                        '2': 'Option 2',
                        '3': 'Option 3',
                        '4': 'Exit'
                    }

                input_prompt (str, optional):
                    str value to display as prompt for user input.

            Returns:
                None.
        """

        # Create a main menu object
        self.create_main_menu(
            menu_items=menu_items
        )

        # Create a menu prompt
        self.format_menu_prompt(
            input_prompt=input_prompt
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
                    descriptive values for each key.

                    Example:

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

    def format_menu_prompt(
        self,
        input_prompt: str = MENU_PROMPT_DEFAULT
    ) -> None:
        """ Check and format the CLI menu input prompt.

            Args:
                input_prompt (str, optional):
                    str value to display as prompt for user input.
                    This method will add a colon and a single space
                    suffix to the prompt, if not already present,
                    for readability.  Default is MENU_PROMPT_DEFAULT.

                    Example:

                    1. 'Enter option' becomes 'Enter option: `
                    2. 'Enter option:' becomes 'Enter option: `
                    3. 'Enter option: ' does not change.

            Returns:
                None.
        """

        # Ensure the 'input_prompt' argument is a string
        if isinstance(input_prompt, str) is True:

            print(f'Prompt={input_prompt}')
            print(f'Type={type(input_prompt)}')

            # Remove any leading spaces in 'input_prompt'
            input_prompt = input_prompt.lstrip()

            # Determine if 'input_prompt' the correct suffix
            if input_prompt.endswith(PROMPT_SUFFIX, -2) is False:
                # Remove any trailing spaces
                input_prompt = input_prompt.rstrip()

                # Determine if 'input_prompt' ends with a colon
                if input_prompt.endswith(PROMPT_SUFFIX[0]) is True:
                    # Add a space character
                    input_prompt += PROMPT_SUFFIX[1]

                # If 'input_prompt' does not end with a colon, add the suffix
                else:
                    input_prompt += PROMPT_SUFFIX

        # Set the self.user_input value
        self.input_prompt = input_prompt

        return None
