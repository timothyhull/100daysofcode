#!/usr/bin/env python3
""" Ultimate Rock, Paper, Scissors game (Ultimate RPS).

    Usage:
        python3 ultimate_rps.py
"""

# Imports
from _15.ultimate_rps.UltimateRPS import UltimateRPS, Player

# Constants
ATTEMPTS = 3
STARTUP_BANNER = '** Ultimate Rock, Paper, Scissors **'


# Display banner
def display_banner(banner_text: str = STARTUP_BANNER) -> None:
    """ Display a banner.

        Args:
            banner_text (str): Text to display in the banner.
                Default: STARTUP_BANNER

        Returns:
            None.
    """

    # Get the length of the banner text
    banner_length = len(banner_text)

    # Display the banner
    print(f'\n{banner_text}\n'
          f'{"-" * banner_length}\n')


# Get player name
def get_player_name(player_number: int) -> str:
    """ Get player name from STDIN

        Args:
            player_number (int): Player number.

        Returns:
            player_name (str): Player name input from STDIN.
                Default: 'Computer'
    """

    player_name = ''
    count = 1

    while count <= ATTEMPTS:
        if player_number == 1:
            print(f'Enter the name for player #{player_number}: ')
            player_name = input()

            if player_name != '':
                break
            else:
                print('* Invalid name, please try again *\n')
                continue

        elif player_number == 2:
            print(f'Enter the name for player #{player_number}'
                  f'or press "Enter" to play against the computer: ')
            player_name = input()
            break

        else:
            raise ValueError('Invalid player number, should be 1 or 2.')

    if player_number == 1 and player_name == '':
        raise ValueError('Invalid player name (cannot be blank).')         

    return player_name


# Get player play
def get_player_play(player):
    pass


# Get play result
def get_play_result():
    pass


# Get game result
def get_game_result():
    pass


def main():
    """ Main program loop.
    """

    # Display startup banner
    display_banner()

    # Create player objects from the Player class
    player_1 = Player()
    player_2 = Player()
    print(player_1, player_2)

    # Create a game object from the UltimateRPS class
    ultimate_rps = UltimateRPS()
    print(ultimate_rps)


if __name__ == '__main__':
    main()
