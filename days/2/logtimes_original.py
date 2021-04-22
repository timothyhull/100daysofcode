#!/usr/bin/env python3

# Reference: https://codechalleng.es/bites/7

# Imports
from datetime import datetime, timedelta
import os
import re
import urllib.request

# Constants
DATE_PATTERN = r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])'
DATE_RE = re.compile(DATE_PATTERN)
SHUTDOWN_EVENT = 'Shutdown initiated'
TIME_PATTERN = r'([0-1][0-9]|2[0-4])(:([0-5][0-9]|60)){2}'
TIME_RE = re.compile(TIME_PATTERN)
URL = 'https://bites-data.s3.us-east-2.amazonaws.com/messages.log'

# prep: read in the log file
tmp = os.getenv('TMP', '/tmp')
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    URL,
    logfile
)

with open(logfile,
          mode='rt',
          encoding='utf-8') as f:
          loglines = f.readlines()


# coding exercise
def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """

    # Find and extract the date string
    date_match_object = DATE_RE.search(line)
    date_string = date_match_object.group(0)
    date_value_list = date_string.split('-')

    # Find and extract the time string
    time_match_object = TIME_RE.search(line)
    time_string = time_match_object.group(0)
    time_value_list = time_string.split(':')

    # Convert each date & time value to an integer
    date_value_ints = [int(d) for d in date_value_list]
    time_value_ints = [int(t) for t in time_value_list]

    # Create a datetime object with list unpacking
    date_time = datetime(*date_value_ints, *time_value_ints)
    
    return (date_time)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """

    # Find all shutdown events in the log
    shutdown_events = [
        event for event in loglines if SHUTDOWN_EVENT in event
    ]

    # Extract the first and last shutdown events
    first_shutdown_event = shutdown_events[0]
    last_shutdown_event = shutdown_events[-1]

    # Extract the timestamps from the log events
    first_shutdown_date_time = convert_to_datetime(first_shutdown_event)
    last_shutdown_date_time = convert_to_datetime(last_shutdown_event)

    # Calculate the time delta between the most recent and oldest event
    shutdown_delta = last_shutdown_date_time - first_shutdown_date_time

    return shutdown_delta


def main():
    """Main program execution:
       1. Call the function to calculate the shutdown time delta.
       2. Display the returned object type.
       3. Display the returned time delta
    """

    shutdown_delta = time_between_shutdowns(loglines)
    print('\n"shutdown_delta" object type: '
          f'{type(shutdown_delta)}')
    print('Delta between first and most recent shutdown: '
          f'{shutdown_delta}\n')


if __name__ == '__main__':
    main()
