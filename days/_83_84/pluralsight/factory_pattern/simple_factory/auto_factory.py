#!/usr/bin/env python3
""" Automobile abstract factory application example. """

# Imports - Python Standard Library
from inspect import getmembers, isclass, isabstract

# Imports - Local
# Import the 'autos' directory to automatically run __init.py__
from _83_84.pluralsight.factory_pattern.simple_factory import autos


class AutoFactory(object):
    """ TODO """

    # Create a dictionary to contain car information
    autos = {}  # key = car model name, value = class for the car

    def __init__(self) -> None:
        """ TODO """

        self.load_autos()

    def load_autos(self) -> None:
        """ TODO """

        classes = getmembers(
            autos,
        )

        for c in classes:
            print(c)
            break
