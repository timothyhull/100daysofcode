#!/usr/bin/env python3
""" Parse the contents of XML RSS feeds. """

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


def parse_rss_xml(
    xml_data: str
) -> None:
    """ Parse RSS XML data with feedparser and print formatted
    contents.
    """

    # Parse the xml_data contents with feedparser
    rss_data = feedparser.parse(
        url_file_stream_or_string=xml_data
    )

    try:
        # Display a subset of the parsed data
        print()
        for index, entry in enumerate(rss_data.entries):
            print(f'{entry.title}')
            print(f'{"=" * len(entry.title)}')
            print(f' - Timestamp: {entry.published}')
            print(f' - Link: {entry.link}\n')

    except AttributeError:
        print(f'** Required attribute missing for object {index} **')
        raise

    return None


def main() -> None:
    """ Main program.

        Run the required functions in the correct order.

        Args:
            None.

        Returns:
            None.
    """

    # Collect the raw XML RSS data
    xml_data = read_xml_file()

    # Parse and display the RSS XML data
    parse_rss_xml(
        xml_data=xml_data
    )

    return None


if __name__ == '__main__':
    main()
