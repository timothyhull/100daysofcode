#!/usr/bin/env python3
""" Pull and aprse XML from RSS feed.
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
    """ Get RSS feed from source.

        Args:
            None.

        Returns:
            rss_xml (str):
                XML text retrieved by the HTTP GET for the RSS feed.
    """

    # Send HTTP GET request to the RSS feed.
    response = requests.get(
        url=URL,
        timeout=TIMEOUT
    )

    # Raise an HTTPError exception for HTTP status codes 400+
    response.raise_for_status()

    # Assign the response.text XML string to a variable
    rss_xml = response.text

    return rss_xml


def write_rss_to_xml(
    rss_xml: str
) -> None:
    """ Write RSS XML data to a local file.

        Args:
            rss_xml (str):
                Raw XML-formatted RSS text string.

        Returns:
            None.
    """

    # Create a file for writing with a context manager
    with open(
        file=XML_FILE,
        mode='wt',
        encoding='utf-8'
    ) as xml_file:

        # Write/overwrite the RSS XML content to the file
        xml_file.write(rss_xml)

    return None


def main() -> None:
    """ Main program.

        Run the required functions in the correct order.

        Args:
            None.

        Returns:
            None.
    """

    # Get the RSS feed XML
    rss_xml = get_rss_feed()

    # Write the RSS feed XML to a file
    write_rss_to_xml(
        rss_feed=rss_xml
    )

    return None


if __name__ == '__main__':
    main()
