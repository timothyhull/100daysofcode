#!/usr/bin/env python3
""" Helper functions for the Server Maker application. """

# Imports - Python Standard Library
from random import randint
from typing import Union

# Imports - Third-Party

# Imports - Local

# Constants
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
    for i in range(1, length):
        server_name += str(randint(0, 9))

    return server_name
