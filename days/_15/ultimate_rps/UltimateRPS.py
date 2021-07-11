#!/usr/bin/env python3
""" Class objects for Ultimate Rock, Paper, Scissors (Ultimate RPS) game.
"""

# Imports
from collections import namedtuple
from csv import DictReader

# Constants
CSV_FILE = 'data/battle-table.csv'


class UltimateRPS:
    """ Class objects for Ultimate Rock, Paper, Scissors (Ultimate RPS)
        gameplay.

        Args:
            None.

        Returns:
            self (UltimateRPS): UltimateRPS object with populated
            'battle_table' attribute.
    """

    def __init__(self):

        # Import the CSV battle table data
        self.battle_table = self.import_battle_table()

    def import_battle_table(self, file: str = CSV_FILE) -> list:
        """ Read data from the CSV file with the 'battle-table.csv' matrix.

            Args:
                file (str): Path to CSV file, default is CSV_FILE.

            Returns:
                battle_table (list): List of dictionaries with CSV file rows.
        """
        with open(
            file=file,
            mode='rt',
            encoding='utf-8'
        ) as csv_data:
            csv_reader = DictReader(csv_data)
            battle_table = list(csv_reader)

        return battle_table

    def get_turn_result(
        self,
        player_1_play: str,
        player_2_play: str
    ) -> str:
        """ Determine the winner of a given turn.

            Args:
                player_1_play (str): Player 1's chosen gameplay article
                                   (e.g, "Scissors")
                player_2_play (str): Player 2's gameplay article
                                     (e.g, "Rock")

            Returns:
                play_result (str): Result of play determination, based on
                                   the battle table (win, lose, or draw).
        """

        # Add titlecase player_1_play and player_2_play to 'self'
        self.player_1_play = player_1_play.title()
        self.player_2_play = player_2_play.title()

        # Loop over battle table and locate player_1_play value for 'Attacker'
        for player_row in self.battle_table:

            # Look for the row with the 'Attacker' that matches 'player_1_play'
            if player_row.get('Attacker') == self.player_1_play:

                """ Get the value for the key in the player_row that matches
                    the player_2_play value.

                    Details:
                        When the loop iteration row (dict) has an 'Attacker'
                        key with a value that matches 'player_1_play', within
                        that same row (dict), get the value for the key that
                        matches 'player_2_play'.  The value of the matching
                        key will yield the result of the computer's play
                        against the player's play.

                    Example:
                        self.player_1_play = 'Scissors'
                        self.player_2_play = 'Rock'
                        battle_table row with an attacker of 'Scissors':
                            {'Air': 'win',
                             'Attacker': 'Scissors',
                             'Devil': 'lose',
                             'Dragon': 'lose',
                             'Fire': 'lose',
                             'Gun': 'lose',
                             'Human': 'win',
                             'Lightning': 'lose',
                             'Paper': 'win',
                             'Rock': 'lose',
                             'Scissors': 'draw',
                             'Snake': 'win',
                             'Sponge': 'win',
                             'Tree': 'win',
                             'Water': 'lose',
                             'Wolf': 'win'}

                        The key that matches 'self.player_2_play' is 'Rock'
                        which has a value of 'lose'.  This means that
                        'self.player_1_play' (Scissors) loses to
                        'self.player_2_play' (Rock).
                """
                player_1_play_result = player_row.get(self.player_2_play)

                # Halt loop after match and return player_1_play_result
                return player_1_play_result


class Player:
    """ Class objects for Ultimate Rock, Paper, Scissors (Ultimate RPS)
        gameplay.

        Args:
            name (str): Player's name, default value is 'Computer'.

        Returns:
            self (Player): Player object with default values.
    """

    def __init__(self, name: str = 'Computer'):

        # namedtuple to store wins and losses count
        Record = namedtuple('Record', 'wins losses')

        # Define initial attribute values
        self.name = name
        self.plays = []
        self.score = 0
        self.record = Record(0, 0)


class MaxRetriesExceeded(Exception):

    def __init__(
        self,
        max_retries: int = 'undefined',
        message: str = 'Exceeded the maximum number of retries'
    ):
        self.max_retries = max_retries
        self.message = f'{message} ({max_retries}).'
        super().__init__(self.message)
