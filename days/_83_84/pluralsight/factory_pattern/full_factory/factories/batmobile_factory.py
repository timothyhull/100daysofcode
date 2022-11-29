#!/usr/bin/env python3
""" Batmobile concrete factory class definition. """

# Imports - Local
from abstract_factory import AbstractFactory
from _83_84.pluralsight.factory_pattern.full_factory.autos.batmobile \
    import Batmobile


class BatmobileFactory(AbstractFactory):
    """ Concrete class for instances of the Batmobile. """

    def create_auto(self) -> Batmobile:
        """ Batmobile implementation of the abstract factory class """

        self.batmobile = batmobile = Batmobile()
        batmobile.name = 'The Batmobile'

        return batmobile
