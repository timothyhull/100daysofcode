#!/usr/bin/env pytest
""" pytest tests for program.py """

# Imports - Python Standard Library

# Imports - Third-party

# Imports - Local
from _55.app.program import (
    read_entries
)

# Constants
BLOG_JSON = 'So maybe you\'ve heard about Requests...'


def test_read_entries() -> None:
    """ Test the read_entries function in program.py.

        Args:
            None.

        Returns:
            None.
    """

    # Call the function
    entries = read_entries()

    assert BLOG_JSON in entries.text

    return None
