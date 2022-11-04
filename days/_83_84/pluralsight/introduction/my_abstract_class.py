#!/usr/bin/env python3
""" Abstract Base Class definition """

# Import the abc module
import abc


# Create an abstract class
class MyABC(abc.ABC):
    """ Abstract Base Class definition.

        Inheriting the abc.ABC class tells Python that this class
        is abstract.
    """

    # Define abstract methods with the @abc.abstractmethod decorator
    @abc.abstractmethod
    def do_something(self, value) -> None:
        """ Required method. """
        pass

    # Define abstract properties with the @abc.abstractproperty decorator
    @abc.abstractproperty
    def some_property(self) -> None:
        """ Required property. """
        pass


# Concrete class implementation
class MyClass(MyABC):
    """ Implementation of an Abstract Base Class.

        Create a Concrete Class by inheriting the abstract
        "MyABC" class.  This enables the Abstract Base Class
        special processing in Python, when the class is instantiated.

        During instantiation, the Abstract Base Class checks to confirm
        that all of the defined abstract methods and properties exist
        in the concrete class.
    """

    def __init__(self, value=None) -> None:
        """ Initialization method. """
        self._myprop = value

    def do_something(self, value) -> None:
        """ Implementation of abstract method. """
        self._myprop *= value

    # Be sure to use the @property decorator so the class works correctly
    @property
    def some_property(self):
        """ Implementation of abstract property. """
        return self._myprop


class BadClassExample(MyABC):
    """ Test to determine the result of not implementing all abstract
        methods and properties.
    """
    pass
