#!/usr/bin/env python3
""" Helper functions for the auto_factory app. """


def start(name: str) -> None:
    """ Display custom start message.

        Args:
            name (str): name of the automobile to display.

        Returns:
            None
    """

    print(f'Starting "{name}."')

    return None


def stop(name: str) -> None:
    """ Display custom stop message.

        Args:
            name (str): name of the automobile to display.

        Returns:
            None
    """

    print(f'Stopping "{name}."')

    return None
