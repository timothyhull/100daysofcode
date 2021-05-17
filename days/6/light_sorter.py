#!/usr/bin/env python3

"""Imports, sorts, and displays a list of lights with the use of
   the 'collections' module.

Usage: python3 light_serter.py
"""

# Imports
from json import load, dump
from collections import Counter, defaultdict, namedtuple
from yaml import safe_load

# Constants
LIGHT_TYPE_CONFIG_PATH = './light_types.yml'
SOURCE_DATA_FILE = './hue_light_data.json'

# Create light_types dictionary to define light type/mode mappings

# Load light type/mode mappings and set variables to represent subkeys
with open(file=LIGHT_TYPE_CONFIG_PATH,
          mode='rt',
          encoding='utf-8') as file:
    light_data = safe_load(file.read())
    light_types = light_data['lights']['hue']['types']
    light_modes = light_data['lights']['hue']['modes']

# Import source data from a file
with open(file=SOURCE_DATA_FILE,
          mode='rt',
          encoding='utf-8') as file:
    all_lights = load(file)

# Create namedtuple class to store data for a light
LightData = namedtuple('LightData', 'name modes')

# Create defaultdict object to store namedtuples of light data
#  lights = defaultdict(LightData)
lights = {}

# Loop over the data set and populate the lights defaultdict with namedtuples
for key, value in all_lights.items():
    if value['type'] in light_types['enhanced']['names']:
        light_modes = light_types['enhanced']['modes']
    else:
        light_modes = light_types['basic']['modes']
    lights[key] = LightData(
            name=value.get('name', None),
            modes=light_modes
        )

from pprint import pprint as pp; pp(lights)
