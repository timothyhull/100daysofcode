#!/usr/bin/env python3
""" Abstract factory pattern concrete product class for Tesla. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.autos.abs_auto \
    import ABSAuto


# Concrete product classes
class ModelX(ABSAuto):
    """ Concrete product class for Model X. """

    def start(self) -> None:
        """ Start a Tesla Model X.

            Args:
                None.

            Returns:
                None.
        """

        print('Model X comfortably starting up...')

        return None

    def stop(self) -> None:
        """ Stop a Tesla Model X.

            Args:
                None.

            Returns:
                None.
        """

        print('Model X casually entering standby mode...')

        return None
