#!/usr/bin/env python3
""" Testing usage of the abstract factory design pattern. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


# Abstract factory class
class ITProvisioner(ABC):
    """ Abstract factory class for provisioning IT resources. """

    @abstractmethod
    def provision_resource(self):
        pass


# Abstract product 1
class Server(ABC):
    """ Abstract product for new servers """

    @abstractmethod
    def new_linux_server(self):
        pass

    @abstractmethod
    def new_win_server(self):
        pass


# Abstract product 2
class NetDevice(ABC):
    """ Abstract product for new network devices """

    @abstractmethod
    def new_router(self):
        pass

    @abstractmethod
    def new_switch(self):
        pass

    @abstractmethod
    def new_firewall(self):
        pass


# Concrete product 1
class CreateServer(Server):

    def new_linux_server(self):
        print('Created new Linux server')

    def new_win_server(self):
        print('Created new Windows server')


# Concrete product 2
class CreateNetDevice(NetDevice):

    def new_router(self):
        print('Created new router')

    def new_switch(self):
        print('Created new switch')

    def new_firewall(self):
        print('Created new firewall')


# Concrete factory 1
class NewServer(ITProvisioner):

    def provision_resource(self):
        return CreateServer()


# Concrete factory 2
class NewNetDevice(ITProvisioner):

    def provision_resource(self):
        return CreateNetDevice()


def main() -> None:
    """ Main application.

        Args:
            None.

        Returns:
            None.
    """
    pass


if __name__ == '__main__':
    main()
