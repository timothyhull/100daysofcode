#!/usr/bin/env pytest

# Imports
from name_game import get_name,\
                      name_to_title,\
                      name_to_lower,\
                      name_to_upper, \
                      name_to_random

# Constants
NAME = 'tim hull'


def static_name():
    """ Function to provide a value to each test function, which must
        be called by each test function.
    """
    name = NAME

    return name


def test_get_name():
    assert get_name().first is not None
    assert get_name().last is not None


def test_name_to_title():
    name = static_name()
    assert name_to_title(name) is not None
    assert name_to_title(name).istitle() is True


def test_name_to_lower():
    name = static_name()
    assert name_to_lower(name) is not None
    assert name_to_lower(name).islower() is True


def test_name_to_upper():
    name = static_name()
    assert name_to_upper(name) is not None
    assert name_to_upper(name).isupper()


def test_name_to_random():
    name = static_name()
    assert name_to_random(name) is not None
    assert name_to_random(name).istitle() is not True
    assert name_to_random(name).islower() is not True
    assert name_to_random(name).isupper() is not True
