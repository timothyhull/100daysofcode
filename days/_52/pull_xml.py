#!/usr/bin/env python3
"""
"""

# Imports - Python Standard Library

# Imports - Third-Party
import requests

# Imports - Local

# Constants
TIMEOUT = 5
URL = 'http://www.va.gov/rss/rss_PressRel.asp'


def get_rss_feed() -> requests.Response:
    """
    """

    response = requests.get(
        url=URL,
        timeout=TIMEOUT
    )

    response.raise_for_status()


def write_rss_to_xml(
    rss_feed: str
) -> None:
    """
    """

    with open()

    return None


def main() -> None:
    """
    """

    rss_feed = get_rss_feed()
    write_rss_to_xml(rss_feed=rss_feed)

    return None


if __name__ == '__main__':
    main()
