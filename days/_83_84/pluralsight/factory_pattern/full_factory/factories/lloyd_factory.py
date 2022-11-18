#!/usr/bin/env python3
""" Lloyd concrete factory class definition. """

# Imports - Local
from .abstract_factory import AbstractFactory
from ..autos.lloyd import Lloyd


class LloydFactory(AbstractFactory):
    """ Concrete class for instances of Lloyd. """

    def create_auto(self) -> Lloyd:
        """ Lloyd implementation of the abstract factory class """

        self.lloyd = lloyd = Lloyd()
        lloyd.name = 'Lloyd'

        return lloyd
