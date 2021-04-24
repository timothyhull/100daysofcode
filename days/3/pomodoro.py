#!/usr/bin/env python3

"""A fun project would be to create yourself a Pomodoro Timer
   that incorporates datetime rather than just the time module.
   Have it display timestamps.

    Usage:
        ./pomodoro.py [work_minutes short_break_minutes long_break_minutes]
"""

# Reference - https://en.wikipedia.org/wiki/Pomodoro_Technique
# Standard timer values - work:25, short break:4, long break:15

# Imports
from datetime import datetime, timedelta
from time import sleep
import sys
import termios
import tty

# Constants
if len(sys.argv) == 4:
    WORK_TIME = float(sys.argv[1])
    SHORT_BREAK_TIME = float(sys.argv[2])
    LONG_BREAK_TIME = float(sys.argv[3])
else:
    WORK_TIME = 25
    SHORT_BREAK_TIME = 4
    LONG_BREAK_TIME = 15

MAX_SHORT_BREAKS = 4
TIMERS = {
    'work': {
        'name': 'Work',
        'time': WORK_TIME
    },
    'short_break': {
        'name': 'Short break',
        'time': SHORT_BREAK_TIME
    },
    'long_break': {
        'name': 'Long break',
        'time': LONG_BREAK_TIME
    }
}


def generate_banner(message: str) -> None:
    """Generate and print a formatted banner from a string.

    Args:
        message: String message to format in the banner.

    Returns:
        None
    """

    # Set the border width
    new_line_position = message.find('\n')
    if new_line_position > 0:
        banner_width = new_line_position
    else:
        banner_width = len(message)

    # Display banner
    banner_border = f'{"-" * banner_width}'
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
        generate_banner(f'*** Exit due to "{exception!r}" ***')

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
    

def timer(timer_type: str, count: int) -> None:
    """Prompt to start a timer by pressing a specific key
       Exit the program for any other key

    Args:
        timer_type: string declaring the type of timer which triggers
                    the corresponding countdown time.
        timer_count: integer declaring the number of iterations for
                     a given timer.

    Returns:
        None
    """

    # Set timer type and time interval
    timer = TIMERS.get(timer_type)
    time_interval = 'minutes'
    if timer.get('time') == 1:
        time_interval = time_interval[0:-1]

    # Prompt for keystroke input
    print('Press Return/Enter to start '
          f'{timer.get("name").lower()} '
          f'timer # {count} ({timer.get("time")} {time_interval}) ' 
          'or any other key to exit: ')

    # Get keystroke
    keystroke = get_keystroke()
    # print(f'You pressed {keystroke!r}')

    # End the program if the keystroke is not Return/Enter
    if keystroke != '\r':
        end_pomodoro()


    # Set and timer type, start time, and end time
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=timer.get('time'))

    # Display timer type, start time, and end time banner
    generate_banner(
        f'{timer.get("name")} '
        f'timer started at {start_time.strftime("%A, %b %d at %H:%M:%S")}\n'
        f'{timer.get("name")} '
        f'timer ends at {end_time.strftime("%A, %b %d at %H:%M:%S")}'
    )

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
        print('\n')


# Display the number of breaks and the break duration when the timer expires


def main() -> None:
    """Main program
    """

    # Display intro at program start
    display_intro()

    # Initialize main program loop counters
    work_count = 1
    short_break_count = 1
    long_break_count = 1

    # Start main program loop
    while True:
        # Work timer
        timer('work', work_count)
        work_count += 1
    
        # Long break timer runs after MAX_SHORT_BREAKS short break cycles
        if short_break_count % MAX_SHORT_BREAKS == 0:
            timer('long_break', long_break_count)
            long_break_count += 1
            continue

        # Short break timer
        timer('short_break', short_break_count)
        short_break_count += 1


if __name__ == '__main__':
    main()
