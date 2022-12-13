#!/usr/bin/env python3
""" Abstract factory pattern autos abstract classes. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


class ABSAutos(ABC):
    """ TODO """

    @abstractmethod
    def create_auto(self) -> None:
        """ TODO """

        pass
