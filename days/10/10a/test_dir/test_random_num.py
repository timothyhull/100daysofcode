# Import the random number file function
from random_number import get_random_num

# Working with random numbers requires that we import the random module
import random

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
