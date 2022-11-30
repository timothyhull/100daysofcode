#!/usr/bin/env python3
""" Package main program for the auto_factory.py app. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.simple.auto_factory \
    import AutoFactory

# Constants
CAR_NAMES = (
    'Batmobile',
    'Domino',
    'Lloyd',
    'Camry',
    'Rivian'
)

# Create an AbstractAutomobile instance
factory = AutoFactory()

# Loop over the CAR_NAMES iterable and run the start and stop methods
for car_name in CAR_NAMES:
    # Use the instance of AutoFactory to run concrete methods
    car = factory.create_instance(car_name)

    # Run instance methods
    car.start()
    car.stop()
