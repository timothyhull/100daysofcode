#!/usr/bin/env python3
""" Abstract factory pattern concrete product class for Tesla. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.autos.abs_auto \
    import ABSAuto


# Concrete product classes
class ModelS(ABSAuto):
    """ Concrete product class for Model S. """

    def start(self) -> None:
        """ Start a Tesla Model S.

            Args:
                None.

            Returns:
                None.
        """

        print('Model S powerfully starting up...')

        return None

    def stop(self) -> None:
        """ Stop a Tesla Model S.

            Args:
                None.

            Returns:
                None.
        """

        print('Model S begrudgingly entering standby mode...')

        return None
