#!/usr/bin/env pytest
""" Selenium testing application for Code Challenge #32.

    https://codechalleng.es/challenges/32/
"""

# Imports - Python Standard Library

# Imports - Third-party
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

# Imports - Local

# Constants
PAGE_URL = 'https://pyplanet.herokuapp.com/'
PAGE_HEADER_XPATH = '/html/body/header/h1'
PAGE_HEADER_TEXT = 'PyBites 100 Days of Django'
LOGIN_URL_TEXT = 'Login'
HOME_URL_TEXT = 'Home'


# pytest fixtures
@fixture()
def chrome_browser() -> WebDriver:
    """ pytest fixture for a Chrome browser object.

        Args:
            None.

        Returns:
            browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object.
    """

    # Create a Chrome browser instance
    browser = webdriver.Chrome()

    return browser


# Test functions
def test_1(
    chrome_browser: WebDriver
) -> None:
    """ Test for the presence of header elements.

        Elements should include a text header and links
        for 'Login' and 'Home'.

        Args:
            chrome_browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object from pytest fixture
                open_chrome.

        Returns:
            None.
    """

    # Open the target URL
    chrome_browser.get(
        url=PAGE_URL
    )

    # Test for the header text element
    header_text = chrome_browser.find_element(
        by=By.XPATH,
        value=PAGE_HEADER_XPATH
    )
    assert header_text.text == PAGE_HEADER_TEXT

    # Test for the 'Login' link
    login_link = chrome_browser.find_element(
        by=By.LINK_TEXT,
        value=LOGIN_URL_TEXT
    )
    assert login_link.text == LOGIN_URL_TEXT

    # Test for the 'Home' link
    login_link = chrome_browser.find_element(
        by=By.LINK_TEXT,
        value=HOME_URL_TEXT
    )
    assert login_link.text == HOME_URL_TEXT

    # Close the browser
    chrome_browser.close()

    return None
