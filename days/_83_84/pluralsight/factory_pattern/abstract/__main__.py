#!/usr/bin/env python3
""" Main program for abstract factory pattern application. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.factories.tesla_factory \
    import TeslaFactory

new_car = TeslaFactory().create_economy_car()
new_car.start()
new_car.stop()

new_car = TeslaFactory().create_sports_car()
new_car.start()
new_car.stop()

new_car = TeslaFactory().create_luxury_car()
new_car.start()
new_car.stop()
