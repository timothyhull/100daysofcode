#!/usr/bin/env python3

"""A fun project would be to create yourself a Pomodoro Timer
   that incorporates datetime rather than just the time module.
   Have it display timestamps.
"""

# Reference - https://en.wikipedia.org/wiki/Pomodoro_Technique

# Declare timer constants for work and break time
# Constants
WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 15
MAX_SHORT_BREAKS = 4


# Banner generator
def generate_banner(message: str) -> str:
    print(f'\n{message}\n'
          f'{"-" * len(message)}\n')


# Display intro
def display_intro() -> None:
    generate_banner('*** Pomodoro Timer ***')


# Graceful exit
def end_pomodoro() -> None:
    generate_banner('*** End Pomodoro Timer ***')


# Display instructions
def display_instructions() -> None:
    prompt = 'Press Return/Enter to start or any other key to exit.'


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


if __name__ == '__main__':
    main()
