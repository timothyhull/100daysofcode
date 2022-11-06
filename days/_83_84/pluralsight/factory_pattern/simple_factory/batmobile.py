#!/usr/bin/env python3
""" Batmobile class definition. """

# Imports - Python Standard Library
from .simple_factory import AbstractAutomobile


class Batmobile(AbstractAutomobile):
    def Start(self) -> None:
        print('Starting Batmobile.')

        return None

    def Stop(self) -> None:
        print('Stopping Batmobile.')

        return None
