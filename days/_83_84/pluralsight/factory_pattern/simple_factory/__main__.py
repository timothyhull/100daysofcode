#!/usr/bin/env python3
""" Package main program for the auto_factory.py app. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.simple_factory.auto_factory \
    import AutoFactory

# Constants
car_names = {
    'batmobile',
    'domino',
    'lloyd'
}

# Create an AbstractAutomobile instance
factory = AutoFactory()
