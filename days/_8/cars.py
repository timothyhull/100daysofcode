#!/usr/bin/env python3

# Imports
from copy import deepcopy

# Cars dictionary
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeeps = cars.get('Jeep')
    jeeps_string = ', '.join(jeeps)

    return jeeps_string


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    car_list = [car[0] for car in cars.values()]

    return car_list


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    car_list = []
    for car in cars.values():
        for model in car:
            if grep.lower() in model.lower():
                car_list.append(model)

    car_list.sort()

    return car_list


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    cars_sorted = deepcopy(cars)
    for models in cars_sorted.values():
        models.sort()

    return cars_sorted
