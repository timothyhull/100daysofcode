#!/usr/bin/env python3
""" Rivian concrete class definition. """

# Imports - Local
from .abstract_automobile import AbstractAutomobile
from . import autos_helper


class Rivian(AbstractAutomobile):
    """ Concrete class for instances of Rivian. """

    def start(self) -> None:
        """ Display custom start message. """

        autos_helper.start(name=self.name)

        return None

    def stop(self) -> None:
        """ Display custom stop message. """

        autos_helper.stop(name=self.name)

        return None
