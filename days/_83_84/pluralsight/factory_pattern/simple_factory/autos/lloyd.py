#!/usr/bin/env python3
""" Lloyd class definition. """

# Imports - Python Standard Library
from .abstract_automobile import AbstractAutomobile


class Lloyd(AbstractAutomobile):
    """ Class for instances of Lloyd. """

    def start(self) -> None:
        print('Starting Lloyd.')

        return None

    def stop(self) -> None:
        print('Stopping Lloyd.')

        return None
