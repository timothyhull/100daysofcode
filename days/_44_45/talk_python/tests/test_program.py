#!/usr/bin/env pytest
""" pytest tests for program.py  """

# Imports - Third-Party Modules
from unittest.mock import MagicMock, patch
import _pytest.capture

# Imports - Local
from _44_45.talk_python.program import main

# Constants
KEYWORDS = [
    '100daysofcode',
    'pytest',
    'requests'
]


@patch(
    'builtins.input',
    side_effects=KEYWORDS
)
def test_main(
    keywords: MagicMock,
    capsys: _pytest.capture.capsys
) -> None:
    """ Test the talkpython_search function program.

        Args:
            user_input (MagicMock):
                Mocked user input.

            capsys (_pytest.capture.capsys):
                STDOUT output capture.
    """

    for keyword in keywords:
        main(
            keyword=keyword
        )

        output = capsys.readouterr().out

        assert keyword in output

    return None
