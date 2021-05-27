#!/usr/bin/env python3

# Imports
import random
from time import time


# Get a random number
def get_random_num():
    random_num = random.randint(1, 20)

    return random_num


# Print a value
def time_check():
    current_time = time()

    return current_time
