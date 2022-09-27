#!/usr/bin/env python3
""" Test application without any abstract/factory classes.

    Class instance creation and runtime both occur within the
    'main' function.
"""


class CreatePXPlot():
    """ Concrete Product #1. """

    def create_plot(self) -> None:
        print('Created PX Plot')
        return None


class CreateGOPlot():
    """ Concrete Product #2. """

    def create_plot(self) -> None:
        print('Created GO Plot')
        return None


def main() -> None:
    """ Main application. """

    px_plot = CreatePXPlot()
    go_plot = CreateGOPlot()

    px_plot.create_plot()
    go_plot.create_plot()


if __name__ == '__main__':
    main()
