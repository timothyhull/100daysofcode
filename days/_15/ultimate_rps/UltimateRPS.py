#!/usr/bin/env python3
""" Class objects for Ultimate Rock, Paper, Scissors (Ultimate RPS) game.
"""

# Imports
from csv import DictReader

# Constants
CSV_FILE = 'data/battle-table.csv'


class UltimateRPS:
    """ Class objects for Ultimate Rock, Paper, Scissors (Ultimate RPS) game.
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
        player_play: str,
        computer_play: str
    ) -> str:
        """ Determine the winner of a given turn.

            Args:
                player_play (str): Player-chosen gameplay article
                                   (e.g, "Scissors")
                computer_play (str): Randomly-chosen gameplay article
                                     (e.g, "Rock")

            Returns:
                play_result (str): Result of play determination, based on
                                   the battle table (win, lose, or draw).
        """

        # Add titlecase player and computer plays to 'self'
        self.player_play = player_play.title()
        self.computer_play = computer_play.title()

        # Loop over battle table and locate player_play value for 'Attacker'
        for player_row in self.battle_table:

            # Look for the row with the 'Attacker' that matches 'player_play'
            if player_row.get('Attacker') == self.player_play:

                """ Get the value for the key in the player_row that matches
                    the computer_play value.

                    Details:
                        When the loop iteration row (dict) has an 'Attacker'
                        key with a value that matches 'player_play', within
                        that same row (dict), get the value for the key that
                        matches 'computer_play'.  The value of the matching
                        key will yield the result of the computer's play
                        against the player's play.

                    Example:
                        self.player_play = 'Scissors'
                        self.computer_play = 'Rock'
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

                        The key that matches 'self.computer_play' is 'Rock'
                        which has a value of 'lose'.  This means that
                        'self.player_play' (Scissors) loses to
                        'self.computer_play' (Rock).
                """
                player_play_result = player_row.get(self.computer_play)

                # Halt loop iteration after match and return player_play_result
                return player_play_result
