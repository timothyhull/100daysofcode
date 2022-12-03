#!/usr/bin/env python3
""" Null class constructor concrete factory class definition. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.full.factories.abstract_factory \
    import AbstractFactory
from _83_84.pluralsight.factory_pattern.full.autos.null_car \
    import NullCar


class NullCarFactory(AbstractFactory):
    """ Concrete class for NullCar/unknown concrete product types. """

    def create_auto(self) -> NullCar:
        """ NullCar implementation of the abstract factory class """

        self.null_car = null_car = NullCar()
        null_car.name = 'Unknown car type.'

        return null_car
