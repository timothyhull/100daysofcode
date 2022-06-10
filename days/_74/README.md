# :calendar: Day 74: 6/4/2022-6/9/2022

---

## Topics

:clipboard: Automating Tasks With Selenium

---

## Resources

:star: [Using Selenium to write tests article](https://selenium-python.readthedocs.io/getting-started.html#using-selenium-to-write-tests)

:star: [RealPython article: Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/#i-already-have-a-requirementstxt-how-do-i-convert-to-a-pipfile)

:star: [`pipenv` Automatic Loading of `.env` files](https://pipenv.pypa.io/en/latest/advanced/#automatic-loading-of-env)

:star: [Code Challenge 32 test page](https://pyplanet.herokuapp.com)

---

## Tasks

:white_check_mark: Watch video 7

:white_check_mark: Read the [Using Selenium to write tests article](https://selenium-python.readthedocs.io/getting-started.html#using-selenium-to-write-tests)

:white_check_mark: Create a `pytest` test of a web page using Selenium

:white_large_square: Complete [Code Challenge 32](https://codechalleng.es/challenges/32)

---

## Notes

### :notebook: 6/4/22

- Watched video 7.

- Read Using Selenium to write tests article.

- Created framework for a `pytest` test for Selenium.
    - Created a `pipenv` environment in the folder [selenium_pytest](https://github.com/timothyhull/100daysofcode/tree/main/days/_74/selenium_pytest).
    - The `pipenv install` will automatically detect a `requirements.txt` file and convert the packages to the `Pipfile`.
    - Alternatively, the command `pipenv install -r requirements.txt` will perform the same action.
    - The command `pipenv install -dr dev-requirements.txt` installs development packages.

- An error occurred when attempting to remove the folder [selenium_pytest](https://github.com/timothyhull/100daysofcode/tree/main/days/_74/selenium_pytest), recreate the folder, and run the command `pipenv install`:

    ```bash
    Usage: pipenv install [OPTIONS] [PACKAGES]...

    ERROR:: --system is intended to be used for pre-existing Pipfile installation, not installation of specific packages. Aborting.
    ```

    - This appears to be a [`pipenv` bug](https://github.com/pypa/pipenv/issues/5052) that requires removing the virtual environment associated with the `pipenv`:

    ```bash
    # Determine the location of the virtual environment
    pipenv --venv
    > /Users/user_name/.local/share/virtualenvs/selenium_pytest-G4_FQY5m

    # Remove the existing virtual environment
    cd ~/.local/share/virtualenvs
    rm -rf selenium_pytest-G4_FQY5m

    # Recreate the pipenv environment
    cd ~
    mkdir selenium_pytest && cd selenium_pytest
    pipenv install
    ```

---

### :notebook: 6/5/22

- Created the file [selenium_pytest.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_74/selenium_pytest/app/selenium_pytest.py), to search a website for a product and click an auto-complete search suggestion link.
    - Script works properly.
    - `pytest` development is the next required step.

---

### :notebook: 6/6/22

- Refactored [selenium_pytest.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_74/selenium_pytest/app/selenium_pytest.py) with functional decomposition, in preparation for testing with `pytest`.

---

### :notebook: 6/7/22

- Added the `main` function to [selenium_pytest.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_74/selenium_pytest/app/selenium_pytest.py), and included `print` statements to indicate progress.

- Added the `test_open_page` function to [test_selenium_pytest.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_74/selenium_pytest/tests/test_selenium_pytest.py), to check that the current URL matches the expected URL.
    - All `pytest` tests pass.

---

### :notebook: 6/8/22

- Added the `test_search_for_product`, `test_search_result_click`,  and `test_close_browser` functions to [test_selenium_pytest.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_74/selenium_pytest/tests/test_selenium_pytest.py).
    - All `pytest` tests pass.

- Added environment variable file to automatically import the `PYTHONPATH` value when the `pipenv` environment starts.

---

### :notebook: 6/9/22

- Created the file [test_django_app.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_74/django_app_pytest/test_django_app.py)
    - Created `pipenv` environment with requirements files.
    - Created the `pytest` fixture function `chrome_browser`, to open a Chrome browser instance.
    - Created the function `test_1`, for test case #1.
    - Tested for the presence of the header text plus two links in the header section of the page.
    - All `pytest` tests pass.
