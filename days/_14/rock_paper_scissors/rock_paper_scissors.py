#!/usr/bin/env python3
""" Rock, Paper, Scissors Game
"""

# Imports
from RPS_Objects import Roll

# Constants
BANNER_MSG = '** Let\'s Play Rock, Paper, Scissors **'
GET_PLAYER_FIRST_NAME_MSG = 'What is your first name? '
ROLLS = [
    'paper',
    'rock',
    'scissors'
]


def display_banner(msg: str = BANNER_MSG) -> None:
    """ Displays the game entry/welcome banner with text decoration

        Args:
            msg (str): Message to display within a banner.
                Default value: BANNER_MSG

        Returns:
            None.
    """

    # Set banner length
    banner_length = len(msg)

    # Display banner:
    print(f'\n{msg}\n'
          f'{"-" * banner_length}\n')


def get_player_name(
        msg: str = GET_PLAYER_FIRST_NAME_MSG,
        first_name: str = ''
        ) -> str:
    """ Collect the player's name.

        Args:
            msg (str): Message prompt to collect player's first name.
            first_name (str): First name of the player.
                Default value: None

        Returns:
            player_name (str): Name of the player.
    """

    if first_name == '':
        player_name = input(msg)

    if player_name == '':
        raise ValueError('A blank name is not allowed')

    return player_name


def main() -> None:
    """ Main program

            Args: None.

            Returns: None
    """

    # Display overview banner
    display_banner()

    # Generate rolls objects
    rolls = list()
    for roll in ROLLS:
        rolls.append(Roll(roll))

    from pprint import pprint as pp
    pp(rolls)


if __name__ == '__main__':
    main()
