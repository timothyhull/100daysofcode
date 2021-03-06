#!/usr/bin/env pytest
""" Test functions for Ultimate Rock, Paper, Scissors (Ultimate RPS).

    Usage:
        pytest ultimate_rps.py
"""

# Imports
from _15.ultimate_rps.UltimateRPS import UltimateRPS, Player, \
                                         UltimateRPSExceptions
from _15.ultimate_rps.ultimate_rps import display_banner, display_matchup, \
                                          get_player_1_name, \
                                          get_player_2_name, get_player_play, \
                                          get_play_result, get_game_result

from collections import namedtuple
from pytest import fixture, mark, raises
from random import randint
from re import compile, VERBOSE
from unittest.mock import patch

# Constants
BANNER_OUTPUT = '** Ultimate Rock, Paper, Scissors **'
MATCHUP_OUTPUT_REGEX = compile(
    r'''
    ^\*\*\s       # Match '** '
    .+\s          # Match 'Player 1 Name '
    \(\d+-\d+\)   # Match win/loss record '(13-4)'
    \svs\s        # Match ' vs '
    .+\s          # Match 'Player 2 Name '
    \(\d+-\d+\)   # Match win/loss record '(4-13)'
    \s\*\*$       # Match ' **'
    ''',
    VERBOSE
)
NUMBER_OF_PLAYERS = 2
NUMBER_OF_PLAYS = 3
PLAYER_1_NAME = 'Tim'
PLAYER_2_NAME = 'Computer'
PLAYER_1_PLAYS = [
    'Scissors',
    'Paper',
    'Rock',
    'Air',
    'Devil',
    'Tree',
    'Snake',
    'Wolf',
    'Fire',
    'Sponge'
]
PLAYER_2_PLAYS = [
    'Rock',
    'Paper',
    'Scissors',
    'Dragon',
    'Human',
    'Lightning',
    'Snake',
    'Water',
    'Gun',
    'Sponge'
]
EXPECTED_RESULTS = [
    'lose',
    'draw',
    'win',
    'win',
    'win',
    'lose',
    'draw',
    'win',
    'lose',
    'draw'
]

# Combine lists to form a 3-tuple object, for parameterize compatibility
# For test_get_play_result() function
GAMEPLAY_ARGS_1 = zip(
    PLAYER_1_PLAYS,
    PLAYER_2_PLAYS,
    EXPECTED_RESULTS
)

# For test_play_result()
GAMEPLAY_ARGS_2 = zip(
    PLAYER_1_PLAYS,
    PLAYER_2_PLAYS,
    EXPECTED_RESULTS
)

PLAYER_1_GAME_SCORES = [
    0,
    2,
    1,
    0
]
PLAYER_2_GAME_SCORES = [
    3,
    1,
    1,
    0
]
PLAYER_1_RECORD_WINS = [
    0,
    1,
    0,
    0
]
PLAYER_2_RECORD_WINS = [
    1,
    0,
    0,
    0
]
PLAYER_1_2_RECORD_DRAWS = [
    0,
    0,
    1,
    1
]
EXPECTED_GAME_WINNER = [
    PLAYER_2_NAME,
    PLAYER_1_NAME,
    '',
    ''
]

# Combine lists to form a 3-tuple object, for parameterize compatibility
# For test_get_game_result() function
GAME_RESULTS_ARGS = zip(
    PLAYER_1_GAME_SCORES,
    PLAYER_2_GAME_SCORES,
    PLAYER_1_RECORD_WINS,
    PLAYER_2_RECORD_WINS,
    PLAYER_1_2_RECORD_DRAWS,
    EXPECTED_GAME_WINNER
)


# Get random play list
def get_random_play_inputs() -> list:
    """ Create a list of random plays for test usage/consumption.

        Args:
            None.

        Returns:
            plays (list): list of player plays
    """

    # Instantiate object from UltimateRPS
    ultimate_rps = UltimateRPS()

    # Create a list of plays
    play_choices = list(ultimate_rps.battle_table[0].keys())
    play_choices.remove('Attacker')

    # Create a blank list for random plays
    plays = []

    # Create random plays NUMBER_OF_PLAYERS times
    for _ in range(NUMBER_OF_PLAYERS):

        # Add enough valid random plays for each player, plus two invalid plays
        for _ in range(NUMBER_OF_PLAYS):

            # Choose a random number between 1 and the length of the plays list
            play_input_number = randint(1, len(play_choices))
            plays.append(str(play_input_number))

        # Add an invalid play after each players valid plays
        plays.append(len(play_choices) + 1)

    return plays


