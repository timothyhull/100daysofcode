#!/usr/bin/env python3
""" Batmobile concrete class definition. """

# Imports - Local
from .abstract_automobile import AbstractAutomobile


class Batmobile(AbstractAutomobile):
    """ Concrete class for instances of the Batmobile. """

    def start(self) -> None:
        print('Starting Batmobile.')

        return None

    def stop(self) -> None:
        print('Stopping Batmobile.')

        return None
