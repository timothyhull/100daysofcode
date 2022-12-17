#!/usr/bin/env python3
""" Abstract factory pattern concrete product class for GM. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.autos.abs_auto \
    import ABSAuto


class GMHummer(ABSAuto):
    """ Concrete product class for GM Hummer. """

    def start(self) -> None:
        """ Start a GM Hummer.

            Args:
                None.

            Returns:
                None.
        """

        print('GM Hummer powerfully starting up...')

        return None

    def stop(self) -> None:
        """ Stop a GM Hummer.

            Args:
                None.

            Returns:
                None.
        """

        print('GM Hummer ambiguously entering standby mode...')

        return None
