#!/usr/bin/env pytest
""" Tests for PyBite #2 (pybite_2.py).
"""

# Imports
from _30.pybite_2 import extract_course_times, get_all_hashtags_and_links, \
                         match_first_paragraph

# Constants
COURSE_TIMES_RESULT = ['01:47', '32:03', '41:51', '27:48', '05:02']
HASTAGS_AND_LINKS_RESULT = [
    'http://pybit.es/requests-cache.html',
    '#python',
    '#APIs'
]
HTML_RESULT = 'pybites != greedy'


def test_extract_course_times() -> None:
    """ Test the extract_course_times function.  Confirm the function returns
        the list of times in the COURSE_TIMES_RESULT constant.

        Args:
            None.

        Returns:
            None.
    """

    assert extract_course_times() == COURSE_TIMES_RESULT


def test_get_all_hashtags_and_links() -> None:
    """ Test the get_all_hashtags_and_links function.  Confirm the function returns
        the list of times in the COURSE_TIMES_RESULT constant.

        Args:
            None.

        Returns:
            None.
    """

    assert get_all_hashtags_and_links() == HASTAGS_AND_LINKS_RESULT


def test_match_first_paragraph() -> None:
    """ Test the get_all_hashtags_and_links function.  Confirm the function returns
        the list of times in the HTML_RESULT constant.

        Args:
            None.

        Returns:
            None.
    """

    assert match_first_paragraph() == HTML_RESULT
