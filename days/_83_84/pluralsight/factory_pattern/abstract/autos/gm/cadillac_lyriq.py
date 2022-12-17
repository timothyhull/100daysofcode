#!/usr/bin/env python3
""" Abstract factory pattern concrete product class for GM. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.autos.abs_auto \
    import ABSAuto


class CadillacLyriq(ABSAuto):
    """ Concrete product class for Cadillac Lyriq. """

    def start(self) -> None:
        """ Start a Cadillac Lyriq.

            Args:
                None.

            Returns:
                None.
        """

        print('Cadillac Lyriq pretentiously starting up...')

        return None

    def stop(self) -> None:
        """ Stop a Cadillac Lyriq.

            Args:
                None.

            Returns:
                None.
        """

        print('Cadillac Lyriq fashionably entering standby mode...')

        return None
