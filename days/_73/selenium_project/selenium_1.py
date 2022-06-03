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
DARK_MODE_XPATH = '/html/body/header/nav/form'
SEARCH_FIELD_XPATH = '/html/body/div[3]/main/div/div[3]/article/div[1]/input'
SEARCH_RESULTS_CLASS = 'mdx-iconsearch-result__list'

# Create a Chrome webdriver object
driver = webdriver.Chrome()

# Open the URL constant value in a Selenium-controlled browser
print('\nOpening URL...', end='')
driver.get(URL)
print('done.')

# Toggle dark mode
print('\nActivating dark mode...', end='')
day_night_toggle = driver.find_element(
    by=By.XPATH,
    value=DARK_MODE_XPATH
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

# Assert the result exists by searching the page source
print(f'\nConfirming "{EMOJI_MATCH}" is in the page source...', end='')
assert EMOJI_MATCH in driver.page_source
print('done.')

# Assert the result exists by searching the results class
print(f'\nConfirming "{EMOJI_MATCH}" is in the results class...', end='')
results = driver.find_element(
    by=By.CLASS_NAME,
    value=SEARCH_RESULTS_CLASS
)
assert EMOJI_MATCH in results.text.split('\n')
print('done.\n')

# Display full search results list
print('Search results:')
for index, result in enumerate(results.text.split('\n'), 1):
    print(f'{index}. {result}')

# Close the web browser
driver.close()
