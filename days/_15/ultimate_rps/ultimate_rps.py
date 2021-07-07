#!/usr/bin/env python3
""" Ultimate Rock, Paper, Scissors game (Ultimate RPS).

    Usage:
        python3 ultimate_rps.py
"""

from UltimateRPS import UltimateRPS, Player


def main():
    """ Main program run.
    """

    # Create object from the UltimateRPS class
    ultimate_rps = UltimateRPS()
    print(ultimate_rps)

    # Create object from the Player class
    player_1 = Player()
    player_2 = Player()
    print(player_1, player_2)


if __name__ == '__main__':
    main()
