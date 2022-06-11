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
APP_LINK_TEXT = 'PyPlanet Article Sharer App'
APP_LINK_URL = 'pyplanet'
TABLE_HEADER_SELECTOR = 'body > main > table > thead > tr > th'
TABLE_HEADER_TEXT = 'Title'
TABLE_ROW_COUNT = 100
TABLE_ROW_XPATH = f'/html/body/main/table/tbody/tr[{TABLE_ROW_COUNT}]'


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

    # Open the target URL
    browser.get(
        url=PAGE_URL
    )

    return browser


# Test functions
def test_1(
    chrome_browser: WebDriver
) -> None:
    """ Test for the presence of header elements.

        "Go to the http://pyplanet.herokuapp.com/. The header should
        say PyBites 100 Days of Django. The navbar has Login and Home
        links. The first link in the main div is PyPlanet Article
        Sharer App"

        Args:
            chrome_browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object from pytest fixture
                open_chrome.

        Returns:
            None.
    """

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


def test_2(
    chrome_browser: WebDriver
) -> None:
    """ Test for the presence of table elements.

        "Click on the PyPlanet Article Sharer App link and test the
        page contains a table with a th (table header) containing the
        word Title. This app watches the PyPlanet feed so the titles
        change every day so that is hard test. What we can test though
        is if the table contains 100 entries (tr)."

        Args:
            chrome_browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object from pytest fixture
                open_chrome.

        Returns:
            None.
    """

    # Locate the 'PyPlanet Article Sharer App' link
    app_link = chrome_browser.find_element(
        by=By.LINK_TEXT,
        value=APP_LINK_TEXT
    )
    assert app_link.text == APP_LINK_TEXT

    # Click on the 'PyPlanet Article Sharer App' link
    app_link.click()
    assert APP_LINK_URL in chrome_browser.current_url

    # Test for the <th> value
    th_value = chrome_browser.find_element(
        by=By.CSS_SELECTOR,
        value=TABLE_HEADER_SELECTOR
    )
    assert th_value.text == TABLE_HEADER_TEXT

    # Test for the correct number of <tr> elements
    last_tr = chrome_browser.find_element(
        by=By.XPATH,
        value=TABLE_ROW_XPATH
    )
    assert last_tr

    # Close the browser
    chrome_browser.close()

    return None


def test_3(
    chrome_browser: WebDriver
) -> None:
    """ Test for the presence of table elements.

        "Go to an article and check there is only a Go back button
        (logged out view). Check if the header link at the top is the
        same as the link you clicked on, in this example: Martin
        Fitzpatrick: KropBot: Multiplayer Internet-controlled robot.
        The Go back should redirect back to the app's home page."

        Args:
            chrome_browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object from pytest fixture
                open_chrome.

        Returns:
            None.
    """

    return None


def test_4(
    chrome_browser: WebDriver
) -> None:
    """ Test the user login functionality.

        "Using Selenium click Login and login with user:
        guest / password: changeme - then click the
        blue Login button."

        Args:
            chrome_browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object from pytest fixture
                open_chrome.

        Returns:
            None.
    """

    return None


def test_5(
    chrome_browser: WebDriver
) -> None:
    """ Test for the presence logged-on user elements.

        "Check you are redirected back to 100Days home and if
        navigation contains Welcome back, guest! and Logout
        and Home links."

        Args:
            chrome_browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object from pytest fixture
                open_chrome.

        Returns:
            None.
    """

    return None


def test_6(
    chrome_browser: WebDriver
) -> None:
    """ Test for the presence of a Twitter button.

        "Going back to the article link (3.), check that you now have a
        Tweet this button alongside the Go back button. Optionally you
        can check the link of the Tweet this button (extra check:
        PyBites entries have New PyBites Article prepended)."

        Args:
            chrome_browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object from pytest fixture
                open_chrome.

        Returns:
            None.
    """

    return None


def test_7(
    chrome_browser: WebDriver
) -> None:
    """ Test for the logout banner and heading links.

        "Finally logout with Selenium and check for See you! and
        You have been successfully logged out., logout in the URL,
        and navbar links are Login and Home again."

        Args:
            chrome_browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object from pytest fixture
                open_chrome.

        Returns:
            None.
    """

    return None
