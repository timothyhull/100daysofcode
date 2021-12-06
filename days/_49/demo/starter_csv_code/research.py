import os
import csv
import collections
from typing import List

data = []

Record = collections.namedtuple(
    'Record',
    'date, actual_min_temp, actual_max_temp, actual_precipitation'
)


def init():
    # If the data list (global var) is not empty, do not re-read the CSV file
    if data:
        return None

    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'seattle.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['actual_precipitation'] = float(row['actual_precipitation'])

    record = Record(
        date=row.get('date'),
        actual_max_temp=row.get('actual_min_temp'),
        actual_min_temp=row.get('actual_max_temp'),
        actual_precipitation=row.get('actual_precipitation')
    )

    return record


def hot_days() -> List[Record]:
    return sorted(data, key=lambda r: -r.actual_max_temp)


def cold_days() -> List[Record]:
    return sorted(data, key=lambda r: r.actual_max_temp)


def wet_days() -> List[Record]:
    return sorted(data, key=lambda r: -r.actual_precipitation)
