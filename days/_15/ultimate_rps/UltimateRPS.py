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
                                   (e.g, "scissors")
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

            # Look for the row with the 'Attacker' that matches player_play
            if player_row.get('Attacker') == self.player_play:
                player_play_result = player_row

                # Stop loop iteration after match
                break

        # Determine if the player_play beats the computer_play
        if player_play_result.get(self.computer_play) == 'lose':
            play_result = 'win'
        elif player_play_result.get(self.computer_play) == 'win':
            play_result = 'lose'
        elif player_play_result.get(self.computer_play) == 'draw':
            play_result = 'draw'

        return play_result
