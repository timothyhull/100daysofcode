#!/usr/bin/env python3
""" Rivian class definition. """

# Imports - Local
from .abstract_automobile import AbstractAutomobile


class Rivian(AbstractAutomobile):
    """ Class for instances of Rivian. """

    def start(self) -> None:
        print('Starting Rivian.')

        return None

    def stop(self) -> None:
        print('Stopping Rivian.')

        return None
