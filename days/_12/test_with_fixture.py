#!/usr/bin/env pytest

# Imports
from name_game import get_name,\
                      name_to_title,\
                      name_to_lower,\
                      name_to_upper, \
                      name_to_random

from pytest import fixture

# Constants
NAME = 'tim hull'


@fixture
def fixture_name():
    """ Fixture to supply each test function with a value, withing having
        to manually specify a value or use a function to supply the value.
        Instead, the value is provided by passing the name of the fixture
        function ('fixture_name') as an argument to each test function.
    """
    name = NAME

    return name


def test_get_name():
    assert get_name().first is not None
    assert get_name().last is not None


def test_name_to_title(fixture_name):
    # name = static_name()
    assert name_to_title(fixture_name) is not None
    assert name_to_title(fixture_name).istitle() is True


def test_name_to_lower(fixture_name):
    # name = static_name()
    assert name_to_lower(fixture_name) is not None
    assert name_to_lower(fixture_name).islower() is True


def test_name_to_upper(fixture_name):
    # name = static_name(fixture_name)
    assert name_to_upper(fixture_name) is not None
    assert name_to_upper(fixture_name).isupper()


def test_name_to_random(fixture_name):
    # name = static_name()
    assert name_to_random(fixture_name) is not None
    assert name_to_random(fixture_name).istitle() is not True
    assert name_to_random(fixture_name).islower() is not True
    assert name_to_random(fixture_name).isupper() is not True
