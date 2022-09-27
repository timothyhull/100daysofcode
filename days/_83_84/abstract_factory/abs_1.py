#!/usr/bin/env python3
""" Testing usage of the abstract factory design pattern. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


# Abstract class
class Airplane(ABC):
    """ Abstract class for all airplanes. """

    @abstractmethod
    def engine_type(self) -> None:
        """ Abstract/common function required by all child classes.

            All child functions must define this method.

            Args:
                None.

            Returns:
                None.
        """
        pass


# Child class #1
class TurboProp(Airplane):
    """ Airplane child/concrete class #1. """

    def engine_type(self) -> str:
        """ Display aircraft engine_type.

            Args:
                None.

            Returns:
                output (str):
                    Engine type.
        """

        output = 'Turbo Prop'

        return output


# Child class #2
class Jet(Airplane):
    """ Airplane child/concrete class #1. """

    def engine_type(self) -> str:
        """ Display aircraft engine_type.

            Args:
                None.

            Returns:
                output (str):
                    Engine type.
        """

        output = 'Jet'

        return output


def main():
    """ Main application.

        Args:
            None.

        Returns:
            None.
    """

    # Display child class #1 output
    prop_plane = TurboProp()
    print(f'\n{prop_plane.engine_type()}')

    # Display child class #2 output
    jet_plane = Jet()
    print(f'\n{jet_plane.engine_type()}')


if __name__ == '__main__':
    main()
