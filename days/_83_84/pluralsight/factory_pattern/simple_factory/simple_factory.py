#!/usr/bin/env python3
""" Simple example of the factory design pattern. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


class AbstractAutomobile(ABC):
    """ Abstract Base Class for Automobile Creation. """

    @abstractmethod
    def Start(self) -> None:
        pass

    @abstractmethod
    def Stop(stop) -> None:
        pass
