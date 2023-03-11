#!/usr/bin/env pytest
""" Automated unit tests for 'home_inventory.py' """

# Imports - Python Standard Library
from typing import Any
from unittest.mock import patch

# Imports - Third-Party
from _pytest.capture import CaptureFixture
from pytest import mark

# Imports - Local
from _88.inventory_app.home_inventory.home_inventory import (
    HomeInventory,  MAIN_MENU, MENU_PROMPT_DEFAULT
)

# Constants
MOCK_MENU_PROMPT_INPUT = [
    MENU_PROMPT_DEFAULT,            # Default input
    '',                             # Empty string
    None,                           # NoneType object
    False,                          # Boolean object
    '  Enter a menu option',        # Leading spaces
    'Enter a menu option  ',        # Trailing spaces without no colon
    'Enter a menu option:    ',     # Colon with trailing spaces
    'Enter a menu option:  : ',     # Colon and trailing space mixture
]
MOCK_MENU_EXPECTED_VALUE = [
    # List of expected results equal to # of items in `MOCK_MENU_PROMPT_INPUT`
    MENU_PROMPT_DEFAULT for _ in MOCK_MENU_PROMPT_INPUT
]
MOCK_CREATE_MENU_OPTIONS = {
    '4': 'Option #4',
    '1': 'Option #1',
    '6': 'Option #6',
    '3': 'Option #3',
    '5': 'Option #5',
    '2': 'Option #2',
}
MOCK_MAIN_MENU_INPUT = [
    '1',        # Valid input
    '  2',      # Leading spaces
    '3  ',      # Trailing spaces
    ' ',        # Blank space
    # '',         # Empty string
    'wrong',    # Invalid input
    None,       # NoneType object
    # 'False'     # Boolean object
]
MOCK_USER_INPUT_ERROR_MESSAGE = 'Invalid input '
MOCK_MAIN_MENU_EXPECTED_VALUE = [
    MAIN_MENU.get('1'),
    MAIN_MENU.get('2'),
    MAIN_MENU.get('3'),
    MOCK_USER_INPUT_ERROR_MESSAGE,
    MOCK_USER_INPUT_ERROR_MESSAGE,
    # MOCK_USER_INPUT_ERROR_MESSAGE,
    MOCK_USER_INPUT_ERROR_MESSAGE,
    # MOCK_USER_INPUT_ERROR_MESSAGE
]


# TODO: test HomeInventory.__init__

def test_create_main_menu() -> None:
    """ Tests for the `HomeInventory.create_main_menu` method.

        Args:
            None.

        Returns:
            None
    """

    # Create a HomeInventory class instance mock menu options
    hi = HomeInventory(
        menu_items=MOCK_CREATE_MENU_OPTIONS
    )

    # Assert `main_menu` is a sorted list of MOCK_CREATE_MENU_OPTIONS
    assert sorted(
        hi.main_menu.items()
     ) == sorted(
        MOCK_CREATE_MENU_OPTIONS.items()
     )

    return None


@mark.parametrize(
    # Specify argument names for the test `test_format_menu_prompt` arguments
    argnames=[
        'mock_input',
        'expected_value'
    ],
    argvalues=zip(
        # Specify and ZIP the argument input and expected values
        MOCK_MENU_PROMPT_INPUT,
        MOCK_MENU_EXPECTED_VALUE
    )
)
def test_format_menu_prompt(
    mock_input: Any,
    expected_value: Any
) -> None:
    """ Tests for the `HomeInventory.display_menu` method.

        Args:
            mock_input (Any):
                pytest.mark.parameterize input test values.

            expected_value (Any):
                pytest.mark.parameterize expected values for each
                input test value.

        Returns:
            None.
    """

    # Create a HomeInventory class instance with each parameterized value
    hi = HomeInventory(
        input_prompt=mock_input
    )

    # Assert the `input_prompt` of the class instance matches `expected_value`
    assert hi.input_prompt == expected_value

    return None


@mark.parametrize(
    # Specify argument names for the test `test_format_menu_prompt` arguments
    argnames=[
        'mock_input',
        'expected_value'
    ],
    argvalues=zip(
        # Specify and ZIP the argument input and expected values
        MOCK_MAIN_MENU_INPUT,
        MOCK_MAIN_MENU_EXPECTED_VALUE
    )
)
def test_main_menu_output(
    capsys: CaptureFixture,
    mock_input: Any,
    expected_value: Any
) -> None:
    """ Tests for the `HomeInventory.format_menu_prompt` method.

        Args:
            capsys (_pytest.capture.CaptureFixture):
                Capture of STDOUT.

        Returns:
            None.
    """

    # Create a HomeInventory class instance and prompt for user input
    hi = HomeInventory()

    # Send values to prompts for user input during the test
    with patch(
        target='builtins.input',
        side_effect=mock_input
    ):

        user_input = hi.display_main_menu()

        # Assign STDOUT text to a variable
        stdout = capsys.readouterr().out

        # Assert the expected STDOUT output is present
        assert expected_value in stdout

        # Assert the user input selection is a key in the Main Menu dictionary
        assert user_input in MAIN_MENU.keys()

    return None


def test__add_room() -> None:
    """ Tests for the `HomeInventory._add_room` method.

        Args:
            TODO

        Returns:
            None.
    """

    # Create an instance of the HomeInventory class
    hi = HomeInventory()

    # Call the HomeInventory._add_room method
    new_room = hi._add_room()

    # Assert the new room is present
    assert new_room is None

    return None


def test__add_inventory() -> None:
    """ Tests for the `HomeInventory._add_inventory` method.

        Args:
            TODO

        Returns:
            None.
    """

    # Create an instance of the HomeInventory class
    hi = HomeInventory()

    # Call the HomeInventory._add_inventory method
    new_item = hi._add_inventory()

    # Assert the new inventory item is present
    assert new_item is None

    return None


def test__view_inventory_list() -> None:
    """ Tests for the `HomeInventory._view_inventory` method.

        Args:
            TODO

        Returns:
            None.
    """

    # Create an instance of the HomeInventory class
    hi = HomeInventory()

    # Call the HomeInventory._view_inventory method
    inventory = hi._view_inventory()

    # Assert the inventory exists
    assert inventory is None

    return None


def test__total_value() -> None:
    """ Tests for the `HomeInventory._total_value` method.

        Args:
            TODO

        Returns:
            None.
    """

    # Create an instance of the HomeInventory class
    hi = HomeInventory()

    # Call the HomeInventory._total_value method
    total_value = hi._total_value()

    # Assert the total inventory value is present
    assert total_value is None

    return None


def test__exit() -> None:
    """ Tests for the `HomeInventory._exit` method.

        Args:
            TODO

        Returns:
            None.
    """

    # Create an instance of the HomeInventory class
    hi = HomeInventory()

    # Call the HomeInventory._exit method
    exit = hi._exit()

    # Verify the application exits
    assert exit is None

    return None
