#!/usr/bin/env pytest
""" pytest tests for parser.py """

# Imports - Python Standard Library

# Imports - Third-Party
from pytest import raises
from unittest.mock import MagicMock, mock_open, patch
import _pytest.capture

# Imports - Local
from _52_53_54.app.parser import (
    parse_rss_xml,
    read_xml_file
)

# Constants
PARSED_SUBJECT = (
    'News Releases from the U.S. Department of '
    'Veterans Affairs.'
)

PARSED_BODY = '''2021 Under Secretary for Health's Robert L. Jesse Award recognizes VA boundary-breaking innovations
===================================================================================================
 - Timestamp: Wed, 8 Dec 2021 10:07:00 EST
 - Link: https://www.va.gov/opa/pressrel/PressArtInternet.cfm?id=5746'''

XML_ASSERTS = [
    '<?xml version="1.0" encoding="ISO-8859-1"?>',
    '<title>VA News Releases</title>'
]

XML = '''
<?xml version="1.0" encoding="ISO-8859-1"?>


<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>VA News Releases</title>
    <link>https://www.va.gov/opa/pressrel/PressArchInternet.cfm</link>
    <description>News Releases from the U.S. Department of Veterans Affairs.
</description>
    <language>en-us</language>
    <copyright>Copyright 2002 VHA</copyright>
    <docs>https://www.va.gov/rss</docs>
    <atom:link href="https://www.va.gov/rss/rss_PressRel.asp" rel="self" type="application/rss+xml" />
<lastBuildDate>Tue, 14 Dec 2021 16:00:00 EST</lastBuildDate>
        <item>
            <title>VA strengthens care for Veterans impacted by intimate partner violence and sexual assault</title>
            <link>https://www.va.gov/opa/pressrel/PressArtInternet.cfm?id=5747</link>
            <description>The Department of Veterans Affairs recently initiated a pilot program to improve services for Veterans who have experienced or are experiencing intimate partner violence or sexual assault.</description>
            <guid>https://www.va.gov/opa/pressrel/PressArtInternet.cfm?id=5747</guid>
            <pubDate>Tue, 14 Dec 2021 16:00:00 EST</pubDate>
        </item>

        <item>
            <title>2021 Under Secretary for Health&apos;s Robert L. Jesse Award recognizes VA boundary-breaking innovations</title>
            <link>https://www.va.gov/opa/pressrel/PressArtInternet.cfm?id=5746</link>
            <description>The Department of Veterans Affairs honored three innovative health care practices and their creators late October with the Robert L. Jesse Award for Excellence in Innovation.</description>
            <guid>https://www.va.gov/opa/pressrel/PressArtInternet.cfm?id=5746</guid>
            <pubDate>Wed, 8 Dec 2021 10:07:00 EST</pubDate>
        </item>

  </channel>
</rss>
'''

XML_ERROR = '''
<?xml version="1.0" encoding="ISO-8859-1"?>


<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>VA News Releases</title>
    <link>https://www.va.gov/opa/pressrel/PressArchInternet.cfm</link>
    <description>News Releases from the U.S. Department of Veterans Affairs.
</description>
    <language>en-us</language>
    <copyright>Copyright 2002 VHA</copyright>
    <docs>https://www.va.gov/rss</docs>
    <atom:link href="https://www.va.gov/rss/rss_PressRel.asp" rel="self" type="application/rss+xml" />
<lastBuildDate>Tue, 14 Dec 2021 16:00:00 EST</lastBuildDate>
        <item>
            <link>https://www.va.gov/opa/pressrel/PressArtInternet.cfm?id=5747</link>
            <description>The Department of Veterans Affairs recently initiated a pilot program to improve services for Veterans who have experienced or are experiencing intimate partner violence or sexual assault.</description>
            <guid>https://www.va.gov/opa/pressrel/PressArtInternet.cfm?id=5747</guid>
        </item>

  </channel>
</rss>
'''


@patch(
    'builtins.open',
    side_effect=mock_open(
        read_data=XML
    )
)
def test_read_xml_file(
    mock_xml_file_data: MagicMock
) -> None:
    """ Test the read_xml_file function with mock data.

        Check content for expected XML data.

        Args:
            mock_xml_file_data (MagicMock):
                pytest patch fixture with mock XML file data

        Returns:
            None.
    """

    # Return the mocked XML from the read_xml_file function
    xml = read_xml_file()

    # Assert the expected content is in the mocked file contents
    for xml_assert in XML_ASSERTS:
        assert xml_assert in xml

    return None


def test_parse_rss_xml() -> None:
    """ Test the parse_rss_xml function.

        Args:
            None

        Returns:
            None.
    """

    # Call the function to return a namedtuple
    parsed_rss = parse_rss_xml(
        xml_data=XML
    )

    assert PARSED_SUBJECT in parsed_rss.email_subject
    assert PARSED_BODY in parsed_rss.email_body

    return None


def test_parse_rss_xml_output(
    capsys: _pytest.capture.CaptureFixture
) -> None:
    """ Test the parse_rss_xml function output.

        Args:
            capsys (_pytest.capture.CaptureFixture):
                pytest fixture to capture writes to sys.stdout and
                sys.stderr.

        Returns:
            None.
    """

    # Call the function to produce STDOUT output
    parse_rss_xml(
        xml_data=XML
    )

    # Capture STDOUT output
    output = capsys.readouterr().out

    # Assert the expected output is in STDOUT
    assert PARSED_SUBJECT in output
    assert PARSED_BODY in output

    return None


def test_parse_rss_xml_errors() -> None:
    """ Test the parse_rss_xml function's error handling.

        Args:
            None.

        Returns:
            None.
    """

    # Call the function to create an exception
    with raises(AttributeError):
        parse_rss_xml(
            xml_data=XML_ERROR
        )
