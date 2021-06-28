#!/usr/bin/env python3
""" Rock, Paper, Scissors Game
"""

# Imports
from _14.rock_paper_scissors.RPS_Objects import Roll, Player

# Constants
BANNER_MSG = '** Let\'s Play Rock, Paper, Scissors **'
GAME_LOOPS = 3
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


def game_loop(
    player_1: Player,
    player_2: Player,
    rolls: Roll
) -> None:
    """ Loop over game play N times and determine a winner.

        Args:
            player_1 (RPS_Objects.Player): Player object for human player.
            player_2 (RPS_Objects.Player): Player object for computer player.
            rolls (list): List of RPS_Objects.Rolls.

        Returns:
            None.
    """
    pass


def main() -> None:
    """ Main program

            Args:
                None.

            Returns:
                None.
    """

    # Display overview banner
    display_banner()

    # Generate rolls objects
    rolls = list()
    for roll in ROLLS:
        rolls.append(Roll(roll))

    # Get player name
    player_name = get_player_name()

    # Create player objects
    player_1 = Player(player_name)
    player_2 = Player()

    # Run the game loop

    print(player_1, player_2)


if __name__ == '__main__':
    main()
