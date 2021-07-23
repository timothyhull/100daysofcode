## :calendar: Day 15: 7/2/21-7/21/21

---

## Topics:

:clipboard: Expand the Rock, Paper, Scissors game

---

## Resources:

:star: Defining [custom Exception objects](https://www.programiz.com/python-programming/user-defined-exception)

---

## Tasks:

:white_check_mark: Create initial program framework

:white_check_mark: Create initial `pytest` framework

:white_check_mark: Import CSV [file data](ultimate_rps/data/battle-table.csv)

:white_check_mark: Search CSV data for win/loss results, based on attacker

:white_check_mark: Add docstring and comments to `test_play_result()` function in `test_ultimate_rps.py`

:white_check_mark: Refactor `test_play_result()` function in `test_ultimate_rps.py` to include mock tests input values, via the `pytest.mark.parameterize` method.

:white_check_mark: Create `class` objects for player properties

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

---

**:notebook: 7/7/21**

- Added TDD functions to validate the instantion objects of the  `Player` `class`.
  - Includes a new `fixture` to instantiate two `Player` objects.
  - Returns a `namedtuple` object with attributes which each contain one the `Player` objects.

```python
@fixture
def player_objects():
    """ pytest fixture to instantiate Player objects.

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
 

def test_player_instantion(player_objects):
    """ Test the ability to instantiate Player objects.

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
    """ Test for the correct Player objects attribute default values

        Args:
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returs:
            None.
    """

    assert player_objects.player_1.score == 0
    # assert type(player_objects.player_1.plays) == list
    assert player_objects.player_1.plays == []
    assert player_objects.player_1.record.wins == 0
    assert player_objects.player_1.record.losses == 0
```



- Created `Player` `class` in [`UltimateRPS.py`](ultimate_rps/UltimateRPS.py).
  - All tests passing.

```python
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
```

---

#### :notebook: 7/8/21

- Built framework for functions to support game loop in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py).
- Completed test construction for the `display_banner()` function in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py), using the `test_display_banner` function in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py).
  - Started test construction for the `get_player_name()` function in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py), using the `test_get_player_name()` function in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py).

---

#### :notebook: 7/9/21

- Refactored `get_player_name()` function in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py) to a `setup_players()` function which creates player objects based on name values passed as arguments.
  - The intent is to provide the function a set of names gathered from input in the game loop.
- Unable to successfuly complete tests of the `setup_players()` function due to the need to pass multiple arguments to the function.
  - Does not appear possible with the `side_effect` parameter of the `unittest.mock.patch` method.
  - Testing with the `unittest.mock.patch.multiple` method.
  - The correct methodology may be to use the `pytest.mark.parameterize` method.

---

#### :notebook: 7/10/21

- Successfully implemented the following `pytest` tests in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py):
  - `test_get_player_1_name()`
    - Tests for valid player 1 name input.
    - Wrote custom `Exception` `class` named `MaxRetriesExceeded` to implement a proper exception after N failed attempts at correct name input:
  
  ```python
  class MaxRetriesExceeded(Exception):
  
      def __init__(
          self,
          max_retries: int = 'undefined',
          message: str = 'Exceeded the maximum number of retries'
      ):
          self.max_retries = max_retries
          self.message = f'{message} ({max_retries}).'
          super().__init__(self.message)
  ```
  
  - `test_get_player_2_name()`
    - Tests for valid player 2 name input or default input ('Computer')
  - `test_display_matchup()`
    - Tests for valid display of matchup details (names and win/loss records) with a **regex** pattern
```shell
# String to match
** Test (0-0) vs Computer (0-0) **
```

```python
# regex pattern
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
```

- Successfully implemented the following functions in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py):
  - `get_player_1_name()`
    - Collects a valid name for player 1 or raises a `MaxRetriesExceeded` `Exception`.
  - `get_player_2_name()`
    - Collects a valid name for player 1 or uses a default name of 'Computer'.
  - `display_matchup()`
    - Displays matchup details (names and win/loss records).
- Refactored `main()` function for cleanliness and brevity.
- All `pytest` tests pass.

---

#### :notebook: 7/11/21

- Setup `test_get_player_play()` function in  [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py) to test the following:
  - Create a game instance
  - Gather Player 1 play input
  - Gather Player 2 play input
  - Determine play winner
  - Determine game winner (best of N)
  - Increment player records

---

#### :notebook: 7/12/21

- Wrote custom `Exception` `class` named `UltimateRPSExceptions` and texted the sub-classes:
  - `MaxRetriesExceeded` (existing `class`)
  - `InvalidPlaySelection` (new `class`)
- Expanded `test_get_player_play()` function in  [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py) to encompass testing using an `@patch` function (to mock user input)
  - Successfully mocked test although writing code to pass the test is still required.
    - The current function under test simply has a `pass` command and will fail tests if not modified to return an explicit value, like 'Rock'.

---

#### :notebook: 7/13/21

- Expanded `test_get_player_play()` function in  [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py).
  - Created `get_random_plays()` function to produce a random list of plays to use as @patch values for input.
  - Modified `test_get_player_play()` function to include the random list of plays.
    - **It does not appear all of the side_effect items are being tested.**
- Added basic functionality to get_player_play() in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py):
  - Create a list of available plays and display that list with prefixed numbers (e.g. 1. Rock)
  - Added function to collect numeric input from player, to choose a play.
    - **No data validation in place at this time**

---

#### :notebook: 7/14/21

- Conducted extensive troubleshooting to determine why the a `list` of three `side_effect` values would only have the first value run.
  - Determined the root cause, only a function call triggers the `next()` method and iterates over the mock input values.
  - A single function call that assigns results to a variable only iterates over the first value in the `side_effect_list`.
  - Corrected as follows:

