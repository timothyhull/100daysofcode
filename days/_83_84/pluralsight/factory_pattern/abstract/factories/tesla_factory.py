#!/usr/bin/env python3
""" Abstract factory pattern concrete factory class for Tesla. """

# Imports - Local
from _83_84.pluralsight.factory_pattern.abstract.factories.abs_factory \
    import ABSFactory
from _83_84.pluralsight.factory_pattern.abstract.autos.tesla.model_3 \
    import Model3
from _83_84.pluralsight.factory_pattern.abstract.autos.tesla.model_s \
    import ModelS
from _83_84.pluralsight.factory_pattern.abstract.autos.tesla.model_x \
    import ModelX


# Concrete factory class
class TeslaFactory(ABSFactory):
    """ Concrete factory class for Tesla. """

    def create_economy_car(self) -> Model3:
        """ Concrete factory method for Tesla Model 3.

            Args:
                None.

            Returns:
                Instance of autos.tesla.Model3.
        """

        return Model3()

    def create_sports_car(self) -> ModelS:
        """ Concrete factory method for Tesla Model S.

            Args:
                None.

            Returns:
                Instance of autos.tesla.ModelS.
        """

        return ModelS()

    def create_luxury_car(self) -> ModelX:
        """ Concrete factory method for Tesla Model X.

            Args:
                None.

            Returns:
                Instance of autos.tesla.ModelX.

        """

        return ModelX()
