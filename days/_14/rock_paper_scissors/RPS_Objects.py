#!/usr/bin/env/python3
""" Game objects for Paper, Rock, Scissors.
"""

# Imports

# Constants
OBJECTS = {
    'rock': {
        'win': 'scissors',
        'lose': 'paper'
    },
    'paper': {
        'win': 'rock',
        'lose': 'scissors'
    },
    'scissors': {
        'win': 'paper',
        'lose': 'rock'
    }
}


class Roll:
    """ Set the attributes for a roll.

        Args:
            name (str): 'rock', 'paper', or 'scissors'
    """
    def __init__(self, name: str) -> None:
        # Verify the name is valid
        if name.lower() in OBJECTS.keys():
            self.name = name.lower()

            # Get the result of a roll with the named object
            self.get_roll_result()

        # For an invalid name, display an error with usage information
        else:

            # Determine if the number of objects is greater than one
            if len(OBJECTS.keys()) > 1:

                # Build formatted string of objects to display in a ValueError
                object_choices = ''
                for object in OBJECTS.keys():

                    # Determine if the current object is the last in the list
                    if object != list(OBJECTS.keys())[-1]:
                        object_choices += f'"{object}", '
                    else:
                        object_choices += f'or "{object}"'

            # For object lists with a length of one, set the formatted string
            else:
                object_choices = OBJECTS.keys()[0]

            # Raise a value error with a formatted string message
            raise ValueError(f'Name must be one of {object_choices}.')

    def get_roll_result(self):
        """ Set the 'win' and 'lose attributes for the current roll.
        """
        self.win = OBJECTS[self.name].get('win')
        self.lose = OBJECTS[self.name].get('lose')


class Player:
    """ Set the attributes for a player.
    """
    def __init__(
        self,
        name: str = 'Computer',
        roll: str = None
    ) -> None:
        self.name = name
        self.roll = roll
