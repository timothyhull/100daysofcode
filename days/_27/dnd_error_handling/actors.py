#!/usr/bin/env python3

# Imports
import random


# Establish a super class which establishes common traits among all creatures
class Creature:

    # Initialize properties (to `self`) which are common to all creatures
    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level

    # Estabilsh a method which produces a roll of a 12-sided die
    def defensive_roll(self):
        roll = random.randint(1, 12)

        # Return the value of the die roll
        return roll * self.level


# Establish a class for a dragon, which inherits the `Creature` class
class Dragon(Creature):

    def __init__(
        self,
        name: str,
        level: int,
        scaliness: int,
        breathes_fire: bool
    ) -> None:

        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    # Inherit the `Creature.defensive_roll` method (as `super()`) and add to it
    def defensive_roll(self):
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breathes_fire is True:
            value = value * 2

        return value


# Establish a class for a wizard, which inherits from the `Creature` class
class Wizard(Creature):

    # The `attack` method compares a player roll with a creature roll
    def attack(self, creature) -> bool:
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        print(f'\nPlayer rolls: {my_roll}\n'
              f'Enemy rolls {their_roll}\n')

        # Returns True or False, based on the outcome of the roll comparision
        return my_roll >= their_roll
