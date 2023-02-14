#!/usr/bin/env pytest
""" Automated unit tests for 'home_inventory.py' """

# Imports - Third-Party
from pytest import mark
from typing import Any

# Imports - Local
from _88.inventory_app.home_inventory.home_inventory import (
    HomeInventory,  MENU_PROMPT_DEFAULT
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

# TODO: test HomeInventory.__init__


# TODO: test HomeInventory.create_main_menu


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
    """ Tests for the `HomeInventory.format_menu_prompt` method.

        Args:
            mock_input (Any):
                pytest.mark.parameterize input test values.

            expected_value (Any):
                pytest.mark.parameterize expected values for each
                input test value.

        Returns:
            None.
    """

    # print(f'Mock Input: {mock_input}')
    # print(f'Expected Value: {expected_value}')

    # Create a HomeInventory class instance with each parameterized value
    hi = HomeInventory(
        input_prompt=mock_input
    )

    # Assert the `input_prompt` of the class instance matches `expected_value`
    assert hi.input_prompt == expected_value

    return None
