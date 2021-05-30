#!/usr/bin/env python3

# Imports
import random

# Constants
START_NUM = 1
END_NUM = 20


# Get a random number
def get_random_num():
    random_num = random.randint(START_NUM, END_NUM)

    return random_num


# Get user input
def get_user_input():
    user_input = input(
        f'Enter a number between: {START_NUM} and {END_NUM}: '
    )

    if user_input is None:
        raise ValueError('Please enter a number')

    try:
        user_input = int(user_input)
    except ValueError:
        raise ValueError('Make sure you enter a number')

    if user_input not in range(START_NUM, END_NUM + 1):
        raise ValueError('The number is out of range')

    return user_input


# Return a boolean (True/False)
def coin_flip(choice):
    # Define the valid argument values
    choices = [
        'heads',
        'tails'
    ]

    # Check for a valid argument value
    if choice.lower() not in choices:
        raise ValueError('Enter "heads" or "tails"')

    # Flip the coin
    coin = random.choice(choices)

    # Determine if the choice matches the coin flip, as a boolean
    boolean_response = coin == choice.lower()

    # Print the result
    print(
        f'\nYou chose {choice.title()}, you got {coin.title()}.\n'
    )

    return boolean_response
