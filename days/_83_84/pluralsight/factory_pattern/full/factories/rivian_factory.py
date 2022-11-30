#!/usr/bin/env python3
""" Rivian concrete factory class definition. """

# Imports - Local
from abstract_factory import AbstractFactory
from _83_84.pluralsight.factory_pattern.full.autos.rivian import Rivian


class RivianFactory(AbstractFactory):
    """ Concrete class for instances of Rivian. """

    def create_auto(self) -> Rivian:
        """ Rivian implementation of the abstract factory class """

        self.rivian = rivian = Rivian()
        rivian.name = 'Rivian'

        return rivian
