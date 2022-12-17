#!/usr/bin/env python3
""" Abstract factory pattern 'factory' abstract class. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


# Class objects
class ABSFactory(ABC):
    """ Abstract factory class to create concrete factories. """

    @abstractmethod
    def create_economy_car(self):
        """ Abstract method to create economy cars for many OEMs. """

        pass

    @abstractmethod
    def create_sports_car(self):
        """ Abstract method to create sport cars for many OEMs. """

        pass

    @abstractmethod
    def create_luxury_car(self):
        """ Abstract method to create luxury cars for many OEMs. """

        pass
