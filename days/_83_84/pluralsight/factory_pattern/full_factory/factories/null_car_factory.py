#!/usr/bin/env python3
""" Null class constructor concrete factory class definition. """

# Imports - Local
from .abstract_factory import AbstractFactory
from ..autos.null_car import NullCar


class RivianFactory(AbstractFactory):
    """ Concrete class for instances of Rivian. """

    def create_auto(self) -> NullCar:
        """ NullCar implementation of the abstract factory class """

        self.null_car = null_car = NullCar()
        null_car.name = 'Rivian'

        return null_car
