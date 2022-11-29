#!/usr/bin/env python3
""" Domino concrete class definition. """

# Imports - Local
from .abstract_automobile import AbstractAutomobile


class Domino(AbstractAutomobile):
    """ Concrete class for instances of Domino. """

    def start(self) -> None:
        print(f'Starting "{self.name}."')

        return None

    def stop(self) -> None:
        print(f'Starting "{self.name}."')

        return None
