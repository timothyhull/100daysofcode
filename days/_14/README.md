## :calendar: Day 14: 6/23/21-6/27/21

---

## Topics:

:clipboard: Text-based Games Challenges (and `class` objects)

---

## Resources:

:star: TBD

---

## Tasks:

:white_large_square: Build functional rock, paper, scissors game

:white_large_square: Use `pytest` for TDD of game.

:white_large_square: Build 15-way for rock, paper, scissors, etc. game

:white_large_square: TBD

---

## Notes:

#### :notebook:6/22/21

- Watched videos 7-9
- Built foundations for rock, paper, scissors game at [rock_paper_scissors](rock_paper_scissors/rock_paper_scissors.py).

---

#### :notebook:6/23/21

- Built out initial `class` objects for `Roll` and `Players`

```python
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
        if name in OBJECTS.keys():
            self.name = name

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

            # Raise a value error
            raise ValueError(f'Name must be one of {object_choices}.')

    def get_roll_result(self):
        """ Set the 'win' and 'lose attributes for the current roll.
        """
        self.win = OBJECTS[self.name].get('win')
        self.lose = OBJECTS[self.name].get('lose')


class Player:
    """ Set the attributes for a player.
    """
    def __init__(self, name: str = 'Computer') -> None:
        self.name = name

```



- Tested functionality with the following REPL commands:

```python
from RPS_Objects import Roll

# Example with a good name value
roll_1 = Roll('rock')
roll_1.name  # returns 'rock'
roll_1.win  # returns 'scissors'
roll_1.lose  # returns 'paper'

# Example with a bad name value
roll_2 = Roll('bad_name')  # raises a ValueError with a custom string
```

---

#### :notebook: 6/24/21

- Created `pytest` tests to support TDD of game functions.
  - Wrote tests for `display_banner()` and `get_player_name()` functions.
  - Used `unittest.mock.patch()` to mock end user STDIN inpu for `get_player_name()`t, with multiple `side_effect` values.
    - Tested for both a valid `return` value and for a `ValueError` exception for an invalid entry (using `pytest.raises(ValueError)`).
  - Used the `capfd` fixture to test for valid text printed to STDOUT.

---

#### :notebook: 6/25/21

- Reviewed `pytest` tests.
- Expanded `main()` function to include initial creation of rolls (using the imported Roll class).

---

#### :notebook: 6/26/21

- Performed troubleshooting on failing `pytest` tests, due to the error `ModuleNotFoundError: No module named 'RPS_Objects'.`
  - Modified the import command in [`rock_paper_scissors.py`](rock_paper_scissors/rock_paper_scissors.py) to match the correct command:

```python
# Old command
from _RPS_Objects import Roll, Player

# New command
from _14.rock_paper_scissors.RPS_Objects import Roll, Player
```

---

#### :notebook: 6/27/21

- Created TDD-based test, `test_game_loop` within the existing test file, [test_rock_paper_scissors.py](test/test_rock_paper_scissors.py)
- Created initial structure and docstring for the `game_loop` function.
