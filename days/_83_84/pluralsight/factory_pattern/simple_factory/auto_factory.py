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
        """ Initialization method. """

        # Run the load_autos method at during object instantiation
        self.load_autos()

    def load_autos(self, carname) -> None:
        """ Gets a list of sub-classes in the 'autos' folder.

            The 'getmembers' function retrieves a list of tuples
            for the 'autos' folder.  A lambda function removes all
            objects that are not classes (__doc__, etc.), and not
            abstract classes(AbstractAutomobile).
        """

        # Creates a list of tuples with non-abstract class object in 'autos'
        classes = getmembers(
            Autos,
            # lambda function removes any non-class and abstract class objects
            lambda member: isclass(member) and not isabstract(member)
        )

        # Adds each class name and type (class) to the autos dictionary
        # The _type keyword returns the object type of tuple index 1
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
