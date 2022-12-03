#!/usr/bin/env python3
""" Main auto factory program. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.full.factories.loader \
    import load_factory

# Constants
CAR_FACTORY_NAMES = (
    'batmobile',
    'domino',
    'lloyd',
    'camry',
    'rivian'
)

# Loop over concrete car factory names and produce concrete products
for car_factory in CAR_FACTORY_NAMES:
    # Create a concrete factory using load_factory and 'factories.' path prefix
    factory = load_factory(
        factory_name=f'factories.{car_factory}'
    )

    # Create a concrete product (car) with the concrete factory object
    car = factory.create_auto()

    # Run methods of the concrete product instance
    car.start()
    car.stop()
