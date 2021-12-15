#!/usr/bin/env python3
""" Parse the contents of XML RSS feeds.
"""

# Imports - Python Standard Library

# Imports - Third-Party
import feedparser

# Imports - Local
from os import path
from pathlib import Path

# Constants
XML_BASE_PATH = Path(path.dirname(__file__))
XML_DIR_NAME = 'RSS_XML'
XML_FILE_NAME = 'rss_feed.xml'
XML_FILE = path.join(XML_BASE_PATH, XML_DIR_NAME, XML_FILE_NAME)


def read_xml_file(
    xml_file: str = XML_FILE
) -> str:
    """ Read the contents of an XML RSS file.

        Args:
            xml_file (str, optional).
                Reads data from a file, using the XML_FILE path as the
                default XML file to parse.

        Returns:
            xml_data (str).
                Content from the XML file defined by the xml_file
                argument.
    """

    # Read the XML file with a context manager
    with open(
        file=xml_file,
        mode='rt',
        encoding='utf-8'
    ) as xml_rss_file:
        # Assign the file contents to a variable
        xml_data = xml_rss_file.read()

    return xml_data


def main() -> None:
    """ Main program.

        Run the required functions in the correct order.

        Args:
            None.

        Returns:
            None.
    """

    xml_data = read_xml_file()

    return None
