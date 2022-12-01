#!/usr/bin/env python3
""" Dynamic concrete factory class loader.

    Uses user-supplied concrete factory (car brand/model) name
    to dynamically import the corresponding concrete factory class,
    if it exists, using the importlib.import_module method.  If no
    concrete class matches the user-supplied name, return a null class.
"""

# Imports - Python Standard Library
from importlib import import_module
from inspect import getmembers, isabstract, isclass
from typing import Type

# Imports - Local
from _83_84.pluralsight.factory_pattern.full.factories.abstract_factory \
    import AbstractFactory

# Constants
DEFAULT_FACTORY_NAME = 'Unknown'


def load_factory(
    factory_name: str = DEFAULT_FACTORY_NAME
) -> Type:
    """ Attempt to import and return a named concrete factory class.

        Args:
            factory_name (str, optional):
                Case-sensitive name of the concrete factory class to
                import.  Default is DEFAULT_FACTORY_NAME.

        Returns:
            _class (Type):
                Instance of a matching concrete factory class or, if no
                concrete class matches the user input value, return an
                instance of the NullCarFactory class.
    """

    # Attempt to import a concrete factory class name that matches user input
    try:
        factory_module = import_module(
            name=f'{factory_name}_factory',
            package='factories'
        )

    # If no matching concrete factory class is found, return a null class
    except ImportError:
        factory_module = import_module(
            name='null_car_factory',
            package='factories'
        )

    # Get a list of available classes
    classes = getmembers(
        object=factory_module,

        # Filter class members to a single match
        predicate=lambda x: isclass(x) and not isabstract(x)
    )

    # Return only a single class (the first class) from the classes object
    for _, _class in classes:
        if issubclass(_class, AbstractFactory):
            return _class()
