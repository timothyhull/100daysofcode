#!/usr/bin/env python3
""" Selenium functions for pytest testing. """

# Imports - Python Standard Library

# Imports - Third-Party
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

# Imports - Local

# Constants
URL = 'https://www.kingarthurbaking.com'
SEARCH_OPEN_XPATH = '/html/body/div[1]/div/header/div/div[3]/div[1]'
SEARCH_BOX_XPATH = '/html/body/div[1]/div/div[4]/div/div[1]/div[2]/input'
SEARCH_BOX_INPUT = 'gluten free chocolate cake'
SEARCH_AUTO_COMPLETE = 'search-autocomplete'
SEARCH_TARGET_PRODUCT = 'Gluten-Free Chocolate Cake'
SLEEP_TIMER = 5


def open_page(
    url: str = URL
) -> WebDriver:
    """ Open a webpage with Chrome.

        Args:
            url (str, optional):
                URL to direct Chrome navigation to.  Defaults to the
                value of the URL constant.

        Returns:
            browser (selenium.webdriver.chrome.webdriver.WebDriver):
                Chrome browser object navigated to a URL.
    """

    # Open a new browser window
    browser = webdriver.Chrome()

    # Open the target URL
    browser.get(URL)

    return browser


def search_for_product(
    browser: WebDriver,
    search_input: str = SEARCH_BOX_INPUT
) -> WebDriver:
    """ Click to activate the search field and input search text.

        Args:
            browser (selenium.webdriver.chrome.webdriver.WebDriver):
                Chrome browser object navigated to a URL.

            search_input (str, optional):
                Text to search for.  Defaults to the value of the
                SEARCH_BOX_INPUT constant.

        Returns:
            browser (selenium.webdriver.chrome.webdriver.WebDriver):
                Chrome browser object with search box filled with
                text input.
    """

    # Locate and click on the search icon
    browser.find_element(
        by=By.XPATH,
        value=SEARCH_OPEN_XPATH
    ).click()

    # Type the product search string
    browser.find_element(
        by=By.XPATH,
        value=SEARCH_BOX_XPATH
    ).send_keys(SEARCH_BOX_INPUT)

    return browser


def search_result_click(
    browser: WebDriver
) -> WebDriver:
    """ Find search results in auto-complete output and click result.

        Args:
            browser (selenium.webdriver.chrome.webdriver.WebDriver):
                Chrome browser object with search box filled with
                text input.

        Returns:
            browser (selenium.webdriver.chrome.webdriver.WebDriver):
                Chrome browser object navigated to search results page.
    """

    # Attempt to locate the "search-autocomplete" results class
    search_auto_complete = browser.find_element(
        by=By.CLASS_NAME,
        value=SEARCH_AUTO_COMPLETE
    )

    # If present, click on the target search product
    if SEARCH_TARGET_PRODUCT in search_auto_complete.text:
        browser.find_element(
            by=By.LINK_TEXT,
            value=SEARCH_TARGET_PRODUCT
        ).click()

    # Pause on the target page for SLEEP_TIMER seconds
    sleep(SLEEP_TIMER)

    return browser


def close_browser(
    browser: WebDriver
) -> WebDriver:
    """ Close a web browser.

        Args:
            browser (selenium.webdriver.chrome.webdriver.WebDriver):
                Chrome browser object.

        Returns:
            browser (selenium.webdriver.chrome.webdriver.WebDriver):
                Closed chrome browser object.
    """

    # Close the browser
    browser.close()

    return browser


def main() -> None:
    """ Main application.

        Args:
            None.

        Returns:
            None.
    """

    # Open the target page
    print(f'\nOpening web browser and navigating to "{URL}"...', end='')
    browser = open_page()
    print('done.')

    # Conduct product search
    print(f'\nSearching for "{SEARCH_BOX_INPUT}"...', end='')
    browser = search_for_product(
        browser=browser
    )
    print('done.')

    # Click on the search result suggestion
    print(f'\nClicking the search result "{SEARCH_TARGET_PRODUCT}"...', end='')
    browser = search_result_click(
        browser=browser
    )
    print('done.')

    # Close the browser
    print('\nClosing the web browser...', end='')
    close_browser(
        browser=browser
    )
    print('done.')

    return None


# Run the script if directly launched, not imported
if __name__ == '__main__':
    main()
