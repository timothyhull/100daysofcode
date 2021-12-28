#!/usr/bin/env pytest
""" pytest tests for program.py """

# Imports - Python Standard Library
from unittest.mock import MagicMock, patch

# Imports - Third-party
from _pytest.capture import CaptureFixture
from pytest import raises
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker

# Imports - Local
from _55.app.program import (
    get_user_input, read_entries
)
from _55.app.blog_client import (
    BASE_URL, BLOG_ENDPOINT
)

# Constants
USER_INPUT = [
    'a',
    'r',
    'w',
    ''
]
EXPECTED_OUTPUT = [
    'Invalid input',
    'Read posts',
    'Write a post',
    'Invalid input'
]
BLOG_TEXT = 'So maybe you\'ve heard about Requests...'


@patch(
    target='builtins.input',
    side_effect=USER_INPUT
)
def test_get_user_input(
    user_input: MagicMock,
    capsys: CaptureFixture
) -> None:
    """ Test the get_user_input function in program.py.

        Compare the STDOUT output with expected results.

        Args:
            user_input (MagicMock):
                Mocked user input data.

            capsys (CaptureFixture):
                pytest fixture to capture writes to sys.stdout and
                sys.stderr.

        Returns:
            None.
    """

    # Loop over each user input value
    for index, _ in enumerate(USER_INPUT):
        # Call the get_user_input function with mocked user input
        get_user_input()

        # Capture STDOUT output
        output = capsys.readouterr().out

        # Assert the first side_effect output
        assert EXPECTED_OUTPUT[index] in output

    return None


def test_read_entries(
    requests_mock: Mocker
) -> None:
    """ Test the read_entries function in program.py.

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

    # Call the read_entries function
    entries = read_entries()

    # Assert the correct text is in the HTTP response text attribute
    assert BLOG_TEXT in entries.text

    return None


def test_read_entries_error(
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

    with raises(
        expected_exception=HTTPError
    ):
        # Call the read_entries function
        read_entries()

    return None
