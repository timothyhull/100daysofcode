#!/usr/bin/env python3

# Imports - Local
from _37.weather_csv_demo import research


def main():
    print()
    print('Weather research for Seattle, 2014-2015')
    print()

    # Initialize the data
    data = research.init()

    # Get and display the 5 hottest days
    hot_days = research.hot_days(
        weather_data=data,
        result_count=5
    )
    print('The hottest 5 days:')
    for index, day in enumerate(hot_days, 1):
        print(
            f'  {index}. Date: {day.date}, Temperature: {day.actual_max_temp}'
        )
    print()

    # Get and display the 5 coldest days
    print('The coldest 5 days:')
    cold_days = research.cold_days(
        weather_data=data,
        result_count=5
    )
    for index, day in enumerate(cold_days, 1):
        print(
            f'  {index}. Date: {day.date}, Temperature: {day.actual_min_temp}'
        )
    print()

    # Get and display the 5 wettest days
    print('The wettest 5 days:')
    wet_days = research.wet_days(
        weather_data=data,
        result_count=5
    )
    for index, day in enumerate(wet_days, 1):
        print(
            f'  {index}. Date: {day.date}, '
            f'Actual Precipitation: {day.actual_precipitation}"'
        )
    print()


if __name__ == '__main__':
    main()
