#!/usr/bin/env python3
""" Abstract factory pattern concrete product class for Tesla. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.autos.abs_auto \
    import ABSAuto


# Concrete product classes
class Model3(ABSAuto):
    """ Concrete product class for Model 3. """

    def start(self) -> None:
        """ Start a Tesla Model 3.

            Args:
                None.

            Returns:
                None.
        """

        print('Model 3 economically starting up...')

        return None

    def stop(self) -> None:
        """ Stop a Tesla Model 3.

            Args:
                None.

            Returns:
                None.
        """

        print('Model 3 subtly entering standby mode...')

        return None
