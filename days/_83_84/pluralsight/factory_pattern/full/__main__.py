#!/usr/bin/env python3
""" Main auto factory program. """

# Imports - Local
from factories.loader import load_factory

# Constants
CAR_FACTORY_NAMES = (
    'batmobile',
    'domino',
    'lloyd',
    'camry',
    'rivian'
)

# TODO
for car_factory in CAR_FACTORY_NAMES:
    factory = load_factory(
        factory_name=car_factory
    )

    # TODO
    car = factory.create_auto()
    car.start()
    car.stop
