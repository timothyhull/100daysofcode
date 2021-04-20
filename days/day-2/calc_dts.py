#!/usr/bin/env python3

# Reference: https://codechalleng.es/bites/67/

# Imports
from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""

    # Create a 100 day time delta object
    delta_100_days = timedelta(100)

    # Add the time delta object to the start date and convert to a string
    time_delta = str(start_100days + delta_100_days)

    return time_delta


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""

    # Subtract the founding date from the pycon_date
    days_timedelta = pycon_date - pybites_founded

    # Extract the integer number of days from days_timedelta
    days = days_timedelta.days

    return days
