#!/usr/bin/env pytest
""" Selenium testing application for Code Challenge #32.

    https://codechalleng.es/challenges/32/
"""

# Imports - Python Standard Library
from os import getenv

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
ARTICLE_ROW_XPATH = '/html/body/main/table/tbody/tr[1]/td/a'
ARTICLE_HEADING_XPATH = '/html/body/main/h2/a'
GO_BACK_BUTTON_SELECTOR = 'body > main > div.pure-button-group > a'
USERNAME_FIELD_SELECTOR = '#id_username'
PASSWORD_FIELD_SELECTOR = '#id_password'
LOGIN_BUTTON_CLASS = 'pure-button'
WELCOME_BANNER_SELECTOR = '#login'
WELCOME_BANNER_TEXT = 'Welcome back, guest!'
LOGOUT_URL_TEXT = 'Logout'
TWEET_BUTTON_TEXT = 'Tweet this'
LOGOUT_HEADING_XPATH = '/html/body/header/h1'
LOGOUT_HEADING_TEXT = 'See you!'
LOGOUT_BANNER_XPATH = '/html/body/main/p'
LOGOUT_BANNER_TEXT = 'You have been successfully logged out.'


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


@fixture()
def chrome_browser_auth() -> WebDriver:
    """ pytest fixture for a Chrome browser object with authentication.

        Args:
            None.

        Returns:
            browser (selenium.webdriver.chrome.webdriver.Webdriver):
                Selenium Chrome web browser object, authenticated to
                site.
    """

    # Create a Chrome browser instance
    browser = webdriver.Chrome()

    # Open the target URL
    browser.get(
        url=PAGE_URL
    )

    # Locate and click on the 'Login' link
    login_link = browser.find_element(
        by=By.LINK_TEXT,
        value=LOGIN_URL_TEXT
    )
    login_link.click()

    # Find and enter text in the 'username' field
    login_field = browser.find_element(
        by=By.CSS_SELECTOR,
        value=USERNAME_FIELD_SELECTOR
    )
    login_field.send_keys(
        getenv(
            key='USER'
        )
    )

    # Find and enter text in the 'password' field
    pw_field = browser.find_element(
        by=By.CSS_SELECTOR,
        value=PASSWORD_FIELD_SELECTOR
    )
    pw_field.send_keys(
        getenv(
            key='PW'
        )
    )

    # Click the 'Login' button
    login_button = browser.find_element(
        by=By.CLASS_NAME,
        value=LOGIN_BUTTON_CLASS
    )
    login_button.click()

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
                chrome_browser.

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
    home_link = chrome_browser.find_element(
        by=By.LINK_TEXT,
        value=HOME_URL_TEXT
    )
    assert home_link.text == HOME_URL_TEXT

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
                chrome_browser.

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
                chrome_browser.

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

    # Locate and click on the first article in the table
    article_link = chrome_browser.find_element(
        by=By.XPATH,
        value=ARTICLE_ROW_XPATH
    )
    article_link_text = article_link.text
    article_link.click()

    # Confirm the article heading is the same as the link text
    article_header = chrome_browser.find_element(
        by=By.XPATH,
        value=ARTICLE_HEADING_XPATH
    )
    assert article_link_text == article_header.text

    # Confirm the 'Go back' button works correctly
    back_button = chrome_browser.find_element(
        by=By.CSS_SELECTOR,
        value=GO_BACK_BUTTON_SELECTOR
    )
    back_button.click()
    assert chrome_browser.current_url.startswith(f'{PAGE_URL}{APP_LINK_URL}')

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
                chrome_browser.

        Returns:
            None.
    """

    # Locate and click on the 'Login' link
    login_link = chrome_browser.find_element(
        by=By.LINK_TEXT,
        value=LOGIN_URL_TEXT
    )
    login_link.click()
    assert chrome_browser.current_url.startswith(
        f'{PAGE_URL}{LOGIN_URL_TEXT.lower()}'
    )

    # Find and enter text in the 'username' field
    login_field = chrome_browser.find_element(
        by=By.CSS_SELECTOR,
        value=USERNAME_FIELD_SELECTOR
    )
    login_field.send_keys(
        getenv(
            key='USER'
        )
    )

    # Find and enter text in the 'password' field
    pw_field = chrome_browser.find_element(
        by=By.CSS_SELECTOR,
        value=PASSWORD_FIELD_SELECTOR
    )
    pw_field.send_keys(
        getenv(
            key='PW'
        )
    )

    # Click the 'Login' button
    login_button = chrome_browser.find_element(
        by=By.CLASS_NAME,
        value=LOGIN_BUTTON_CLASS
    )
    login_button.click()

    return None


def test_5(
    chrome_browser_auth: WebDriver
) -> None:
    """ Test for the presence logged-on user elements.

        "Check you are redirected back to 100Days home and if
        navigation contains Welcome back, guest! and Logout
        and Home links."

        Args:
            chrome_browser_auth (
                selenium.webdriver.chrome.webdriver.Webdriver
            ):
                Selenium Chrome web browser object from pytest fixture
                chrome_browser, authenticated to site.

        Returns:
            None.
    """

    # Confirm the redirect URL is correct
    assert chrome_browser_auth.current_url.startswith(PAGE_URL)

    # Confirm the welcome banner exists and is correct
    welcome_banner = chrome_browser_auth.find_element(
        by=By.CSS_SELECTOR,
        value=WELCOME_BANNER_SELECTOR
    )
    assert welcome_banner.text.startswith(WELCOME_BANNER_TEXT)

    # Confirm the Logout and Home links exist
    logout_link = chrome_browser_auth.find_element(
        by=By.LINK_TEXT,
        value=LOGOUT_URL_TEXT
    )
    assert logout_link.text == LOGOUT_URL_TEXT

    # Confirm the Logout and Home links exist
    home_link = chrome_browser_auth.find_element(
        by=By.LINK_TEXT,
        value=HOME_URL_TEXT
    )
    assert home_link.text == HOME_URL_TEXT

    return None


def test_6(
    chrome_browser_auth: WebDriver
) -> None:
    """ Test for the presence of a Twitter button.

        "Going back to the article link (3.), check that you now have a
        Tweet this button alongside the Go back button. Optionally you
        can check the link of the Tweet this button (extra check:
        PyBites entries have New PyBites Article prepended)."

        Args:
            chrome_browser_auth (
                selenium.webdriver.chrome.webdriver.Webdriver
            ):

        Returns:
            None.
    """

    # Locate and click the 'PyPlanet Article Sharer App' link
    app_link = chrome_browser_auth.find_element(
        by=By.LINK_TEXT,
        value=APP_LINK_TEXT
    )
    app_link.click()

    # Locate and click on the first article in the table
    article_link = chrome_browser_auth.find_element(
        by=By.XPATH,
        value=ARTICLE_ROW_XPATH
    )
    article_link.click()

    # Confirm the presence of a 'Tweet this' button
    tweet_button = chrome_browser_auth.find_element(
        by=By.LINK_TEXT,
        value=TWEET_BUTTON_TEXT
    )
    assert tweet_button.text == TWEET_BUTTON_TEXT

    return None


def test_7(
    chrome_browser_auth: WebDriver
) -> None:
    """ Test for the logout banner and heading links.

        "Finally logout with Selenium and check for See you! and
        You have been successfully logged out., logout in the URL,
        and navbar links are Login and Home again."

        Args:
            chrome_browser_auth (
                selenium.webdriver.chrome.webdriver.Webdriver
            ):

        Returns:
            None.
    """

    # Logout of the application
    chrome_browser_auth.find_element(
        by=By.LINK_TEXT,
        value=LOGOUT_URL_TEXT
    ).click()
    assert chrome_browser_auth.current_url.startswith(
        f'{PAGE_URL}{LOGOUT_URL_TEXT.lower()}'
    )

    # Confirm the logout heading displays
    logout_heading = chrome_browser_auth.find_element(
        by=By.XPATH,
        value=LOGOUT_HEADING_XPATH
    )
    assert logout_heading.text == LOGOUT_HEADING_TEXT

    # Confirm the logout banner displays
    logout_banner = chrome_browser_auth.find_element(
        by=By.XPATH,
        value=LOGOUT_BANNER_XPATH
    )
    assert logout_banner.text == LOGOUT_BANNER_TEXT

    return None
