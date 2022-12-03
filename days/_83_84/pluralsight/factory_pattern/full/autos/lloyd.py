#!/usr/bin/env python3
""" Lloyd concrete class definition. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.full.autos.abstract_automobile \
    import AbstractAutomobile
from _83_84.pluralsight.factory_pattern.full.autos \
    import autos_helper


class Lloyd(AbstractAutomobile):
    """ Concrete class for instances of Lloyd. """

    def start(self) -> None:
        """ Display custom start message. """

        autos_helper.start(name=self.name)

        return None

    def stop(self) -> None:
        """ Display custom stop message. """

        autos_helper.stop(name=self.name)

        return None
