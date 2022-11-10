#!/usr/bin/env python3
""" Automobile abstract factory application example. """

# Imports - Python Standard Library
from inspect import getmembers, isclass, isabstract
from typing import Union

# Imports - Local
# Import the 'autos' directory to automatically run __init.py__
# import days._83_84.pluralsight.factory_pattern.simple_factory.autos as autos
from . import autos as Autos


class AutoFactory(object):
    """ TODO """

    # Create a dictionary to contain car information
    autos = {}  # key = car model name, value = class for the car

    def __init__(self) -> None:
        """ TODO """

        self.load_autos()

    def load_autos(self, carname) -> None:
        """ TODO """

        # TODO
        classes = getmembers(
            Autos,
            lambda member: isclass(member) and not isabstract(member)
        )

        # TODO
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, Autos.AbstractAutomobile):
                self.autos.update([[name, _type]])

        return None

    def create_instance(
        self,
        carname: str
    ) -> Union(str | Autos.NullCar):
        """ TODO """

        # TODO
        if carname in self.autos:
            return self.autos[carname]
        else:
            return Autos.NullCar(carname)
