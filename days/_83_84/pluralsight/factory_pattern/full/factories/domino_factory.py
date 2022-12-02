#!/usr/bin/env python3
""" Domino concrete factory class definition. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.full.factories.abstract_factory \
    import AbstractFactory
from _83_84.pluralsight.factory_pattern.full.autos.domino import Domino


class DominoFactory(AbstractFactory):
    """ Concrete class for instances of Domino. """

    def create_auto(self) -> Domino:
        """ Domino implementation of the abstract factory class """

        self.domino = domino = Domino()
        domino.name = 'Domino'

        return domino
