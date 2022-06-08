#!/usr/bin/env pytest
""" Selenium pytest test cases for selenium_pytest.py. """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from _74.selenium_pytest.app.selenium_pytest import (
    open_page, search_for_product, search_result_click, close_browser, URL
)

# Constants


# Test functions
def test_open_page() -> None:
    """ Test the open_page function.

        Args:
            None.

        Returns:
            None.
    """

    browser = open_page()

    assert URL in browser.current_url

    return None