# pytest fixtures
@fixture
def ultimate_rps_object():
    """ pytest figture to instantiate a full UltimateRPS object.

        Args:
            None.

        Returns:
            ultimate_rps (class UltimateRPS): Ultimate Rock, Paper, Scissors,
                                              game object.
    """
    ultimate_rps = UltimateRPS()

    return ultimate_rps


@fixture
def battle_table(ultimate_rps_object):
    """ pytest fixture to read data from the CSV file with
        the 'battle-table.csv' matrix.

        Args:
            ultimate_rps_object (class UltimateRPS): Ultimate Rock, Paper,
                                                     Scissors game object.

        Returns:
            battle_table (list): Ultimate Rock, Paper, Scissors
                                 UltimateRPS.battle_table game object.
    """

    battle_table = ultimate_rps_object.battle_table

    return battle_table


@fixture
def player_objects():
    """ pytest fixture to instantiate multiple Player objects.

        Args:
            None.

        Returns:
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.
    """

    # Create namedtuple object to store test player object data
    PlayerObjects = namedtuple('PlayerObjects', 'player_1 player_2')

    # Instantiate Players object for player_1 and player_2
    player_objects = PlayerObjects(
        player_1=Player(name=PLAYER_1_NAME),
        player_2=Player()
    )

    return player_objects


# pytest tests
def test_display_banner(capfd):
    """ Test the output of the display_banner function. The test value
        'BANNER_OUTPUT' should be in the text printed to STDOUT.

        Args:
            capfd (pytest fixture): pytest capture fixture for STDOUT and
                                    STDERR output.

        Returns:
            None.
    """

    # Call the display_banner function
    display_banner()

    # Read the output from the capfd fixture
    output = capfd.readouterr()[0]

    # Test for expected output
    assert BANNER_OUTPUT in output


@patch(
    'builtins.input',
    side_effect=[
        PLAYER_1_NAME,
        '',
        '',
        ''
    ]
)
def test_get_player_1_name(name):
    """ Test for player 1 name input. Assert that the input string for
        player 1 returns and raise a ValueError if the player 1 name
        is blank.

        Args:
            name (MagicMock): Placeholder variable for side_effect values.
                Note: The test for a blank name ('') repeats 3 x times to
                      account for 3 x attempts to collect a valid name.

        Returns:
            None.
    """

    # Test for non-blank input
    assert get_player_1_name() == PLAYER_1_NAME

    # Test for blank input
    with raises(UltimateRPSExceptions.MaxRetriesExceeded):
        get_player_1_name()


@patch(
    'builtins.input',
    side_effect=[
        PLAYER_2_NAME,
        ''
    ]
)
def test_get_player_2_name(name):
    """ Test for player 2 name input. Assert that the input for player 2
        returns or, if the input is blank, returns the name 'Computer'.

        Args:
            name (MagicMock): Placeholder variable for side_effect values.

        Returns:
            None.
    """

    # Test for non-blank input
    assert get_player_2_name() == PLAYER_2_NAME

    # Test for blank input
    assert get_player_2_name() == PLAYER_2_NAME


def test_display_matchup(capfd, player_objects):
    """ Test the output of the display_matchup function. The test value
        'MATCHUP_OUTPUT_REGEX' should be in the text printed to STDOUT.

        Args:
            capfd (pytest fixture): pytest capture fixture for STDOUT and
                                    STDERR output.
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returns:
            None.
    """

    # Call the display_matchup function
    display_matchup(
        player_1=player_objects.player_1,
        player_2=player_objects.player_2
    )

    # Read the output from the capfd fixture and strip leading/trailing space
    output = capfd.readouterr()[0].strip()

    # Regex search the output with the MATCHUP_OUTPUT_REGEX pattern
    assert MATCHUP_OUTPUT_REGEX.search(output).group(0)


