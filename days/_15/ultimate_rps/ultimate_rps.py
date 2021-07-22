#!/usr/bin/env python3
""" Ultimate Rock, Paper, Scissors game (Ultimate RPS).

    Usage:
        python3 ultimate_rps.py
"""

# Imports
from _15.ultimate_rps.UltimateRPS import UltimateRPS, Player, \
                                         UltimateRPSExceptions
from collections import namedtuple

# Constants
NUMBER_OF_PLAYS = 3
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
) -> Player:
    """ Collect the move for a given player.

        Args:
            player (Player): UltimateRPS Player object.

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
    play_number = int(input('Enter a play number: ')) - 1

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
def get_play_result(
    player_1: Player,
    player_2: Player
) -> namedtuple:
    """ Get the result/winner after each play.

        Args:
            player_1 (Player): UltimateRPS.Player object for player 1.
            player_2 (Player): UltimateRPS.Player object for player 2.

        Return:
            play_result (namedtuple): player_1 and player_2 objects plus
                                      text result for player_1.

    """

    # Instantiate ultimateRPS object
    ultimate_rps = UltimateRPS()

    # Create namedtuple object to store play results
    PlayResult = namedtuple(
        'PlayResult',
        'player_1 player_2 player_1_result'
    )

    # Determine play result
    player_1_result = ultimate_rps.get_turn_result(
        player_1_play=player_1.plays[-1],
        player_2_play=player_2.plays[-1]
    )

    # Update the score for each Player object and display the game outcome
    if player_1_result == 'lose':
        player_1.score += 1
        print(f'{player_1.name} scores 1 point.\n')

    elif player_1_result == 'win':
        player_2.score += 1
        print(f'{player_2.name} scores 1 point.\n')

    else:
        print('Draw play.\n')

    # Set the turn results in a namedtuple object
    play_result = PlayResult(player_1, player_2, player_1_result)

    return play_result


# Get game result
def get_game_result(
    player_1: Player,
    player_2: Player
) -> namedtuple:
    """ Get the result/winner after each play.

        Args:
            player_1 (Player): UltimateRPS.Player object for player 1.
            player_2 (Player): UltimateRPS.Player object for player 2.

        Return:
            game_results (namedtuple): player_1 and player_2 objects plus
                                      winner attrobute, with winning player.

    """

    # Determine if player_1 is the winner
    if player_1.score > player_2.score:
        # Set the winner as player_1
        winner = player_1.name

        # Increment the player records
        player_1.record = player_1.record._replace(
            wins=player_1.record.wins + 1
        )
        player_2.record = player_2.record._replace(
            losses=player_1.record.losses + 1
        )

    # Determine if player_2 is the winner
    elif player_1.score < player_2.score:
        winner = player_2.name

        # Increment the player records
        player_1.record = player_1.record._replace(
            losses=player_1.record.losses + 1
        )
        player_2.record = player_2.record._replace(
            wins=player_1.record.wins + 1
        )

    # Determine if the game is a draw
    else:
        winner = ''

        # Increment the player records
        player_1.record = player_1.record._replace(
            draws=player_1.record.draws + 1
        )
        player_2.record = player_2.record._replace(
            draws=player_2.record.draws + 1
        )

    # Create a namedtuple class to return
    PlayResults = namedtuple('PlayResults', 'player_1 player_2 winner')

    # Create a play_results namedtuple instance to return
    game_results = PlayResults(
        player_1=player_1,
        player_2=player_2,
        winner=winner
    )

    return game_results


# Game Loop
def game_loop(
    game_object: UltimateRPS,
    player_1: Player,
    player_2: Player
) -> None:
    """ Loop through gameplay until canceled.

        Args:
            game_object (UltimateRPS): Instantiation of the UltimateRPS class.
            player_1 (Player): Instantiation of the Player class, for player 1.
            player_2 (Player): Instantiation of the Player class, for player 2.

        Returns:
            None.
    """

    # Initalize the game number count
    game_number = 1

    # Start the loop of games
    while True:
        # Display the current game number
        print(f'* Game #{game_number} *\n')

        # Start the play loop, for the total NUMBER_OF_PLAYS
        for index in range(NUMBER_OF_PLAYS):
            # Display the current play index and play total
            print(f'* Play {index +1} of {NUMBER_OF_PLAYS} *\n')

            # Get plays for each player
            player_1 = get_player_play(player=player_1)
            player_2 = get_player_play(player=player_2)

            # Determine the winner of the head-to-head plays
            play_result = get_play_result(
                player_1=player_1,
                player_2=player_2
            )
            player_1 = play_result.player_1
            player_2 = play_result.player_2

        # Determine the winner of the game (after all plays)
        game_result = get_game_result(
            player_1=player_1,
            player_2=player_2
        )
        player_1 = game_result.player_1
        player_2 = game_result.player_2

        print(f'*** {game_result.winner} wins! ***\n'
              f'\tPlayer 1 record: {player_1.record}\n'
              f'\tPlayer 2 record: {player_2.record}\n')

        game_number += 1


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

    # Game loop
    game_loop(
        game_object=ultimate_rps,
        player_1=player_1,
        player_2=player_2
    )


if __name__ == '__main__':
    main()
