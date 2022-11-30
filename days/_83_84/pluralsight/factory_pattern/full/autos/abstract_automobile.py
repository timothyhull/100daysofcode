#!/usr/bin/env python3
""" Abstract Base Class to produce concrete products. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


class AbstractAutomobile(ABC):
    """ Abstract Base Class definition. """

    @property
    def name(self) -> str:
        """ Definition of the 'name' property. """

        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """ Set the value of the 'name' property. """

        self._name = name
        return None

    @abstractmethod
    def start(self) -> None:
        """ Abstract 'start' method definition. """

        pass

    @abstractmethod
    def stop(self) -> None:
        """ Abstract 'stop' method definition. """

        pass
