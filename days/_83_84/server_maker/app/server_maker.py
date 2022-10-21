#!/usr/bin/env python3
""" Server Maker application for testing abstract factory design. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod
from random import randint
from typing import NamedTuple, Union

# Imports - Third-Party

# Imports - Local

# Server name length constants
SERVER_BASE_NAME = 'svr_'
SERVER_NAME_LENGTH = 8


def generate_server_name(
    base_name: str = SERVER_BASE_NAME,
    length: Union[int, str] = SERVER_NAME_LENGTH
) -> str:
    """ Generate a randomized server name.

        Args:
            base_name (str), optional:
                Base name for a server.  Default is SERVER_BASE_NAME.

            Length (Union[int, str], optional):
                Number of random characters in the server name.
                Default is SERVER_NAME_LENGTH

        Returns:
            server_name (str):
                Randomized server name.
    """

    # Declare an empty string server_name variable
    server_name = base_name

    # Generate a random string for the server name
    for i in range(1, 8):
        server_name += str(randint(0, 9))

    return server_name


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

    name: str = generate_server_name()
    size: str = 'micro'
    ha: bool = False


# Constants
CLOUD_PLATFORMS = {
    '1': 'aws',
    '2': 'azure',
    '3': 'gcp',
    '4': 'oracle'
}
DEFAULT_CLOUD = '1'
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
    ) -> None:

        """ Construct a server configuration definition. """
        pass

    @abstractmethod
    def deploy_server_config(
        self,
        target_cloud: str[int] = DEFAULT_CLOUD
    ) -> None:

        """ Deploy a server configuration to a cloud provider """
        pass
