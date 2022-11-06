#!/usr/bin/env python3
""" Null class constructor for unknown cars. """

# Imports - Python Standard Library
from .simple_factory import AbstractAutomobile


class NullCar(AbstractAutomobile):
    def __init__(self, car_name) -> None:
        self._car_name = car_name

        return None

    def Start(self) -> None:
        print(f'Error, unknown car, "{self._car_name}".')

        return None

    def Stop(self) -> None:
        pass
