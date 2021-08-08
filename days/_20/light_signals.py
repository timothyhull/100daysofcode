#!/usr/bin/env python3
""" Traffic light graphics
"""

# Imports
from typing import Union

# Constants
RED_ANSI = '48;5;9'
YELLOW_ANSI = '48;5;11'
GREEN_ANSI = '48;5;10'


# ANSI escape sequence for text formatting
def esc(code: Union[str, int]) -> str:
    """ Formats a string using an ANSI escape code, to colored/formatted output.
        ANSI code reference: https://en.wikipedia.org/wiki/ANSI_escape_code

    Args:
        code:
            Option #1 (str):
                Single ANSI code or semicolon-separated list of codes.
            Option #2 (int):
                Any single ANSI code.

        Example:
            code = '48;5;9;38;5;15'

    Prints:
        None.

    Returns:
        code (str): ANSI-formatted escape code.

        Example:
            \033[48;5;9;38;5;15m
    """

    ansi_code = f'\033[{code}m'

    return ansi_code


def activate_light(ansi_color: str = RED_ANSI) -> str:
    """ Create a traffic light color block.

        Args:
            ansi_color (str):
                ANSI-formatted background color string.

        Returns:
            light (str):
                Colored active light string

    """

    light = f"""
| {esc(ansi_color)}      {esc(0)} |
| {esc(ansi_color)}      {esc(0)} |
""".strip()

    return light


class TrafficLights:
    """
    """

    def __init__(self) -> None:
        # Create traffic lights
        pass

    def red_light(self):
        """
        """

        self.red_light = f"""
|¯¯¯¯¯¯¯¯|
{activate_light(ansi_color=RED_ANSI)}
|        |
| |¯¯¯¯| |
| |____| |
|        |
| |¯¯¯¯| |
| |____| |
|________|
"""
        print(self.red_light)

    def yellow_light(self):
        """
        """
        self.yellow_light = f"""
|¯¯¯¯¯¯¯¯|
| |¯¯¯¯| |
| |____| |
|        |
{activate_light(ansi_color=YELLOW_ANSI)}
|        |
| |¯¯¯¯| |
| |____| |
|________|
"""
        print(self.yellow_light)

    def green_light(self):
        """
        """

        self.green_light = f"""
|¯¯¯¯¯¯¯¯|
| |¯¯¯¯| |
| |____| |
|        |
| |¯¯¯¯| |
| |____| |
|        |
{activate_light(ansi_color=GREEN_ANSI)}
|________|
"""
        print(self.green_light)
