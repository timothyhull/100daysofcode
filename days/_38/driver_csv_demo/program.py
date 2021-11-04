#!/usr/bin/env python3
""" Bad Driver application. """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from _38.driver_csv_demo.app.bad_drivers import BadDrivers


def main():
    """ Main program. """

    # Display header message
    header_msg = '** Bad Driver Data **'
    print(
        f'\n{header_msg}\n'
        f'{"-" * len(header_msg)}\n'
    )

    # Create instance of BadDrivers
    bad_drivers = BadDrivers()

    # Display top 5 states for fatal collisions without alcohol involved
    print(
        'Top 5 states for fatal collisions without alcohol involved '
        'per billion miles:'
        )

    for i, r in enumerate(bad_drivers.top_n_driver_fatal_states_no_alc(), 1):
        print(f'  {i}. {r.state} ({r.value})')
    print()

    # Display top 5 states for fatal collisions with alcohol involved
    print(
        'Top 5 states for fatal collisions with alcohol involved '
        'per billion miles:'
        )

    for i, r in enumerate(bad_drivers.top_n_driver_fatal_states_with_alc(), 1):
        print(f'  {i}. {r.state} ({r.value})')
    print()

    # Display top 5 states for car insurance premiums
    print(
        'Top 5 states for car insurance premiums:'
        )

    for i, r in enumerate(bad_drivers.top_n_car_insurance_premium_states(), 1):
        print(f'  {i}. {r.state} (${r.value}/year)')
    print()


if __name__ == '__main__':
    main()