@patch(
    'builtins.input',
    side_effect=get_random_play_inputs()
)
def test_get_player_play(
    play,
    ultimate_rps_object,
    player_objects
):
    """ Test Player objects for the correct values, after a complete turn.
        The player play must be found in the UltimateRPS.battle_table.

        Args:
            play: (MagicMock): Placeholder variable for side_effect values.
            ultimate_rps_object (class UltimateRPS): Ultimate Rock, Paper,
                                                     Scissors game object.
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returns:
            None.
    """

    # Assign player objects to short variables
    player_1 = player_objects.player_1
    player_2 = player_objects.player_2

    """ Repeat all assertions NUMBER_OF_PLAYS times for each player,
        to match the total number of side_effect iterations.
    """

    # Player 1 plays
    # Assert the player 1 play is in the battle_table and is not 'Attacker'
    player_1 = get_player_play(player=player_1)
    assert player_1.plays[-1] in ultimate_rps_object.battle_table[0] and \
        player_1.plays[-1] != 'Attacker'

    # Repeat the same function call, in order to get a new side_effect value
    player_1 = get_player_play(player=player_1)
    assert player_1.plays[-1] in ultimate_rps_object.battle_table[0] and \
        player_1.plays[-1] != 'Attacker'

    # Repeat the same function call, in order to get a new side_effect value
    player_1 = get_player_play(player=player_1)
    assert player_1.plays[-1] in ultimate_rps_object.battle_table[0] and \
        player_1.plays[-1] != 'Attacker'

    with raises(IndexError):
        player_1 = get_player_play(player=player_1)

    # Player 2 plays
    # Assert the player 2 play is in the battle_table and is not 'Attacker'
    player_2 = get_player_play(player=player_2)
    assert player_2.plays[-1] in ultimate_rps_object.battle_table[0] and \
        player_2.plays[-1] != 'Attacker'

    # Repeat the same function call, in order to get a new side_effect value
    player_2 = get_player_play(player=player_2)
    assert player_2.plays[-1] in ultimate_rps_object.battle_table[0] and \
        player_2.plays[-1] != 'Attacker'

    # Repeat the same function call, in order to get a new side_effect value
    player_2 = get_player_play(player=player_2)
    assert player_2.plays[-1] in ultimate_rps_object.battle_table[0] and \
        player_2.plays[-1] != 'Attacker'

    with raises(IndexError):
        player_2 = get_player_play(player=player_1)


@mark.parametrize(
    'player_1_play, player_2_play, expected_result',
    list(GAMEPLAY_ARGS_1)
)
def test_get_play_result(
    player_1_play,
    player_2_play,
    expected_result,
    player_objects
):
    """ Test to determine the result of a play by each player, and increment
        the score after each play.  Assert that the function under test
        returns the expected results.

        Args:
            player_1_play (str):
                Player 1's play choice (e.g. 'Rock').
            player_2_play (str):
                Player 2's play choice (e.g. 'Scissors').
            expected_result (str):
                Expected player result for the matchup against Player 2's
                play (e.g. 'Win').
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returns:
            None.
    """

    # Extract players from player_object
    player_1 = player_objects.player_1
    player_2 = player_objects.player_2

    # Assign plays to each player
    player_1.plays.append(player_1_play)
    player_2.plays.append(player_2_play)

    # Test plays against expected results
    play_result = get_play_result(
        player_1=player_1,
        player_2=player_2
    )

    assert play_result.player_1_result == expected_result


