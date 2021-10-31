#!/usr/bin/env python3
""" Weather research data """

# Imports - Python Standard Library
import csv
import os

# Constants
CSV_FILE = 'seattle.csv'
CSV_FOLDER = 'data'

# Define an empty list for weather data
data = []


def init():
    """ Initialize weather data """

    # Specify path to CSV data file
    csv_file = CSV_FILE
    csv_folder = CSV_FOLDER
    base_folder = os.path.dirname(__file__)
    file_name = os.path.join(base_folder, csv_folder, csv_file)

    # Open the CSV file
    with open(
         file=file_name,
         mode='rt',
         encoding='utf-8') as file:

        # Use the csv.DictReader function to convert CSV data to a dictionary
        reader = list(csv.DictReader(file))

        # for row in reader:
        #     print(f'ROW --> {type(row.get("actual_min_temp"))}')
        #     break

    print(f'The reader object type is: {type(reader)}')
    print()

    for row in reader:
        print(f'The row object type is {type(row)}')
        print()

        print('The row data is:')
        print(row)
        print()

        print(
            'The value object type for the "actual_min_temp" key is: '
            f'{type(row.get("actual_min_temp"))}'
        )
        print()
        break
