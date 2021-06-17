#!/usr/bin/env pytest

# Imports
from name_game import get_name,\
                      name_to_upper,\
                      name_to_lower,\
                      name_to_random


def test_get_name():
    assert get_name().first is not None
    assert get_name().last is not None


def test_name_to_upper():
    assert name_to_upper() is not None


def test_name_to_lower():
    assert name_to_lower() is not None


def test_name_to_random():
    assert name_to_random() is not None
