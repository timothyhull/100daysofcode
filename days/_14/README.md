## :calendar: Day 14: 6/23/21-7/2/21

---

## Topics:

:clipboard: Text-based Games Challenges (and `class` objects)

---

## Resources:

:star: TBD

---

## Tasks:

:white_check_mark: Build functional rock, paper, scissors game

:white_check_mark: Use `pytest` for TDD of game.

---

## Notes:

#### :notebook:6/22/21

- Watched videos 7-9
- Built foundations for rock, paper, scissors game at [rock_paper_scissors](rock_paper_scissors/rock_paper_scissors.py).

---

#### :notebook:6/23/21

- Built out initial `class` objects for `Roll` and `Players`

```python
#!/usr/bin/env python3
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

---

#### :notebook: 6/28/21

- Started development of the `game_loop` function within , [rock_paper_scissors.py](rock_paper_scissors/rock_paper_scissors.py).
  - Built initial loop functionality, random choice of player #2 (computer) rolls, and basic input validation.
- Developed initial `assert` statement for TDD-based test, `test_game_loop` within the existing test file, [test_rock_paper_scissors.py](test/test_rock_paper_scissors.py)

---

#### :notebook: 6/29/21

- Added outline for the portion of the `game_loop` function which will determine which player roll wins
  - Need to review and possibly revise the `class` structure to account for the current program flow.

---

#### :notebook: 6/30/21

- Completed initial **functional** game, after reviewing `class` structure.
  - Need to revise formatting for a smoother game play experience.

---

#### :notebook: 7/1/21

- Successfully re-tested game for functionality.
- Removed variable assignment from the call of the `game_loop` function.
- Established framework for `pytest` tests of `game_loop` with `unittest.mock.patch`.
  - Built `side_effect` list to supply random values for testing player input selections.
  - `pytest` test passes at this time.

```python
root@4e75680cdf7d:/workspaces/100daysofcode/days/_14/tests# pytest -sv
==================================================== test session starts ====================================================
platform linux -- Python 3.9.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/100daysofcode/days/_14/tests
plugins: cov-2.12.1, anyio-3.2.1
collected 3 items                                                                                                           

test_rock_paper_scissors.py::test_display_banner 
** Let's Play Rock, Paper, Scissors **
--------------------------------------



** Test Message **
------------------


PASSED
test_rock_paper_scissors.py::test_get_player_name PASSED
test_rock_paper_scissors.py::test_game_loop 
Round 1 of 3
------------
Tim: 0	Computer: 0

Choices:
1. Paper
2. Rock
3. Scissors

** Tim chooses scissors
** Computer chooses paper

Round 2 of 3
------------
Tim: 0	Computer: 1

Choices:
1. Paper
2. Rock
3. Scissors

** Tim chooses rock
** Computer chooses scissors

Round 3 of 3
------------
Tim: 0	Computer: 2

Choices:
1. Paper
2. Rock
3. Scissors

** Tim chooses paper
** Computer chooses paper

** This round is is a tie **

** Final Score **

Tim: 0	Computer: 2


 ** Computer wins **

PASSED

===================================================== 3 passed in 0.06s =====================================================

```

---

#### **:notebook: 7/2/21**

- Corrected logic issue in round winner determination

```python
# Replaced this line:
if player_1.roll.name == player_2.roll.win:

# With this line
if player_1.roll.name == player_2.roll.lose:
```

