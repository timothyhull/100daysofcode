#!/usr/bin/env python3
""" Ultimate Rock, Paper, Scissors game (Ultimate RPS).

    Usage:
        python3 ultimate_rps.py
"""

# Imports
from collections import namedtuple
from _15.ultimate_rps.UltimateRPS import UltimateRPS, Player

# Constants
NUMBER_OF_PLAYERS = 2
PLAYER_NAME_ATTEMPTS = 3
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


# Setup player objects
def setup_players(
    player_1_name: str,
    player_2_name: str = 'Computer'
) -> namedtuple:
    """ Get player name from STDIN

        Args:
            player_1_name (str): Player 1 name.
            player_2_name (str): Player 2 name.
                Default: 'Computer'

        Returns:
            players (namedtuple): namedtuple of Player objects for each of
                                  two players.
    """

    # Create namedtuple class for player objects
    Players = namedtuple('Players', 'player_1 player_2')

    players = Players(
        player_1=Player(name=player_1_name),
        player_2=Player(name=player_2_name)
    )

    return players


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

    # Setup player objects
    for player in range(NUMBER_OF_PLAYERS):

        loop_count = 1

        while loop_count <= PLAYER_NAME_ATTEMPTS:
            print(f'Enter the name for player #{player + 1}: ')
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


    # Create a game object from the UltimateRPS class
    ultimate_rps = UltimateRPS()
    print(ultimate_rps)


if __name__ == '__main__':
    main()
