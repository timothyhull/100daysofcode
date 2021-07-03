#!/usr/bin/env python3
""" Rock, Paper, Scissors Game
"""

# Imports
from _14.rock_paper_scissors.RPS_Objects import Roll, Player
from random import choice
from sys import exit

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
    rolls: list
) -> None:
    """ Loop over game play N times and determine a winner.

        Args:
            player_1 (RPS_Objects.Player): Player object for human player.
            player_2 (RPS_Objects.Player): Player object for computer player.
            rolls (list): List of RPS_Objects.Rolls.

        Returns:
            None.
    """

    # Initialize the game loop counter
    loop_count = 1

    # Start the game loop
    while loop_count < GAME_LOOPS + 1:
        # Display loop banner
        results_header = f'Round {loop_count} of {GAME_LOOPS}'
        print(f'\n{results_header}\n'
              f'{"-" * len(results_header)}\n'
              f'{player_1.name}: {player_1.score}'
              f'\t{player_2.name}: {player_2.score}')

        # Initialize round_winner variable
        round_winner = None

        # Randomly choose a roll for player 2 (computer)
        player_2.roll = choice(rolls)

        # Display a list of choices
        print('\nChoices:')
        for index, roll in enumerate(rolls):
            print(f'{index +1}. '
                  f'{roll.name.title()}')

        player_1_input = input(f'\nMake your choice - '
                               f'1-{len(rolls)}: ')

        try:
            # Confirm the input is an integer greater than 0 and in range
            valid_input = int(player_1_input) in range(1, len(rolls) + 1)
            if valid_input is True:
                player_1.roll = rolls[int(player_1_input) - 1]
            else:
                raise ValueError

        except ValueError:
            # Display error for non-integer value
            print('\n** Invalid choice **')
            continue

        except IndexError:
            # Display error for out-of-range value
            print('\n** Invalid choice **')
            continue

        # Determine the winner for this loop iteration
        # Display each players' roll
        print(f'\n** {player_1.name} chooses {player_1.roll.name}\n'
              f'** {player_2.name} chooses {player_2.roll.name}')

        if player_1.roll.name == player_2.roll.name:
            # If the roll values are equal, declare a tie
            print('\n** This round is a tie **')

        # Determine if player 1 beats player 2 this round
        else:
            if player_1.roll.name == player_2.roll.lose:
                round_winner = player_1
            else:
                round_winner = player_2

        # add to the winner's score
        if round_winner is not None:
            round_winner.score += 1

        # Add to the loop counter
        loop_count += 1

    # Display game results
    print('\n** Final Score **\n')
    print(f'{player_1.name}: {player_1.score}'
          f'\t{player_2.name}: {player_2.score}\n')

    if player_1.score == player_2.score:
        print('** Tie Game **\n')

    elif player_1.score > player_2.score:
        print(f'** {player_1.name} wins **\n')

    else:
        print(f'** {player_2.name} wins **\n')


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
    rolls = []
    for roll in ROLLS:
        rolls.append(Roll(roll))

    # Get player name
    player_name = get_player_name()

    # Create player objects
    player_1 = Player(player_name)
    player_2 = Player()

    # Run the game loop
    game_loop(
        player_1=player_1,
        player_2=player_2,
        rolls=rolls
    )


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print()
        exit(0)
