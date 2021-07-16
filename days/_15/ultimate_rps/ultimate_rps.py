#!/usr/bin/env python3
""" Ultimate Rock, Paper, Scissors game (Ultimate RPS).

    Usage:
        python3 ultimate_rps.py
"""

# Imports
from _15.ultimate_rps.UltimateRPS import UltimateRPS, Player, \
                                         UltimateRPSExceptions

# Constants
NUMBER_OF_PLAYERS = 2
PLAYER_2_DEFAULT_NAME = 'Computer'
PLAYER_INPUT_ATTEMPTS = 3
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


# Get player 1 name
def get_player_1_name() -> str:
    """ Get the player 1 name from STDIN.

        Args:
            None.

        Returns:
            player_name (str): Player name.
    """

    # Initialize loop counter
    loop_count = 1

    # Try to collect non-blank input up to PLAYER_INPUT_ATTEMPTS times
    while loop_count <= PLAYER_INPUT_ATTEMPTS:
        player_name = input('Enter a name for Player 1: ').strip()

        # Exit the loop for a non-blank name entry
        if player_name != '':
            break

        # Restart the loop and increment the counter, for a blank input
        else:
            print('\n** Player 1 name cannot be blank, please try again **\n')
            loop_count += 1

    # Raise a MaxRetriesExceeded excepten after exhausting specified retries
    if player_name == '':
        raise UltimateRPSExceptions.MaxRetriesExceeded(
            max_retries=PLAYER_INPUT_ATTEMPTS
        )

    return player_name


# Get player 2 name
def get_player_2_name() -> str:
    """ Get the player 2 name from STDIN.

        Args:
            None.

        Returns:
            player_name (str): Player name.
    """

    player_name = input(
        'Enter a name for Player 2, or\n'
        ' Press Enter/Return to play the computer: '
    ).strip()

    if player_name == '':
        player_name = PLAYER_2_DEFAULT_NAME

    return player_name


# Display matchup
def display_matchup(player_1, player_2):
    """ Display names and win/loss records, in the current game, for each
        player 1 and player 2.

        Args:
            player_1 (Player): UltimateRPS.Player object for player 1.
            player_2 (Player): UltimateRPS.Player object for player 2.

        Returns:
            None.
    """

    print(
        f'\n** '
        f'{player_1.name} '
        f'({player_1.record.wins}-{player_1.record.losses}) vs '
        f'{player_2.name} '
        f'({player_2.record.wins}-{player_2.record.losses}) '
        f'**\n'
    )


# Get player play
def get_player_play(
    player: Player,
) -> int:
    """ Collect the move for a given player.

        Args:
            player (Player): UltimateRPS Player object.
            play (str): The player's play.

        Returns:
            player (Player): UltimateRPS Player object with updated play list.
    """

    # Display a list of plays to choose from

    # Instantiate object from UltimateRPS and create a list of play choices
    ultimate_rps = UltimateRPS()
    play_choices = list(ultimate_rps.battle_table[0].keys())
    play_choices.remove('Attacker')
    play_choices.sort()

    # Display a list of plays
    for index, play in enumerate(play_choices):
        print(f'{index + 1}. {play}')

    # Gather and validate player input
    play_number = int(input('Enter a play number: ') - 1)

    # Add play to player's play list attribute
    try:
        player.plays.append(play_choices[play_number])

        # Display the player's choice, with the last index in the plays list
        print(f'\n** {player.name} chooses "{play_number + 1} '
              f'({player.plays[-1]})" **\n')

    # Validate player input
    except IndexError:
        print(f'\n** Invalid choice: "{play_number + 1}" **\n')
        raise

    # Return the updated Player object
    return player


# Get play result
def get_play_result():
    pass


# Get game result
def get_game_result():
    pass


def main():
    """ Main program.
    """

    # Display startup banner
    display_banner()

    # Setup player 1
    player_1 = Player(name=get_player_1_name())

    # Setup player 2
    player_2 = Player(name=get_player_2_name())

    # Display matchup details
    display_matchup(
        player_1=player_1,
        player_2=player_2
    )

    # Create a game object from the UltimateRPS class
    ultimate_rps = UltimateRPS()
    print(ultimate_rps)

    # Game loop


if __name__ == '__main__':
    main()
