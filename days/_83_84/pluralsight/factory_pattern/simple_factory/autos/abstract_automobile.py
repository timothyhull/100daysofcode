#!/usr/bin/env python3
""" Abstract automobile classes. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


class AbstractAutomobile(ABC):
    """ Abstract Base Class for Automobile Creation. """

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(stop) -> None:
        pass
