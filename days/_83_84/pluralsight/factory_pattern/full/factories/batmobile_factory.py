#!/usr/bin/env python3
""" Batmobile concrete factory class definition. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.full.factories.abstract_factory \
    import AbstractFactory
from _83_84.pluralsight.factory_pattern.full.autos.batmobile import Batmobile


class BatmobileFactory(AbstractFactory):
    """ Concrete class for instances of the Batmobile. """

    def create_auto(self) -> Batmobile:
        """ Batmobile implementation of the abstract factory class """

        self.batmobile = batmobile = Batmobile()
        batmobile.name = 'The Batmobile'

        return batmobile
