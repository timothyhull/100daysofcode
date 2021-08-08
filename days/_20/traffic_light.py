#!/usr/bin/env python3
""" Application to simulate traffic light behavior
"""

# Imports
from itertools import cycle
from light_signals import TrafficLights
from os import system
from random import randint
from sys import stdout
from time import sleep

# Constants
INTERVAL = 1.0
LIGHTS = TrafficLights()
RED = LIGHTS.red
YELLOW = LIGHTS.yellow
GREEN = LIGHTS.green

# Create a list of light colors to cycle over
colors = [
    GREEN,
    YELLOW,
    RED
]

# Create cycles object
light_cycle = cycle(colors)


def traffic(
    interval: float = INTERVAL,
    random: bool = False
) -> None:
    """ Display a loop of traffic signals.

        Args:
            interval (float):
                Interval between light changes.
            random (bool):
                Randomize the interval.

        Returns:
            None.
    """

    try:
        # Loop until a keyboard interrupt sequence
        while True:
            # Clear the screen
            system('clear')

            # Display the next iteration in the cycle object
            stdout.write(f'{next(light_cycle)}')
            stdout.flush()

            # Determine if the interval is random
            if random is True:
                interval = randint(1, 4)

            # Sleep for the interval time
            sleep(interval)

    except KeyboardInterrupt as e:
        print(f'\n{e!r}')
