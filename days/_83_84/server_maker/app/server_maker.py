#!/usr/bin/env python3
""" Server Maker application for testing abstract factory design. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod
from typing import NamedTuple

# Imports - Third-Party

# Imports - Local
from server_maker_helper import (  # type: ignore (ignores Pylance warning)
    generate_server_name
)

# Server name length constants
SERVER_BASE_NAME = 'svr_'
SERVER_NAME_LENGTH = 8


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


# Abstract product class or interface class #1
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
        target_cloud: str(int) = DEFAULT_CLOUD
    ) -> None:

        """ Deploy a server configuration to a cloud provider """
        pass


# Concrete product classes
class AWSServer(ServerMaker):
    """ Create an AWS Server. """

    def create_server_config(
        self,
        params: ServerParams = SERVER_1_PARAMS
    ) -> str:
        """ Create an AWS server configuration string. """

        # Call a function that produces the AWS-formatted string

        return None


class AzureServer(ServerMaker):
    """ Create an Azure Server. """

    def create_server_config(
        self,
        params: ServerParams = SERVER_1_PARAMS
    ) -> str:
        """ Create an AWS server configuration string. """

        # Call a function that produces the Azure-formatted string

        return None


class GCPServer(ServerMaker):
    """ Create an GCP Server. """

    def create_server_config(
        self,
        params: ServerParams = SERVER_1_PARAMS
    ) -> str:
        """ Create an GPC server configuration string. """

        # Call a function that produces the GPC-formatted string

        return None
