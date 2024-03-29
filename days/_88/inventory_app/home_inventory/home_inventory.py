#!/usr/bin/env python3
""" Home inventory application classes and methods. """

# Imports - Python Standard Library
from os import environ
from typing import Callable, Dict, Union
import sys

# Constants
KEYBOARD_INTERRUPT_MESSAGE = 'User-initiated application shutdown.'
MAIN_MENU = {
    '1': 'Add Room',
    '2': 'Add Inventory',
    '3': 'View Inventory List',
    '4': 'Total Value',
    '5': 'Exit'
}
MAIN_MENU_BANNER = '** Home Inventory App - Main Menu **'
MENU_PROMPT_DEFAULT = 'Enter a menu option: '
PROMPT_SUFFIX = ': '
PYTEST_ENV_VAR = 'PYTEST_CURRENT_TEST'
USER_INPUT_ERROR_MESSAGE = 'Invalid input "{}", please try again.'


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
                    Default value is MAIN_MENU.

                    Example:

                    menu = {
                        '1': 'Option 1',
                        '2': 'Option 2',
                        '3': 'Option 3',
                        '4': 'Exit'
                    }

                input_prompt (str, optional):
                    str value to display as prompt for user input.
                    Default value is MENU_PROMPT_DEFAULT.

            Returns:
                None.
        """

        # Map valid user input options to methods
        self.user_input_map = {
            '1': self._add_room(),
            '2': self._add_inventory(),
            '3': self._view_inventory(),
            '4': self._add_room(),
            '5': self._exit()
        }

        # Create a main menu object
        self.create_main_menu(
            menu_items=menu_items
        )

        # Create a menu prompt
        self.format_menu_prompts(
            input_prompt=input_prompt
        )

        return None

    def create_main_menu(
        self,
        menu_items: Dict
    ) -> None:
        """ Create a main menu object.

            This method provides the option of creating a custom
            menu object.

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

                    The constant 'MAIN_MENU' contains a default menu.

            Returns:
                None.
        """

        # Create a dictionary object and populate it user-supplied values.
        self.main_menu = dict(**menu_items)

        return None

    def format_menu_prompts(
        self,
        input_prompt: str = MENU_PROMPT_DEFAULT
    ) -> None:
        """ Check and format the CLI menu input prompt.

            Args:
                input_prompt (str, optional):
                    str value to display as prompt for user input.
                    This method will add a colon and a single space
                    suffix to the prompt, if not already present,
                    for readability.  Default value is
                    MENU_PROMPT_DEFAULT.

                    Example:

                    1. 'Enter option' becomes 'Enter option: '
                    2. 'Enter option:' becomes 'Enter option: '
                    3. 'Enter option: ' does not change.

            Returns:
                None.
        """

        # Ensure the 'input_prompt' argument is a non-blank string
        if isinstance(input_prompt, str) is True \
           and input_prompt != '':

            # Remove any leading spaces in 'input_prompt'
            input_prompt = input_prompt.lstrip()

            # Check 'input_prompt' for the correct suffix
            if input_prompt.endswith(PROMPT_SUFFIX) is False:
                # Remove any trailing spaces
                input_prompt = input_prompt.rstrip()

                # Add the correct suffix
                if input_prompt.endswith(PROMPT_SUFFIX[0]):
                    # Add a blank space if the string ends with ':'
                    input_prompt += PROMPT_SUFFIX[1]
                else:
                    # Add the full suffix if the string does not end with ':'
                    input_prompt += PROMPT_SUFFIX

            # Remove any excess instances of the correct suffix
            if input_prompt.count(PROMPT_SUFFIX) != 1:
                # Split the prompt string from instances of PROMPT_SUFFIX
                prompt_parts = input_prompt.partition(PROMPT_SUFFIX[0])

                # Format input_string with one instance of PROMPT_SUFFIX
                input_prompt = prompt_parts[0] + PROMPT_SUFFIX

        else:
            # Use the default prompt when `input_prompt` is a blank string
            input_prompt = MENU_PROMPT_DEFAULT

        # Set the self.user_input value to the formatted prompt
        self.input_prompt = input_prompt

        return None

    def display_main_menu(self) -> str:
        """ Display the main menu, collect user input, run methods.

            Args:
                None.

            Returns:
                user_input (str):
                    Valid user input selection.
        """

        # Collect and validate user input
        while True:
            # Display the menu, sorted by key, and input prompt
            print(f'\n{MAIN_MENU_BANNER}\n')
            for key, value in sorted(self.main_menu.items()):
                print(f'{key}. {value}')

            try:
                print()
                user_input = input(self.input_prompt)

            # Exception handling for KeyboardInterrupt exceptions
            except KeyboardInterrupt:
                # Display friendly message
                print(f'\n{KEYBOARD_INTERRUPT_MESSAGE}\n')

                # Gracefully close the application
                sys.exit()

            # Validate user input
            if user_input.strip() in self.main_menu.keys():
                print(
                    f'\nUser selects option {user_input}, '
                    f'"{self.main_menu.get(user_input)}"\n'
                )

                # Break the loop after a successful menu selection
                break

            # Display an invalid input message
            print(f'\n{USER_INPUT_ERROR_MESSAGE.format(user_input)}')

            # Break the loop if method called by pytest
            if PYTEST_ENV_VAR in str(environ.keys()):
                break
            else:
                # Continue to the next loop iteration
                continue

        return user_input

    def get_input_method(
        self,
        user_input: Union[int, str]
    ) -> Callable:
        """ Gets a method based on the user input value.

            Args:
                user_input (Union[int, str]):
                    Menu option user input.

            Returns:
                input_method (Callable):
                    Method that corresponds with the 'user_input'
                    argument value.
        """

        # Ensure the value of 'user_input' is a string:
        user_input = str(user_input)

        # Determine if the value in 'user_input' is valid
        if user_input not in self.user_input_map.keys():
            raise ValueError(
                'user_input parameter must be one of '
                f'{", ".join(self.user_input_map)}'
            )
        else:
            input_method = self.user_input_map.get(
                user_input
            )
            print(
                self.user_input_map.get(
                    user_input
                )
            )

        return input_method

    def _add_room(self) -> str:
        """ TODO

            Args:
                TODO

            Returns:
                TODO
        """

        return '_add_room'

    def _add_inventory(self) -> str:
        """ TODO

            Args:
                TODO

            Returns:
                TODO
        """

        return '_add_inventory'

    def _view_inventory(self) -> str:
        """ TODO

            Args:
                TODO

            Returns:
                TODO
        """

        return '_view_inventory'

    def _total_value(self) -> str:
        """ TODO

            Args:
                TODO

            Returns:
                TODO
        """

        return '_total_value'

    def _exit(self) -> str:
        """ TODO

            Args:
                TODO

            Returns:
                TODO
        """

        return '_exit'
