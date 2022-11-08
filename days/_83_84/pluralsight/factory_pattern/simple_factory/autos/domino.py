#!/usr/bin/env python3
""" Domino class definition. """

# Imports - Python Standard Library
from .abstract_automobile import AbstractAutomobile


class Domino(AbstractAutomobile):
    def Start(self) -> None:
        print('Starting Domino.')

        return None

    def Stop(self) -> None:
        print('Stopping Domino.')

        return None
