#!/usr/bin/env python3
""" Main program for abstract factory pattern application. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.factories.tesla_factory \
    import TeslaFactory
from _83_84.pluralsight.factory_pattern.abstract.factories.gm_factory \
    import GMFactory

# Loop over imported concrete factory classes, create objects & run methods
for factory in [TeslaFactory, GMFactory]:

    # Create an economy car and run concrete methods
    new_car = factory().create_economy_car()
    new_car.start()
    new_car.stop()

    # Create a sports car and run concrete methods
    new_car = factory().create_sports_car()
    new_car.start()
    new_car.stop()

    # Create a luxury car and run concrete methods
    new_car = factory().create_luxury_car()
    new_car.start()
    new_car.stop()
