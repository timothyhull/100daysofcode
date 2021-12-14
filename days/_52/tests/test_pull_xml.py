#!/usr/bin/env python3
""" pytest tests for pull_xml.py
"""

# Imports - Python Standard Library
from unittest.mock import MagicMock, mock_open, patch

# Imports - Third-Party
from pytest import raises
from requests.exceptions import HTTPError
import requests_mock.mocker

# Imports - Local
from _52.app.pull_xml import (
    URL, get_rss_feed
)

# Constants
XML_ASSERTS = [
    '<?xml version="1.0" encoding="ISO-8859-1"?>',
    '<title>VA News Releases</title>'
]
XML = '''
<?xml version="1.0" encoding="ISO-8859-1"?>


<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
    <title>VA News Releases</title>
    </channel>
</rss>
'''


def test_get_rss_feed_successful(
    requests_mock: requests_mock.mocker.Mocker
) -> None:

    """ Tests the get_rss_feed function using a mock HTTP request.

        Tests a successful HTTP response.

        Args:
            requests_mock (requests_mock.mocker.Mocker):
                pytest fixture to mock requests class HTTP requests.

        Returns:
            None.
    """

    # Create a successful mock HTTP request
    requests_mock.get(
        url=URL,
        text=XML
    )

    # Call the get_rss_feed function, using the mock request
    response = get_rss_feed()

    # Assert the expected content is in the response body
    for xml_assert in XML_ASSERTS:
        assert xml_assert in response


def test_get_rss_feed_http_error(
    requests_mock: requests_mock.mocker.Mocker
) -> None:

    """ Tests the get_rss_feed function using a mock HTTP request.

        Tests an unsuccessful HTTP request, with a mocked HTTP
        status code.

        Args:
            requests_mock (requests_mock.mocker.Mocker):
                pytest fixture to mock requests class HTTP requests.

        Returns:
            None.
    """

    # Create an unsuccessful mock HTTP request
    requests_mock.get(
        url=URL,
        status_code=404
    )

    # Call the get_rss_feed function and mocks an HTTPError exception
    with raises(HTTPError):
        get_rss_feed()

    return None


@patch(
    'builtins.open',
    side_effect=mock_open(
        read_data=XML
    )
)
def test_write_rss_to_xml(
    mock_xml_file_data: MagicMock
) -> None:
    """ Test the write_rss_to_xml function with mock data.

        Check content for expected XML data.

        Args:
            mock_xml_file_data (MagicMock):
                pytest patch fixture with mock XML file data

        Returns:
            None.
    """

    # Assert the expected content is in the mocked file contents
    for xml_assert in XML_ASSERTS:
        assert xml_assert in XML

    return None
