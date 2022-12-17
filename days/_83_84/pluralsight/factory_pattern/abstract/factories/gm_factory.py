#!/usr/bin/env python3
""" Abstract factory pattern concrete factory class for GM. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.factories.abs_factory \
    import ABSFactory
from _83_84.pluralsight.factory_pattern.abstract.autos.gm.chevy_bolt \
    import ChevyBolt
from _83_84.pluralsight.factory_pattern.abstract.autos.gm.gm_hummer \
    import GMHummer
from _83_84.pluralsight.factory_pattern.abstract.autos.gm.cadillac_lyriq \
    import CadillacLyriq


class GMFactory(ABSFactory):
    """ TODO """

    def create_economy_car(self) -> ChevyBolt:
        """ TODO """

        return ChevyBolt()

    def create_sports_car(self) -> GMHummer:
        """ TODO """

        return GMHummer()

    def create_luxury_car(self) -> CadillacLyriq:
        """ TODO """

        return CadillacLyriq()
