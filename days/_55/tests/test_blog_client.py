#!/usr/bin/env pytest
""" pytest tests for blog_client.py """

# Imports - Python Standard Library

# Imports - Third-party
from pytest import raises
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker

# Imports - Local
from _55.app.blog_client import (
    BASE_URL, BLOG_ENDPOINT, BlogClient
)

# Constants
BLOG_TEXT = 'So maybe you\'ve heard about Requests...'

# Constants
BLOG_TEXT = 'So maybe you\'ve heard about Requests...'


def test_get_all_entries(
    requests_mock: Mocker
) -> None:
    """ Test the get_all_entries function in blog_client.py.

        Args:
            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup mock HTTP request
    url = f'{BASE_URL}{BLOG_ENDPOINT}'

    # Send the mock HTTP request
    requests_mock.get(
        url=url,
        text=BLOG_TEXT
    )

    # Create a class instance
    blog_client = BlogClient()

    # Call the get_all_entries method
    all_entries = blog_client.get_all_entries()

    assert BLOG_TEXT in all_entries.text

    return None


def test_get_all_entries_error(
    requests_mock: Mocker
) -> None:
    """ Test errors in the get_all_entries function in blog_client.py.

        Args:
            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup mock HTTP request
    url = f'{BASE_URL}{BLOG_ENDPOINT}'

    # Send the mock HTTP request
    requests_mock.get(
        url=url,
        status_code=400
    )

    # Create a class instance
    blog_client = BlogClient()

    with raises(
        expected_exception=HTTPError
    ):
        # Call the get_all_entries method
        all_entries = blog_client.get_all_entries()
        all_entries.raise_for_status()

    return None
