#!/usr/bin/env python3
""" Domino concrete factory class definition. """

# Imports - Local
from .abstract_factory import AbstractFactory
from ..autos.domino import Domino


class DominoFactory(AbstractFactory):
    """ Concrete class for instances of Domino. """

    def create_auto(self) -> Domino:
        """ Domino implementation of the abstract factory class """

        self.domino = domino = Domino()
        domino.name = 'Domino'

        return domino
