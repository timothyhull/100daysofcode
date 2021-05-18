#!/usr/bin/env python3

"""Imports, sorts, and displays a list of lights with the use of
   the 'collections' module.

Usage: python3 light_serter.py
"""

# Imports
from json import load
from collections import namedtuple
# from collections import Counter, defaultdict
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
LightData = namedtuple('LightData', 'id name modes')

# Create a list object to store namedtuples of light data
lights = []

# Loop over the data set and populate the lights list with namedtuples
for key, value in all_lights.items():
    # Determine whether or not the light supports enhanced modes
    if value['type'] in light_types['enhanced']['names']:
        light_modes = light_types['enhanced']['modes']
    else:
        light_modes = light_types['basic']['modes']

    # Add a namedtuple of light data to the 'lights' list
    lights.append(
        LightData(
            id=key,
            name=value.get('name', None),
            modes=light_modes
        )
    )

# Find the light with the longest name, to format the output
name_len = []
for light_name in lights:
    name_len.append(len(light_name.name))
spaces = max(name_len) + 1

# Display an output header banner
header_banner = '** Choose a light for availability monitoring **'
print(f'\n{header_banner}\n')

# Display column headers
header = f'No:  {"Name:":<{spaces}} {"Modes:":<28}'
print(header)
print(f'{"-" * len(header)}')

# Display list of lights and modes
for index, light in enumerate(lights):
    print(f'{index + 1:>2}.  '
          f'{light.name:<{spaces}} '
          f'{", ".join(light.modes)}')
