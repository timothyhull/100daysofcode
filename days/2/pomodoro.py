#!/usr/bin/env python3

"""A fun project would be to create yourself a Pomodoro Timer
   that incorporates datetime rather than just the time module.
   Have it display timestamps.
"""

# Reference - https://en.wikipedia.org/wiki/Pomodoro_Technique

# Imports
import sys
import termios
import tty

# Declare timer constants for work and break time
# Constants
WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 15
MAX_SHORT_BREAKS = 4


# Banner generator
def generate_banner(message: str) -> str:
    banner_border = f'{"-" * len(message)}'
    print(f'\n{banner_border}\n'
          f'{message}\n'
          f'{banner_border}\n')


# Display intro
def display_intro() -> None:
    generate_banner('*** Pomodoro Timer ***')


# Graceful exit
def end_pomodoro(exception: None = None) -> None:
    if exception is None:
        generate_banner('*** End Pomodoro Timer ***')
    else:
        generate_banner(f'*** {exception!r} ***')

    sys.exit(0)


# Get single keystroke input
def get_keystroke() -> str:
    # Get the underlying file descriptor, if one exists
    file_descriptor = sys.stdin.fileno()

    # Save a copy of the original terminal attributes
    original_terminal_attributes = termios.tcgetattr(file_descriptor)

    # Try to collect a keystroke
    try:
        # Put the terminal in raw mode
        tty.setraw(file_descriptor)

        # Collect exactly one keystroke
        keystroke = sys.stdin.read(1)
    finally:
        # Always restore original attributes after keystroke input attempt
        termios.tcsetattr(
            file_descriptor,
            termios.TCSADRAIN,
            original_terminal_attributes
        )

        return keystroke


# Display instructions
def display_instructions() -> None:
    # Prompt for keystroke input
    print('Press Return/Enter to start or any other key to exit: ')

    # Get keystroke
    keystroke = get_keystroke()
    print(f'You pressed {keystroke!r}')

    if keystroke != '\r':
        end_pomodoro()
        

# Prompt to start a timer by pressing a specific key
    # Exit the program for any other key
def start_prompt() -> None:
    pass


# Start the timer and display a timestamp

# Display the number of minutes and seconds remaining

# Display an alert with audio when the work timer expires

# Display the number of breaks and the break duration when the timer expires

# Display an alert with audio when the timer expires and the work timer starts

# Handle ctrl-c events to gracefully exit


def main() -> None:
    display_intro()
    display_instructions()


if __name__ == '__main__':
    main()
