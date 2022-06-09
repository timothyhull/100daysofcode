#!/usr/bin/env pytest
""" Selenium pytest test cases for selenium_pytest.py. """

# Imports - Python Standard Library

# Imports - Third-Party
from pytest import raises
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException

# Imports - Local
from _74.selenium_pytest.app.selenium_pytest import (
    open_page, search_for_product, search_result_click, close_browser,
    SEARCH_AUTO_COMPLETE, SEARCH_TARGET_PRODUCT, URL
)

# Constants
SEARCH_RESULT_PAGE_URL = (
    'recipes/gluten-free-chocolate-cake-recipe'
)


# Test functions
def test_open_page() -> None:
    """ Test the open_page function.

        Args:
            None.

        Returns:
            None.
    """

    # Call the open_page function
    browser = open_page()

    # Confirm the URL matches the expected value
    assert URL in browser.current_url

    return None


def test_search_for_product() -> None:
    """ Test the search_for_product function.

        Args:
            None.

        Returns:
            None.
    """

    # Call the open_page function
    browser = open_page()

    # Call the search_for_product function
    browser = search_for_product(
        browser=browser
    )

    # Confirm the search auto-complete results contain the expected value
    assert SEARCH_TARGET_PRODUCT in browser.find_element(
        by=By.CLASS_NAME,
        value=SEARCH_AUTO_COMPLETE
    ).text

    return None


def test_search_result_click() -> None:
    """ Test the search_result_click function.

        Args:
            None.

        Returns:
            None.
    """

    # Call the open_page function
    browser = open_page()

    # Call the search_for_product function
    browser = search_for_product(
        browser=browser
    )

    # Call the search_result_click function
    browser = search_result_click(
        browser=browser
    )

    # Confirm the current browser URL matches the expected value
    assert browser.current_url.endswith(SEARCH_RESULT_PAGE_URL)

    return None


def test_close_browser() -> None:
    """ Test the close_browser function.

        Args:
            None.

        Returns:
            None.
    """

    # Call the open_page function
    browser = open_page()

    # Call the search_for_product function
    browser = search_for_product(
        browser=browser
    )

    # Call the search_result_click function
    browser = search_result_click(
        browser=browser
    )

    # Call the close_browser function
    browser = close_browser(
        browser=browser
    )

    # Confirm a check for the browser.page_source attribute raises an exception
    with raises(
        expected_exception=InvalidSessionIdException
    ):
        browser.page_source

    return None
