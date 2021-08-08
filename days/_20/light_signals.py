#!/usr/bin/env python3
""" Traffic light graphics
"""

# Imports
from typing import Union

# Constants
RED_ANSI = '48;5;9'
YELLOW_ANSI = '48;5;11'
GREEN_ANSI = '48;5;10'


class TrafficLights:
    """ Object to display colored ASCII traffic lights.

        Usage:
            # Instantiate a TrafficLights object:
                lights = TrafficLights()

            # Use color methods to display a light:
                lights.red()
    """

    def __init__(self) -> None:
        # Create traffic lights
        pass

    # ANSI escape sequence for text formatting
    def __esc__(self, code: Union[str, int]) -> str:
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

        Returns:
            code (str): ANSI-formatted escape code.

            Example:
                \033[48;5;9;38;5;15m
        """

        ansi_code = f'\033[{code}m'

        return ansi_code

    def __activate_light__(self, ansi_color: str) -> str:
        """ Create a traffic light color block to fill an ASCII trafic light
            placeholder graphic.

            Args:
                ansi_color (str):
                    ANSI-formatted background color string.

            Returns:
                light (str):
                    Colored active light string

        """

        light = f"""
| {self.__esc__(ansi_color)}      {self.__esc__(0)} |
| {self.__esc__(ansi_color)}      {self.__esc__(0)} |
    """.strip()

        return light

    def red(self) -> None:
        """ Method of a TrafficLights object that displays the ASCII graphic
            for a red traffic light.

            Args:
                None.

            Returns:
                None.
        """

        self.red_light = f"""
|¯¯¯¯¯¯¯¯|
{self.__activate_light__(ansi_color=RED_ANSI)}
|        |
| |¯¯¯¯| |
| |____| |
|        |
| |¯¯¯¯| |
| |____| |
|________|
"""
        print(self.red_light)

    def yellow(self) -> None:
        """ Method of a TrafficLights object that displays the ASCII graphic
            for a yellow traffic light.

            Args:
                None.

            Returns:
                None.
        """

        self.yellow_light = f"""
|¯¯¯¯¯¯¯¯|
| |¯¯¯¯| |
| |____| |
|        |
{self.__activate_light__(ansi_color=YELLOW_ANSI)}
|        |
| |¯¯¯¯| |
| |____| |
|________|
"""
        print(self.yellow_light)

    def green(self) -> None:
        """ Method of a TrafficLights object that displays the ASCII graphic
            for a green traffic light.

            Args:
                None.

            Returns:
                None.
        """

        self.green_light = f"""
|¯¯¯¯¯¯¯¯|
| |¯¯¯¯| |
| |____| |
|        |
| |¯¯¯¯| |
| |____| |
|        |
{self.__activate_light__(ansi_color=GREEN_ANSI)}
|________|
"""
        print(self.green_light)
