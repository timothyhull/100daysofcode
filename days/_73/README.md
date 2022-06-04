# :calendar: Day 73: 5/29/2022-6/3/2022

---

## Topics

:clipboard: Automating Tasks With Selenium

---

## Resources

:star: [`pipenv` on PyPI](https://pypi.org/project/pipenv)

:star: [`pipenv` Documentation](https://pipenv.pypa.io/en/latest)

:star: [Selenium on PyPI](https://pypi.org/project/selenium)

:star: [Selenium Documentation](https://www.selenium.dev)

:star: [Sending Keystrokes with Selenium](https://www.selenium.dev/documentation/webdriver/elements/interactions/#send-keys)

:star: [Chromedriver binary download](https://chromedriver.chromium.org/downloads)

---

## Tasks

:white_check_mark: Watch videos 1-2

:white_check_mark: Research `pipenv` versus `venv`

:white_check_mark: Setup a local `pipenv` runtime environment for Selenium development/testing

:white_check_mark: Make Chromedriver available to the `pipenv` runtime environment

:white_check_mark: Watch video 3

:white_check_mark: Watch video 4

:white_check_mark: Watch videos 5-6

---

## Notes

### :notebook: 5/29/22

- Watched videos 1-3.
    - Selenium automates simulated human interaction with a web page through a Python-controlled instance of a web browser"
        - Installs with Python pip:

            ```bash
            pip install selenium
            ```

    - Selenium requires a headless web browser driver, typically this is [Chromedriver](https://chromedriver.chromium.org/downloads).
        - Firefox also supports headless operation.

---

### :notebook: 5/31/22

- Reviewed `pipenv` documentation in order to setup local development, outside of the VS Code devcontainer.
    - This is necessary to launch a local browser, because the devcontainer does not have a graphical browser.

- Setup `pipenv` on my local computer development environment using the [selenium_project](https://github.com/timothyhull/100daysofcode/tree/main/days/_73/selenium_project) directory:

    ```bash
    # Install pipenv
    pip install pipenv

    # Create a new directory
    cd selenium_project && mkdir selenium_project

    # Create a pipenv environment
    pipenv install

    # Install Selenium in the pipenv environment
    pipenv install selenium

    # Install iPython as a development package
    pipenv install --dev ipython

    # Run the 'pip freeze' command for the pipenv environment
    pipenv run pip freeze
    ```

- A `pipenv` shell is available to interactively work with the `pipenv` environment:

    ```bash
    # Launch the pipenv shell
    pipenv shell

    # Check the python version
    python --version
    ```

- Copied Chromedriver to `/usr/local/bin` on my local computer, and verified the availability of Chromedriver to the `pipenv` environment with the following commands:

    ```bash
    # Display the location of the chromedriver binary
    pipenv run which chromedriver
    # output -> /usr/local/bin/chromedriver

    pipenv run chromedriver --version
    # output -> ChromeDriver 102.0.5005.61 (0e59bcc00cc4985ce39ad31c150065f159d95ad3-refs/branch-heads/5005@{#819})
    ```

---

### :notebook: 6/1/22

- Installed `python-dotenv` in the `pipenv` environment.

     ```bash
    # Install python-dotenv in the pipenv environment
    pipenv install python-dotenv
    ```

- Created the file [selenium_1.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_73/selenium_project/selenium_1.py):
    - Created basic automation to open a web page and perform click interaction.

    ```python
    # Import Selenium packages and classes
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    # Create a Chrome webdriver object
    driver = webdriver.Chrome()

    # Open a URL in a Selenium-controlled browser
    driver.get(URL)

    # Find and click on an element
    toggle_button = driver.find_element(
        by=By.XPATH,
        value='/sample/xpath/value'
    )
    toggle_button.click()
    ```

- Watched the first 3 minutes of video 3

---

### :notebook: 6/2/22

- Tested reviewing search results with a CSS class selector, and displaying the results as a list:

    ```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    URL = 'https://squidfunk.github.io/mkdocs-material/reference/icons-emojis'
    SEARCH_RESULTS_CLASS = 'mdx-iconsearch-result__list'

    # Create a Chrome webdriver object
    driver = webdriver.Chrome()

    # Open a URL in a Selenium-controlled browser
    driver.get(URL)

    # Assert the result exists by searching the results class
    print(f'\nConfirming "{EMOJI_MATCH}" is in the results class...', end='')
    results = driver.find_element(
        by=By.CLASS_NAME,
        value=SEARCH_RESULTS_CLASS
    )
    assert EMOJI_MATCH in results.text.split('\n')
    print('done.\n')

    # Display full search results list
    print('\nSearch results:')
    for index, result in enumerate(results.text.split('\n'), 1):
        print(f'{index}. {result}')
    ```

    - Shell output from [selenium_1.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_73/selenium_project/selenium_1.py):

        ```bash
        Search results:
        1. :material-github:
        2. :octicons-logo-github-16:
        3. :octicons-mark-github-16:
        4. :fontawesome-brands-github:
        5. :fontawesome-brands-github-alt:
        6. :fontawesome-brands-github-square:
        ```

- Tested closing the web browser:

    ```python
    driver.close()
    ```

---

### :notebook: 6/3/22

- Watched videos 5-6.
