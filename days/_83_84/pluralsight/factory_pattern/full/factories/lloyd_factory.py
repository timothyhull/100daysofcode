#!/usr/bin/env python3
""" Lloyd concrete factory class definition. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.full.factories.abstract_factory \
    import AbstractFactory
from _83_84.pluralsight.factory_pattern.full.autos.lloyd import Lloyd


class LloydFactory(AbstractFactory):
    """ Concrete class for instances of Lloyd. """

    def create_auto(self) -> Lloyd:
        """ Lloyd implementation of the abstract factory class """

        self.lloyd = lloyd = Lloyd()
        lloyd.name = 'Lloyd'

        return lloyd
