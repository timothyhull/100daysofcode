#!/usr/bin/env python3
""" Null class constructor for unknown cars. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.full.autos.abstract_automobile \
    import AbstractAutomobile


class NullCar(AbstractAutomobile):
    """ Concrete class for instances of unknown/NullCar cars. """

    def start(self) -> None:
        print('Error, unknown car.')
        print(self._name)
        return None

    def stop(self) -> None:
        pass
