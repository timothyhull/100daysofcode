#!/usr/bin/env python3
""" Banner Display for the DT FL DB Application. """


def display_banner(
    banner_string: str
) -> str:
    """ Display a welcome banner.

        Args:
            banner_string (str):
                String for the banner display.

        Returns:
            banner (str).
                Banner to write to STDOUT.
    """

    # Create horizontal and vertical rule strings
    horizontal_rule = f'{(len(banner_string) + 4) * "-"}'
    vertical_rule = f'| {banner_string} |'

    # Create and display full banner string
    banner = (
        f'\n{horizontal_rule}\n'
        f'{vertical_rule}\n'
        f'{horizontal_rule}\n'
    )

    return banner
