#!/usr/bin/env python3
""" Lloyd concrete class definition. """

# Imports - Local
from .abstract_automobile import AbstractAutomobile


class Lloyd(AbstractAutomobile):
    """ Concrete class for instances of Lloyd. """

    def start(self) -> None:
        print('Starting Lloyd.')

        return None

    def stop(self) -> None:
        print('Stopping Lloyd.')

        return None
