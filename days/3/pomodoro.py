#!/usr/bin/env python3

"""A fun project would be to create yourself a Pomodoro Timer
   that incorporates datetime rather than just the time module.
   Have it display timestamps.
"""

# Reference - https://en.wikipedia.org/wiki/Pomodoro_Technique

# Imports
from datetime import datetime, timedelta
from time import sleep
import sys
import termios
import tty

# Declare timer constants for work and break time
# Constants
WORK_MINUTES = 1
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 15
MAX_SHORT_BREAKS = 4


def generate_banner(message: str) -> None:
    """Generate and print a formatted banner from a string.

    Args:
        message: String message to format in the banner.

    Returns:
        None
    """
    banner_border = f'{"-" * len(message)}'
    print(f'\n{banner_border}\n'
          f'{message}\n'
          f'{banner_border}\n')


def display_intro() -> None:
    """Display intro banner
    """

    generate_banner('*** Pomodoro Timer ***')


def end_pomodoro(exception: None = None) -> None:
    """Gracefully exit the program

    Args:
        exception: Optionally pass an exception object to display exit cause.
            default: None

    Returns:
        None
    """
    if exception is None:
        generate_banner('*** End Pomodoro Timer ***')
    else:
        generate_banner(f'*** {exception!r} ***')

    sys.exit(0)


def get_keystroke() -> str:
    """Get single keystroke input

    Args:
        None

    Returns:
        keystroke: String representing keystroke.
    """
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


def start_prompt() -> None:
    """Prompt to start a timer by pressing a specific key
       Exit the program for any other key

    Args:
        None

    Returns:
        None
    """
    # Prompt for keystroke input
    print('Press Return/Enter to start or any other key to exit: ')

    # Get keystroke
    keystroke = get_keystroke()
    # print(f'You pressed {keystroke!r}')

    # End the program if the keystroke is not Return/Enter
    if keystroke != '\r':
        end_pomodoro()
    

def work_timer() -> None:
    """Timer for working time

    Args:
        None

    Returns:
        None
    """

    # Set and displaythe start and end times
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=WORK_MINUTES)

    print(f'Timer started at {start_time.strftime("%A, %b %d at %H:%M:%S")}')
    print(f'Timer ends at {end_time.strftime("%A, %b %d at %H:%M:%S")}')

    try:
        while end_time >= datetime.now():
            time_remaining = end_time - datetime.now()
            minutes_remaining = time_remaining.seconds // 60
            seconds_remaining = time_remaining.seconds % 60

            print(f'Time remaining: '
                  f'{minutes_remaining}:'
                  f'{seconds_remaining:02d}', end='\r')
            sleep(1)
    except KeyboardInterrupt as e:
        end_pomodoro(e)
    finally:
        print('\a')


# Display the number of minutes and seconds remaining

# Display an alert with audio when the work timer expires

# Display the number of breaks and the break duration when the timer expires

# Display an alert with audio when the timer expires and the work timer starts

# Handle ctrl-c events to gracefully exit


def main() -> None:
    display_intro()
    start_prompt()
    work_timer()


if __name__ == '__main__':
    main()
