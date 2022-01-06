#!/usr/bin/env python3
""" User interface for the Movie Search application. """

# Imports - Python Standard Library
from sys import exit

# Imports - Third-Party

# Imports - Local

# Constants


def display_keyboard_interrupt_message() -> None:
    """ Display an invalid input error message.

        Args:
            None.

        Returns:
            None.
    """

    print(
        '\nRead keyboard interrupt sequence, exiting program.\n'
    )

    return None


def display_banner() -> None:
    """ Display an application banner.

        Args:
            None.

        Returns:
            None.
    """

    # Create a banner message
    msg = '* Movie Search Application *'
    border = f'{"*" * len(msg)}'
    banner = (
        f'\n{border}\n'
        f'{msg}\n'
        f'{border}\n'
    )

    # Display the banner message
    print(banner)

    return None


def invalid_input_error() -> None:
    """ Display an invalid input error message.

        Args:
            None.

        Returns:
            None.
    """

    print(
        '\n** Invalid input, please try again **\n'
    )

    return None


def select_menu_option() -> int:
    """ Display a menu and collect user selection input.

        Args:
            None.

        Returns:
            menu_choice (int):
                User input choice from the menu.
    """

    # Create an input loop
    while True:
        # Display menu
        print(
            '1. Search for a movie by title.\n'
            '2. Search for a movie by director name.\n'
            '3. Search for a movie by IMDB code.\n'
        )

        # Prompt for menu selection input
        menu_choice = input('Choose a search option (1-3): ')

        # Attempt to convert the input to an integer
        try:
            menu_choice = int(menu_choice)
        except ValueError:
            invalid_input_error()
            continue

        if menu_choice in range(1, 4):
            break
        else:
            invalid_input_error()
            continue

    return menu_choice


def main() -> None:
    """ Main program function.

        Runs application functions in the proper sequence.

        Args:
            None.

        Returns:
            None
    """

    # Display the banner when the program starts
    display_banner()

    # Collect a user search menu selection
    try:
        menu_choice = select_menu_option()
        print(menu_choice)
    except KeyboardInterrupt:
        display_keyboard_interrupt_message()
        exit()

    # TODO - Collect a user search keyword

    # TODO - Display results

    return None


if __name__ == '__main__':
    main()
