#!/usr/bin/env python3

# Imports
from actors import Creature, Wizard, Dragon
import random


def main():
    print_header()
    game_loop()


def print_header():
    print('-------------------\n'
          '    WIZARD GAME    \n'
          '-------------------\n')


def game_loop():
    creatures = [
         Creature('Bat', 5),
         Creature('Toad', 1),
         Creature('Tiger', 12),
         Dragon('Dragon', 50, 2, False),
         Wizard('Evil Wizard', 1000, )
    ]

    # Create the player character
    hero = Wizard('Galdolf', 75)

    while True:

        # Randomly choose a creature
        active_creature = random.choice(creatures)

        print(f'A {active_creature.name} of level {active_creature.level} '
              f'has appeared from a dark and foggy forest...\n')

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print(f'The wizard defeated the {active_creature.name}')
            else:
                print(f'The mighty {active_creature.name} '
                      f'of level {active_creature.level} defeats {hero.name}')
        elif cmd == 'r':
            print('The wizard has become unsure of his powers and flees!!!')
        elif cmd == 'l':
            print(f'The wizard {hero.name} '
                  f'takes in the surroundings and sees:')
            for index, creature in enumerate(creatures):
                print(f'{index +1}. {creature.name} of level {creature.level}')
            print()
        else:
            # print('Okay, exiting game...bye!\n')
            # break
            raise ValueError('Invalid entry')

        if not creatures:
            print('You\'ve defeated all of the creatures, well done!')

        print()


if __name__ == '__main__':
    main()
