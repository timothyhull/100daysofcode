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
XML_FILE = './rss_feed.xml'


def get_rss_feed() -> str:
    """
    """

    response = requests.get(
        url=URL,
        timeout=TIMEOUT
    )

    response.raise_for_status()

    return response.text


def write_rss_to_xml(
    rss_feed: str
) -> None:
    """
    """

    with open(
        file=XML_FILE,
        mode='wt',
        encoding='utf-8'
    ) as xml_file:

        xml_file.write(rss_feed)

    return None


def main() -> None:
    """
    """

    rss_feed = get_rss_feed()
    write_rss_to_xml(rss_feed=rss_feed)

    return None


if __name__ == '__main__':
    main()
