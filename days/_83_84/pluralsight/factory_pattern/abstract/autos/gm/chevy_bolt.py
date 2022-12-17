#!/usr/bin/env python3
""" Abstract factory pattern concrete product class for GM. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.autos.abs_auto \
    import ABSAuto


class ChevyBolt(ABSAuto):
    """ Concrete product class for Chevy Bolt. """

    def start(self) -> None:
        """ Start a Chevy Bolt.

            Args:
                None.

            Returns:
                None.
        """

        print('Chevy Bolt economically starting up...')

        return None

    def stop(self) -> None:
        """ Stop a Chevy Bolt.

            Args:
                None.

            Returns:
                None.
        """

        print('Chevy Bolt subtly entering standby mode...')

        return None
