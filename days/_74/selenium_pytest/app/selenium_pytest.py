#!/usr/bin/env python3
""" Selenium pytest testing. """

# Imports - Python Standard Library

# Imports - Third-Party
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# Imports - Local

# Constants
URL = 'https://kingarthurbaking.com'
SEARCH_OPEN_XPATH = '/html/body/div[1]/div/header/div/div[3]/div[1]'
SEARCH_BOX_XPATH = '/html/body/div[1]/div/div[4]/div/div[1]/div[2]/input'
SEARCH_BOX_INPUT = 'gluten free chocolate cake'
SEARCH_AUTO_COMPLETE = 'search-autocomplete'
SEARCH_TARGET_PRODUCT = 'Gluten-Free Chocolate Cake'

# Open a new browser window
browser = webdriver.Chrome()

# Open the target URL
browser.get(URL)

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


# assert 'Gluten-Free Chocolate Cake' in browser.page
