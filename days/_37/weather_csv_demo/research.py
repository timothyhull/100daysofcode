#!/usr/bin/env python3
"""
"""

# Imports - Python Standard Library
import os

data = []


def init():
    """
    """

    # Specify path to CSV data file
    csv_file = 'seattle.csv'
    csv_folder = 'data'
    base_folder = os.path.dirname(__file__)
    file_name = os.path.join(base_folder, csv_folder, csv_file)

    # Open the file
    with open(
        file=file_name,
        mode='rt',
        encoding='utf-8'
    ) as file:

        # Store the file contents in a list of file lines
        csv_data = file.readlines()

    # Display the CSV headers
    print(csv_data[0])
