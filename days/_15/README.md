## :calendar: Day 15: 7/2/21-7/6/21

---

## Topics:

:clipboard: Expand the Rock, Paper, Scissors game

---

## Resources:

:star: TBD

---

## Tasks:

:white_check_mark: Create initial program framework

:white_check_mark: Create initial `pytest` framework

:white_check_mark: Import CSV [file data](ultimate_rps/data/battle-table.csv)

:white_check_mark: Search CSV data for win/loss results, based on attacker

:white_check_mark: Add docstring and comments to `test_play_result()` function in `test_ultimate_rps.py`

:white_check_mark: Refactor `test_play_result()` function in `test_ultimate_rps.py` to include mock tests input values, via the `pytest.mark.parameterize` method.

:white_large_square: ​Create `class` objects for player properties

:white_large_square: Create game loop which allows for interactive input and score feedback 

---

## Notes:

#### :notebook: 7/2/21

- Created initial program framework, [ultimate_rps.py](ultimate_rps/ultimate_rps.py)
- Created initial `pytest` framework, [test_ultimate_rps.py](ultimate_rps/tests/test_ultimate_rps.py)

---

#### :notebook: 7/3/21

- Worked with the `csv` module, to import and understand resulting object (a `list` with nested `list` objects for each line in the CSV).

---

#### :notebook: 7/4/21

- Expanded `pytest` functionality to separate assertions into their own functions.
  - Added docstings to each `pytest` function.
- Added `pytest` `fixture` (`csv_data`) to retreive the CSV data from the [battle-table.csv](data/battle-table.csv) matrix.

```python
from pytest import fixture

@fixture
def csv_data():
    """ pytest fixture to read data from the CSV file with
        the 'battle-table.csv' matrix.

        Args:
            None.

        Returns:
            data (list): List of dictionaries with CSV file rows.
    """

    data = import_csv()

    return data
 
def test_import_csv_type(csv_data):
    """ Test the Python object with the CSV data and assert the
        object type is a list.

        Args:
            csv_data (list): pytest fixture of CSV data.

        Returns:
            None.
    """

    assert type(csv_data) == list
```

- Initial testing with searching the CSV data for the correct attacker/result data (e.g. when attacker is 'Rock',  it beats 'X' but loses to 'Y'.

---

#### :notebook: 7/5/21

- Refactored [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py) such that CSV import functionality is now a component of a new `class` within the file [`UltimateRPS.py`](ultimate_rps/UltimateRPS.py).
  - The `class` name is `UltimateRPS`.
- Added TDD function to determine the outcome of a turn/play:
  - Need to add docstring and comments
  - Need to refactor for `mock.patch` `side_effect` input values.

```python
def test_play_result():
    ultimate_rps = UltimateRPS()
    player_play = 'Scissors'
    computer_play = 'Rock'

    turn_result = ultimate_rps.get_turn_result(
            player_play=player_play,
            computer_play=computer_play
        )
    assert turn_result == 'win'
```

- Build function within the `UltimateRPS` `class` to fufill the test criterial of `test_play_results`.
  - The function is `get_turn_result`

```python
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
```

---

#### :notebook: 7/6/21

- Refactored [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py) to implement static player and computer input values, using `pytest.mark.parameterize`.
  - Used the `zip()` function to create a `tuple` of iterables (`player_play`, `computer_play`, `expected_result`) to pass to the `pytest.mark.parameterize` decorator.
  - Enclosed the `zip` object type in a `list()` function, in order to pass an iterable object (`list` of tuples) to the decorator:

```python
@mark.parametrize(
    'player_play, computer_play, expected_result',
    list(GAMEPLAY_ARGS)
)
def test_play_result(
    ultimate_rps_object,
    player_play,
    computer_play,
    expected_result
):
  # Function details omitted for brevity
```

- Added docstring to `test_play_result()` function in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py).
- Refactored [`UltimateRPS.py`](ultimate_rps/UltimateRPS.py) `get_turn_result()` method to simplify return functionality.
  - Added detailed documentation for specific steps in the method.

