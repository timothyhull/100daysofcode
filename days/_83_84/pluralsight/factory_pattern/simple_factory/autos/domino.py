#!/usr/bin/env python3
""" Domino class definition. """

# Imports - Python Standard Library
from .abstract_automobile import AbstractAutomobile


class Domino(AbstractAutomobile):
    """ Class for instances of Domino. """

    def start(self) -> None:
        print('Starting Domino.')

        return None

    def stop(self) -> None:
        print('Stopping Domino.')

        return None