@mark.parametrize(
    'player_1_score, player_2_score, player_1_record_wins, '
    'player_2_record_wins, player_1_2_record_draws, expected_game_winner',
    list(GAME_RESULTS_ARGS)
)
def test_get_game_result(
    player_1_score,
    player_2_score,
    player_1_record_wins,
    player_2_record_wins,
    player_1_2_record_draws,
    expected_game_winner,
    player_objects
):
    """ Test to determine the result of a game by each player, incrementing
        the score after each play.

        Args:
            player_1_score (int):
                Player 1's tally of wins in a game.
            player_2_score (int):
                Player 2's tally of wins in a game.
            player_1_record_wins (int):
                Player 1's record after the game completes.
            player_2_record_wins (int):
                Player 2's record after the game completes.
            player_1_2_record_draws (int):
                Record of player_1/player_2 draws, after the game completes.
            expected_game_winner (str):
                Expected winning player player's name.
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returns:
            None.
    """

    # Extract players from player_object
    player_1 = player_objects.player_1
    player_2 = player_objects.player_2

    # Set mock Player object attribute values
    player_1.score = player_1_score
    player_2.score = player_2_score

    # Setup a result object to store the response
    result = get_game_result(
        player_1=player_1,
        player_2=player_2
    )

    # Assert the result values match expected values
    # Response objects are in the result and of the correct type/class
    assert type(result.player_1) == Player and \
           type(result.player_2) == Player and \
           type(result.winner) == str

    # Response values match expected results
    assert result.player_1.record.wins == player_1_record_wins and \
           result.player_1.record.losses == player_2_record_wins and \
           result.player_2.record.wins == player_2_record_wins and \
           result.player_2.record.losses == player_1_record_wins and \
           result.player_1.record.draws == player_1_2_record_draws and \
           result.player_2.record.draws == player_1_2_record_draws and \
           result.winner == expected_game_winner


def test_game_loop(
    ultimate_rps_object,
    player_objects
):
    """ Test the game_loop function for proper functionality.

        Args:
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.
            ultimate_rps_object (class UltimateRPS): Ultimate Rock, Paper,
                                                     Scissors game object.
    """

    pass


def test_import_csv_type(battle_table):
    """ Test the Python object with the CSV data and assert the
        object type is a list.

        Args:
            battle_table (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    assert type(battle_table) == list


def test_import_csv_len(battle_table):
    """ Test the Python object with the CSV data and assert the
       list length is greater than zero.

        Args:
            battle_table (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    assert len(battle_table) > 0


def test_import_csv_sub_type(battle_table):
    """ Test the Python object with the CSV data and assert that the
        object type for a randomly-chosen list item is a dict.

        Args:
            csv_data (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    data_len = len(battle_table)
    rand_index = randint(0, data_len) - 1
    assert type(battle_table[rand_index]) == dict


@mark.parametrize(
    'player_1_play, player_2_play, expected_result',
    list(GAMEPLAY_ARGS_2)
)
def test_play_result(
    ultimate_rps_object,
    player_1_play,
    player_2_play,
    expected_result
):
    """ Test the result of a single game play (turn) to determine the
        result of the player_1 play vs the player_2 play

        Args:
            ultimate_rps_object (class UltimateRPS): Ultimate Rock, Paper,
                                                     Scissors game object.
            player_1_play (str):
                Player 1's play choice (e.g. 'Rock').
            player_2_play (str):
                Player 2's play choice (e.g. 'Scissors').
            expected_result (str):
                Expected player result for the matchup against Player 2's
                play (e.g. 'Win').

        Returns:
            None.
    """

    # Call the 'get_turn_result' function with parameterized play arguments
    turn_result = ultimate_rps_object.get_turn_result(
            player_1_play=player_1_play,
            player_2_play=player_2_play
        )

    # Compare the result of the function call to the parameterized turn_result
    assert turn_result == expected_result


def test_player_instantion(player_objects):
    """ Test the Player class in UltimateRPS for the ability to instantiate
        Player objects. player_2 should receive the default name of 'Computer',
        having no name argument value passed to the method in the
        'player_objects' fixture.

        Args:
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returs:
            None.
    """

    assert type(player_objects.player_1) == Player
    assert player_objects.player_1.name == PLAYER_1_NAME
    assert type(player_objects.player_2) == Player
    assert player_objects.player_2.name == PLAYER_2_NAME


def test_instantiated_player_attributes(player_objects):
    """ Test the Player class in UltimateRPS for the correct Player objects
        attribute default values

        Args:
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returs:
            None.
    """

    assert player_objects.player_1.score == 0
    assert player_objects.player_1.plays == []
    assert player_objects.player_1.record.wins == 0
    assert player_objects.player_1.record.losses == 0
