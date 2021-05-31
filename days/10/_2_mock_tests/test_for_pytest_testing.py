# Import the file and functions to test
from pytest_testing import get_random_num, \
                           get_user_input, \
                           coin_flip

# Working with random numbers requires that we import the random module
import random

# Testing for exceptions requires that we input the pytest module
import pytest

# Import the 'builtins' function to mock input (not actually required)
# import builtins

"""We need to mock up a test result, since there is no way to predict
   the result of a random number within a range"""
from unittest.mock import patch


"""Use the @patch decorator to mock up a random number (with a static number)
   'patch.bject' method, first argument=module for mockup,
   second argument=function for mockup"""


@patch.object(random, 'randint')
# Create a function for testing (don't for get to start it with 'test')
def test_get_random_num(number):
    """Assign a dummy value to the 'return_value' attribute, from the
       correct range of numbers (1-20, in this case)
       Overrides/simulates the number `randint` would provide"""
    number.return_value = 15

    """Create an assert statement for pytest
       Call the function to test and assert that the simulated
       return value is correct"""
    assert get_random_num() == 15


@patch(
   # Use the `builtins.input` object type
   'builtins.input',
   # Specify 'side_effect' values which are possible inputs by the user
   side_effect=[4, '4', 15, 'tim', -4, 30, None]
)
# Function to test for validity of user input
def test_get_user_input(user_input):
    # Test for the first three inputs/side_effects, which should work correctly
    assert get_user_input() == 4
    assert get_user_input() == 4
    assert get_user_input() == 15

    # Test for an exception generated by the forth input
    with pytest.raises(ValueError):
        get_user_input()

    # Test for an exception generated by the fifth, sixth, and seventh inputs
    with pytest.raises(ValueError):
        get_user_input()
    with pytest.raises(ValueError):
        get_user_input()
    with pytest.raises(ValueError):
        get_user_input()


def test_coin_flip(capfd):
    """Function to test the validity of a return value.
       In this case, whether the return value is either True or False.
       Also test the output (stdout) printed by the function matches
       an expected value.
    """

    # Define the valid return values
    valid_returns = [
        True,
        False,
    ]

    # Create a list of input values to choose from
    choices = [
        'heads',
        'tails'
    ]

    """Randomly choose an input value to test with.
       This could be a static test although randomizing is more realistic.
    """
    choice = random.choice(choices)

    # Verify the return value is valid
    assert coin_flip(choice) in valid_returns

    """Assign the values from capfd.readouterr() to two variables
       The two arguments in capfd.readouterr() are 'out=' and 'err='
       Use the throwaway variable '_' for 'err=' or, another option
       is to specify the 0 index of capfd.readouterr() like this:
       out = capfd.readouterr()[0]
    """
    out, _ = capfd.readouterr()

    # Verify the expected, printed output is in the 'out' variable.
    assert f'You chose {choice.title()}, you got ' in out

    """Test for a ValueError raised by the coin_flip function
       When an invalid value is input
    """
    with pytest.raises(ValueError):
        coin_flip('ducks')