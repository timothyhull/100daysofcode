#!/usr/bin/env python3
""" Null class constructor for unknown cars. """

# Imports - Local
from .abstract_automobile import AbstractAutomobile


class NullCar(AbstractAutomobile):
    def __init__(self, car_name) -> None:
        self._car_name = car_name

        return None

    def start(self) -> None:
        print(f'Error, unknown car, "{self._car_name}".')

        return None

    def stop(self) -> None:
        pass
