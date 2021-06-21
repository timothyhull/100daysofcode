#!/usr/bin/env python3

# Imports
from actors import Creature


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
         Creature('Dragon', 50),
         Creature('Evil Wizard', 1000)
    ]

    print(creatures)

    hero = None  # TODO: create a hero

    while True:

        # Ask user for action
        active_creature = None

        print(f'A {None} of level {None} has appeared from a dark and foggy forest...\n')

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            pass
            # TODO: attack
        elif cmd == 'r':
            print('The wizard has become unsure of his powers and flees!!!')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            # TODO: show the creatures in the room
        else:
            print('Okay, exiting game...bye!\n')
            break

        if not creatures:
            print('You\'ve defeated all of the creatures, well done!')

        print()


if __name__ == '__main__':
    main()
