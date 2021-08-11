#!/usr/bin/env python3
""" Write a function called friends_teams that takes a list of friends,
    a team_size (type int, default=2) and order_does_matter
    (type bool, default False).

    Return all possible teams.
    Hint: if order matters (order_does_matter=True), the number of
    teams would be greater.
"""

# Imports
from itertools import combinations, permutations

friends = 'john paul george ringo'.split()


def friends_teams(
    friends: list,
    team_size: int = 2,
    order_does_matter: bool = False
) -> tuple:

    if order_does_matter is False:
        teams = combinations(friends, r=team_size)
    else:
        teams = permutations(friends, r=team_size)

    return list(teams)


def main():
    print(friends_teams(friends, order_does_matter=False))


if __name__ == '__main__':
    main()
