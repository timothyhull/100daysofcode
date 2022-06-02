#!/usr/bin/env python3
""" First test of Selenium. """

# Imports - Python Standard Library

# Imports - Third-Party
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Imports - Local

# Constants
URL = 'https://squidfunk.github.io/mkdocs-material/reference/icons-emojis'
EMOJI_SEARCH = 'github'
EMOJI_MATCH = ':fontawesome-brands-github:'
DARK_MODE_XPATh = '/html/body/header/nav/form'
SEARCH_FIELD_XPATH = '/html/body/div[3]/main/div/div[3]/article/div[1]/input'

# Create a Chrome webdriver object
driver = webdriver.Chrome()

# Open the URL constant value in a Selenium-controlled browser
print('\nOpening URL...', end='')
driver.get(URL)
print('done.')

# Toggle darke mode
print('\nActivating dark mode...', end='')
day_night_toggle = driver.find_element(
    by=By.XPATH,
    value=DARK_MODE_XPATh
)
day_night_toggle.click()
print('done.')

# Locate the search field
print('\nLocating search field...', end='')
search_field = driver.find_element(
    by=By.XPATH,
    value=SEARCH_FIELD_XPATH
)
print('done.')

# Enter the search string
print('\nSending search string...', end='')
search_field.send_keys(EMOJI_SEARCH)
print('done.')


# Press the "Return" key
print('\nPressing "Return"...', end='')
search_field.send_keys(Keys.RETURN)
print('done.')

# Assert the result exists
print(f'\nConfirming "{EMOJI_MATCH}" is in the results...', end='')
assert EMOJI_MATCH in driver.page_source
print('done.\n')
