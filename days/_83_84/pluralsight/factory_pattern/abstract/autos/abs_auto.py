#!/usr/bin/env python3
""" Abstract factory pattern 'auto' abstract class. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


class ABSAuto(ABC):
    """ Abstract product methods for each concrete product. """

    @abstractmethod
    def start(self) -> None:
        """ Abstract 'start' method.

            Args:
                None.

            Returns:
                None.
        """

        pass

    @abstractmethod
    def stop(self) -> None:
        """ Abstract 'start' method.

            Args:
                None.

            Returns:
                None.
        """

        pass
