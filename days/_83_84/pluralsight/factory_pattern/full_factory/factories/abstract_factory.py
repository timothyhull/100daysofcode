#!/usr/bin/env python3
""" Abstract Factory Base Class to produce concrete factories. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """ Abstract Factory Class definition.

        Each factory must implement the defined abstract methods.
    """

    @abstractmethod
    def create_auto(self) -> None:
        """ Abstract 'create_auto' method definition. """

        pass
