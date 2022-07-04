#!/usr/bin/env python3
""" Main menu display for the DT FL DB Application. """

# Imports - Local
from _81.DTFLDB.display_banner import display_banner
from _81.DTFLDB.output_messages import invalid_menu_input
from _81.DTFLDB.quit_program import quit_program


def display_main_menu() -> int:
    """ Display a menu of options.

        Args:
            None.

        Returns:
            menu_choice (int):
                Menu choice.
    """

    try:
        while True:
            # Display a menu
            msg = display_banner(
                banner_string='** Main Menu **'
            )
            print(msg)

            print(
                '\n'
                '1. Display all DB entries\n'
                '2. Display a specific DB entry\n'
                '3. Add a new DB entry\n'
                '4. Update a specific DB entry\n'
                '5. Delete a specific DB entry\n'
                '6. Quit'
                '\n'
            )

            # Get menu selection
            menu_choice = input(
                'Enter a menu selection: '
            )

            # Validate menu selection
            if not menu_choice:
                print(invalid_menu_input())
                continue
            else:
                try:
                    # Determine if the menu selection is an integer
                    menu_choice = int(menu_choice)
                except ValueError:
                    print(invalid_menu_input())
                    continue
                # Determine if the menu selection is within the range of 1-6
                if not 1 <= menu_choice <= 6:
                    print(invalid_menu_input())
                    continue

            return menu_choice

    except KeyboardInterrupt:
        # Display a message and exit the application
        quit_program()
