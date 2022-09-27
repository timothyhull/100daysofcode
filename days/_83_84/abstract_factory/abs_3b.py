#!/usr/bin/env python3
""" Test application without any abstract/factory classes.

    Class instance creation and runtime both occur within the
    'main' function.
"""

# Imports - Python Standard Library
from abc import ABC, abstractmethod


class AbstractPlotFactory(ABC):
    """ Abstract factory class for plotting data. """

    @abstractmethod
    def create_plot(self) -> None:
        pass


class AtmosphericCO2PlotPX(ABC):
    """ Abstract Product #1. """

    @abstractmethod
    def create_plot_px(self) -> None:
        pass


class AtmosphericCO2PlotGO(ABC):
    """ Abstract Product #2. """

    @abstractmethod
    def create_plot_go(self) -> None:
        pass


class BarPlotPX(AtmosphericCO2PlotPX):
    """ Concrete Product #1. """

    def create_plot_px(self) -> None:
        print('Created PX Plot')
        return None


class BarPlotGO(AtmosphericCO2PlotGO):
    """ Concrete Product #2. """

    def create_plot_go(self) -> None:
        print('Created GO Plot')
        return None


class AtmosphericCO2PlotPXFactory(AbstractPlotFactory):
    """ Concrete Factory #1 """

    def create_plot(self) -> BarPlotPX:
        return BarPlotPX()


class AtmosphericCO2PlotGOFactory(AbstractPlotFactory):
    """ Concrete Factory #2 """

    def create_plot(self) -> BarPlotGO:
        return BarPlotGO()


def main() -> None:
    """ Main application. """

    # AtmosphericCO2PlotPXFactory()
    # AtmosphericCO2PlotGOFactory()

    pass


if __name__ == '__main__':
    main()
