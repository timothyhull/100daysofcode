#!/usr/bin/env python3
""" Dynamic factory class loader """

# Imports - Python Standard Library
from importlib import import_module
from inspect import getmembers, isabstract, isclass

# Imports - Local
from abstract_factory import AbstractFactory


def load_factory(factory_name: str) -> None:
    """ TODO """

    # TODO
    try:
        factory_module = import_module(
            name=f'.{factory_name}',
            package='factories'
        )

    # TODO
    except ImportError:
        factory_module = import_module(
            name='.null_car_factory',
            package='factories'
        )

    # Get a list of available classes
    classes = getmembers(
        object=factory_module,
        predicate=lambda x: isclass(x) and not isabstract(x)
    )

    # TODO
    for _, _class in classes:
        if issubclass(_class, AbstractFactory):
            return _class()
