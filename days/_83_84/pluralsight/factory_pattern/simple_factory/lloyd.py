#!/usr/bin/env python3
""" Lloyd class definition. """

# Imports - Python Standard Library
from .simple_factory import AbstractAutomobile


class Lloyd(AbstractAutomobile):
    def Start(self) -> None:
        print('Starting Lloyd.')

        return None

    def Stop(self) -> None:
        print('Stopping Lloyd.')

        return None
