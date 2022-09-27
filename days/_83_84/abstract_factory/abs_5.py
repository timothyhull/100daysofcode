#!/usr/bin/env python3
""" Testing usage of the abstract factory design pattern. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod


# Abstract factory class
class ServiceCatalog(ABC):
    @abstractmethod
    def device_services(self):
        pass


# Abstract product class #1
class MobilePhone(ABC):
    @abstractmethod
    def provision_device(self):
        pass

    @abstractmethod
    def provision_user(self):
        pass


# Abstract product class #2
class Laptop(ABC):
    @abstractmethod
    def provision_device(self):
        pass

    @abstractmethod
    def provision_user(self):
        pass


# Concrete product class #1
class ATTPhoneServices(MobilePhone):
    def provision_device(self):
        print('Added new AT&T device')

    def provision_user(self):
        print('Added new AT&T user')


# Concrete product class #2
class MacBookProServices(Laptop):
    def provision_device(self):
        print('Added new MacBookPro')

    def provision_user(self):
        print('Added new MacBookPro User')


# Concrete factory class #1
class ATTPhone(ServiceCatalog):
    def device_services(self):
        return ATTPhoneServices()


# Concrete factory class #2
class MacBookPro(ServiceCatalog):
    def device_services(self):
        return MacBookProServices()


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
