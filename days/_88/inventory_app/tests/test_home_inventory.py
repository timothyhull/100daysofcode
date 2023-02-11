#!/usr/bin/env pytest
""" Automated unit tests for 'home_inventory.py' """

# Imports - Third-Party
from pytest import mark

# Imports - Local
from _88.inventory_app.home_inventory.home_inventory import (
    HomeInventory,  MENU_PROMPT_DEFAULT
)

# Constants
MOCK_MENU_PROMPT_INPUT = [
    MENU_PROMPT_DEFAULT,            # Default input
    '',                              # Empty string
    None,                           # NoneType object
    False,                          # Boolean object
    '  Enter a menu option',        # Leading spaces
    'Enter a menu option  ',        # Trailing spaces without no colon
    'Enter a menu option:    ',     # Colon with trailing spaces
    'Enter a menu option:  : ',     # Colon and trailing space mixture
]
MOCK_MENU_EXPECTED_VALUE = [
    MENU_PROMPT_DEFAULT,            # Default input
    MENU_PROMPT_DEFAULT,            # Default input
    MENU_PROMPT_DEFAULT,            # Default input
    MENU_PROMPT_DEFAULT,            # Default input
    MENU_PROMPT_DEFAULT,            # Default input
    MENU_PROMPT_DEFAULT,            # Default input
    MENU_PROMPT_DEFAULT             # Default input
]


# TODO: test HomeInventory.__init__


# TODO: test HomeInventory.create_main_menu


# TODO: test HomeInventory.format_menu_prompt
@mark.parametrize(
    # TODO
    argnames=[
        'mock_input',
        'expected_value'
    ],
    argvalues=zip(
        # TODO
        MOCK_MENU_PROMPT_INPUT,
        MOCK_MENU_EXPECTED_VALUE
    )
)
def test_format_menu_prompt(
    mock_input: str,
    expected_value: str
) -> None:
    """ TODO """

    print(f'Mock Input: {mock_input}')
    print(f'Expected Value: {expected_value}')

    # TODO
    hi = HomeInventory(
        input_prompt=mock_input
    )

    # TODO
    assert hi.input_prompt == expected_value

    return None