```python
@patch(
    'builtins.input',
    side_effect=get_random_plays()
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
    # player_2 = player_objects.player_2

    # Repeat all assertions NUMBER_OF_PLAYS times, matching side_effect count

    # Assert the player 1 play is in the battle_table and is not 'Attacker'
    player_1_play = get_player_play(player=player_1)
    assert player_1_play in ultimate_rps_object.battle_table[0] and \
        player_1_play != 'Attacker'

    # Repeat the same function call, in order to get a new side_effect value
    player_1_play = get_player_play(player=player_1)
    assert player_1_play in ultimate_rps_object.battle_table[0] and \
        player_1_play != 'Attacker'

    # Repeat the same function call, in order to get a new side_effect value
    player_1_play = get_player_play(player=player_1)
    assert player_1_play in ultimate_rps_object.battle_table[0] and \
        player_1_play != 'Attacker'
```

---

#### :notebook: 7/15/21

- Completed `test_get_player_play()` function.
  - Includes the following asserts for each player:
    - 3 x valid tests
    - 1 x invalid test (testing supported by raising an `IndexError`)
  - Refactored `get_random_plays()` to `get_random_play_inputs()` in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py).
    - To support automatically choosing random play inputs, both valid and invalid.
  - Refactored to add play choices to the `Player` object `plays` `list` (instead of returning a string of the play)
    - Refactored `test_get_player_play()` function in[`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py) and `get_player_play()` function in[`ultimate_rps.py`](ultimate_rps/ultimate_rps.py) and 

```python
get_random_play_inputs() -> list:
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
            plays.append(play_input_number)
            print(plays)

        # Add an invalid play after each players valid plays
        plays.append(len(play_choices) + 1)
        print(plays)

    return plays
```

```python
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
    print(get_random_play_inputs())
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
```

```python
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
```

---

#### :notebook: 7/16/21

- Developed framework for `test_get_play_result()` function in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py).
    - Created `@mark.parameterized` Configuration to support testing.
    
---

#### :notebook: 7/17/21

- Expanded framework for `test_get_play_result()` function in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py).
    - Successfully passing the `test_get_play_result()` test although it appears `@mark.parameterized` may only work once in a test file, when using the same source data for parameters.
    - Need to conduct testing to validate and correct.
- Developed function `get_play_result()` function in in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py).
    - Returns valid data.

---

#### :notebook: 7/18/21

 - Confirmed that `@mark.parameterized` only works once in a test file, when using the same source data for parameters.
    - Added a second `zip()` object, to supply a separate set of source data for each instance of `@mark.parameterize`.
        - `GAMEPLAY_ARGS_1` for `test_get_play_result()`
        - `GAMEPLAY_ARGS_2` for `test_play_result()`
- Revised function `get_play_result()` function in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py) to return a `namedtuple` object which contains both `Player` objects plus text which indicates the outcome of the play, for `player_1`.
- Revised `test_get_play_result()` function in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py) to accomodate new return object, from `get_play_result()`.

All tests passing:

```python
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

    # Set the turn results
    play_result = PlayResult(player_1, player_2, player_1_result)

    return play_result
```

---

#### :notebook: 7/19/21

- Created test `test_get_game_result()` function in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py).
    - Populated `get_game_result()` function in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py) with code to pass the test.
    - All tests passing but the current test lacks paramaterization and only tests one scenario.

`test_get_game_result()` function:

```python
def test_get_game_result(player_objects):
    """ Test to determine the result of a game by each player, incrementing
        the score after each play.

        Args:
            player_objects (namedtuple): namedtuple of objects of the
                                         Player class.

        Returns:
            None.
    """

    # Extract players from player_object
    player_1 = player_objects.player_1
    player_2 = player_objects.player_2

    # Set mock Player object attribute values
    player_1.score = 2
    player_2.score = 1

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
    assert result.player_1.record.wins == 1 and \
           result.player_2.record.losses == 1 and \
           result.player_1.record.draws == 0 and \
           result.player_2.record.draws == 0 and \
           result.winner == player_1.name
```

`get_game_result()` function:

```python
def get_game_result(
    player_1: Player,
    player_2: Player
) -> namedtuple:
    """ Get the result/winner after each play.

        Args:
            player_1 (Player): UltimateRPS.Player object for player 1.
            player_2 (Player): UltimateRPS.Player object for player 2.

        Return:
            play_result (namedtuple): player_1 and player_2 objects plus
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
            draws=player_1.record.draws + 1
        )

    # Create a namedtuple class to return
    PlayResults = namedtuple('PlayResults', 'player_1 player_2 winner')

    # Create a play_results namedtuple instance to return
    play_results = PlayResults(
        player_1=player_1,
        player_2=player_2,
        winner=winner
    )

    return play_results
```

---

#### :notebook: 7/20/21

- Updated test `test_get_game_result()` function in [`test_ultimate_rps.py`](ultimate_rps/test_ultimate_rps.py).
    - Added paramaterization to select wins, losses, draws, and expected winner (player name) for each of several games.
    - Corrected reference mistake in `get_game_result()` function in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py).
        - Incorrect reference to `player_1.record.draws` (corrected to `player_2.record.draws`).
    - All tests passing.

`test_get_game_result()` function:

```python
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
```

`get_game_result()` function:

```python
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
```

---

#### :notebook: 7/21/21

- Created `game_loop()` function in [`ultimate_rps.py`](ultimate_rps/ultimate_rps.py) to support interactive play.
- Completed game:
    - All tests pass.
    - Time not committed to UI elegance.

`game_loop()` function

```python
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
```
