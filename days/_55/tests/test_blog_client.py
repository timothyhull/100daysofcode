#!/usr/bin/env pytest
""" pytest tests for blog_client.py """

# Imports - Python Standard Library
from datetime import datetime

# Imports - Third-party
from pytest import raises
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker

# Imports - Local
from _55.app.blog_client import (
    BASE_URL, BLOG_ENDPOINT, BlogClient
)

# Constants
BLOG_ID = 'c7081102-e2c9-41ec-8b79-adc1f3469d91'
BLOG_TEXT = 'So maybe you\'ve heard about Requests...'
NEW_BLOG_JSON = {
    'title': 'Test the write_entries function',
    'content': 'This is a test of the write_entries function in program.py...',
    'view_count': 54321,
    'published': f'{datetime.now().date().isoformat()}',
}


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
        blog_client.get_all_entries()

    return None


def test_get_entry(
    requests_mock: Mocker
) -> None:
    """ Test the get_entry function in blog_client.py.

        Args:
            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup mock HTTP request
    url = f'{BASE_URL}{BLOG_ENDPOINT}/{BLOG_ID}'

    # Send the mock HTTP request
    requests_mock.get(
        url=url,
        text=BLOG_TEXT
    )

    # Create a class instance
    blog_client = BlogClient()

    # Call the get_all_entries method
    blog_entry = blog_client.get_entry(
        entry_id=BLOG_ID
    )

    assert BLOG_TEXT in blog_entry.text

    return None


def test_get_entry_error(
    requests_mock: Mocker
) -> None:
    """ Test errors in the get_entry function in blog_client.py.

        Args:
            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup mock HTTP request
    url = f'{BASE_URL}{BLOG_ENDPOINT}/{BLOG_ID}'

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
        # Call the get_entry method
        blog_client.get_entry(
            entry_id=BLOG_ID
        )

    return None


def test_write_entry(
    requests_mock: Mocker
) -> None:
    """ Test the write_entry function in blog_client.py.

        Args:
            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup mock HTTP request
    url = f'{BASE_URL}{BLOG_ENDPOINT}'

    # Send the mock HTTP request
    requests_mock.post(
        url=url,
        json=NEW_BLOG_JSON,
        status_code=201
    )

    # Create a class instance
    blog_client = BlogClient()
    new_blog = blog_client.write_entry(**NEW_BLOG_JSON)

    # Call the get_all_entries method
    assert new_blog.json() == NEW_BLOG_JSON

    return None


def test___write_entry(
    requests_mock: Mocker
) -> None:
    """ Test the __write_entry function in blog_client.py.

        Args:
            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup mock HTTP request
    url = f'{BASE_URL}{BLOG_ENDPOINT}'

    # Send the mock HTTP request
    requests_mock.post(
        url=url,
        json=NEW_BLOG_JSON,
        status_code=201
    )

    # Create a class instance
    blog_client = BlogClient()

    # Call the get_all_entries method
    new_blog = blog_client._BlogClient__write_entry()

    assert new_blog.status_code == 201
    assert new_blog.json() == NEW_BLOG_JSON

    return None


def test___write_entry_error(
    requests_mock: Mocker
) -> None:
    """ Test errors in the __write_entry function in blog_client.py.

        Args:
            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup mock HTTP request
    url = f'{BASE_URL}{BLOG_ENDPOINT}'

    # Send the mock HTTP request
    requests_mock.post(
        url=url,
        status_code=404
    )

    with raises(
        expected_exception=HTTPError
    ):
        # Create a class instance
        blog_client = BlogClient()

        # Call the get_all_entries method
        blog_client._BlogClient__write_entry()

    return None
