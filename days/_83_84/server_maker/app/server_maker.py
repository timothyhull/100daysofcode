#!/usr/bin/env python3
""" Server Maker application for testing abstract factory design. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod
from typing import NamedTuple

# Imports - Third-Party

# Imports - Local


# NamedTuple objects
class ServerParams(NamedTuple):
    """ Object to define cloud-agnostic server parameters.

        Args:
            name (str):
                Server name.

            size (str, optional):
                Server template size.  Valid values are:
                    micro
                    small
                    medium
                    large
                    xlarge
                Default is micro.

            ha (bool, optional):
                High-availability/redundancy.  Default is False.


    """

    name: str
    size: str = 'micro'
    ha: bool = False


# Constants
SERVER_SIZE_MAPPING = {
    '1': 'micro',
    '2': 'small',
    '3': 'medium',
    '4': 'large',
    '5': 'xlarge'
}
SERVER_1_PARAMS = ServerParams(
    name='server_1',
    size='small',
    ha=False
)


# Abstract factory class
class ServerMaker(ABC):
    """ Basic representation of a cloud server provisioning app. """

    @abstractmethod
    def create_server_config(
        self,
        params: ServerParams = SERVER_1_PARAMS
    ):
        """ Construct a server configuration definition. """
        pass
