#!/usr/bin/env python3
""" Domino concrete class definition. """

# Imports - Local
from .abstract_automobile import AbstractAutomobile
from . import autos_helper


class Domino(AbstractAutomobile):
    """ Concrete class for instances of Domino. """

    def start(self) -> None:
        """ Display custom start message. """

        autos_helper.start(name=self.name)

        return None

    def stop(self) -> None:
        """ Display custom stop message. """

        autos_helper.stop(name=self.name)

        return None
