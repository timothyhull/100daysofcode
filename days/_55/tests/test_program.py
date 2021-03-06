#!/usr/bin/env pytest
""" pytest tests for program.py """

# Imports - Python Standard Library
from datetime import datetime
from unittest.mock import MagicMock, patch

# Imports - Third-party
from _pytest.capture import CaptureFixture
from pytest import raises
from requests.exceptions import HTTPError
from requests.models import Response
from requests_mock.mocker import Mocker

# Imports - Local
from _55.app.program import (
    get_user_input, get_write_entry_input, read_entries, write_entries
)
from _55.app.blog_client import (
    BASE_URL, BLOG_ENDPOINT
)

# Constants
VALID_USER_INPUT = [
    'r',
    'w'
]
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
BLOG_JSON = [
  {
    'id': 'c7081102-e2c9-41ec-8b79-adc1f3469d91',
    'published': '2017-02-14',
    'view_count': 1231,
    'content': 'So maybe you\'ve heard about Requests...',
    'title': 'Easy Breezy Python HTTP Clients'
  }
]
BLOG_ID = 'c7081102-e2c9-41ec-8b79-adc1f3469d91'
NEW_BLOG_JSON = {
    'title': 'Test the write_entries function',
    'content': 'This is a test of the write_entries function in program.py...',
    'view_count': 54321,
    'published': f'{datetime.now().date().isoformat()}',
}
NEW_BLOG_JSON_RESPONSE = {
    **NEW_BLOG_JSON,
    'id': BLOG_ID
}


@patch(
    target='builtins.input',
    side_effect=VALID_USER_INPUT
)
def test_get_user_input(
    valid_user_input: MagicMock
) -> None:
    """ Test the get_user_input function in program.py.

        Compare the string output with valid results.

        Args:
            valid_user_input (MagicMock):
                Mocked user input data.
    """

    # Loop over each valid user input option
    for index, _ in enumerate(VALID_USER_INPUT):

        # Call the function, and assign the result to a variable
        user_input = get_user_input()

        # Assert that user_input is equivalent to the mocked input value.
        assert user_input == VALID_USER_INPUT[index]

    return None


@patch(
    target='builtins.input',
    side_effect=USER_INPUT
)
def test_get_user_input_stdout(
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


@patch(
    'builtins.input',
    side_effect=[1]
)
def test_read_entries(
    user_input: MagicMock,
    requests_mock: Mocker,
) -> None:
    """ Test the read_entries function in program.py.

        Args:
            user_input: (MagicMock):
                Mocked user responses to input prompts.

            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup two mock HTTP requests
    url = f'{BASE_URL}{BLOG_ENDPOINT}'
    url_2 = f'{BASE_URL}{BLOG_ENDPOINT}/{BLOG_ID}'

    # Send the first mock HTTP request
    requests_mock.get(
        url=url,
        json=BLOG_JSON
    )

    # Send the second mock HTTP request
    requests_mock.get(
        url=url_2,
        json=BLOG_JSON[0]
    )

    # Call the read_entries function
    entries = read_entries()

    # Assert the correct text is in the HTTP response text attribute
    assert BLOG_JSON[0].get('content') == entries.json()[0].get('content')

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


@patch(
    target='builtins.input',
    side_effect=NEW_BLOG_JSON.values()
)
def test_get_write_entry_input(
    user_input: MagicMock
) -> None:
    """ Test the get_write_entry function in program.py.

        Args:
            user_input: (MagicMock):
                Mocked user responses to input prompts.

            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Call the function
    user_input = get_write_entry_input()

    # Assert dictionary properties are correct
    assert user_input == NEW_BLOG_JSON

    return None


@patch(
    target='builtins.input',
    side_effect=NEW_BLOG_JSON.values()
)
def test_write_entries(
    user_input: MagicMock,
    requests_mock: Mocker
) -> None:
    """ Test the write_entries function in program.py.

        Args:
            user_input: (MagicMock):
                Mocked user responses to input prompts.

            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup the Mock HTTP request
    url = f'{BASE_URL}{BLOG_ENDPOINT}'

    # Create the Mock HTTP request
    requests_mock.post(
        url=url,
        json=NEW_BLOG_JSON_RESPONSE,
        status_code=201
    )

    # Call the write_entries function
    new_blog_post = write_entries()

    assert new_blog_post.json().get('id') == BLOG_ID

    return None


@patch(
    target='builtins.input',
    side_effect=NEW_BLOG_JSON.values()
)
def test_write_entries_error(
    user_input: MagicMock,
    requests_mock: Mocker
) -> Response:
    """ Test errors in the write_entries function in program.py.

        Args:
            user_input: (MagicMock):
                Mocked user responses to input prompts.

            requests_mock (Mocker):
                Mock requests object.

        Returns:
            None.
    """

    # Setup the Mock HTTP request
    url = f'{BASE_URL}{BLOG_ENDPOINT}'

    # Create the Mock HTTP request
    requests_mock.post(
        url=url,
        status_code=401
    )

    # Use a context manager to call pytest.raises with an exception (HTTPError)
    with raises(
        expected_exception=HTTPError
    ):
        # Call the write_entries function
        write_entries()

    return None
