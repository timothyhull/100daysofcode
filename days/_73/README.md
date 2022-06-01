# :calendar: Day 73: 5/29/2022-6/4/2022

---

## Topics

:clipboard: Automating Tasks With Selenium

---

## Resources

:star: [`pipenv` on PyPI](https://pypi.org/project/pipenv)

:star: [`pipenv` Documentation](https://pipenv.pypa.io/en/latest)

:star: [Selenium documentation]

:star: [Chromedriver binary download]

---

## Tasks

:white_check_mark: Watch videos 1-3

:white_large_square: Research `pipenv` versus `venv`

:white_large_square: Setup a local Selenium runtime environment

:white_large_square: Watch videos 4-8

---

## Notes

### :notebook: 5/29/22

- Watched videos 1-3.
    - Selenium automates simulated human interaction with a web page through a Python-controlled instance of a web browser"
        - Installs with Python pip:

            ```bash
            pip install selenium
            ```

    - Selenium requires a headless web browser driver, typically this is either:
        - [Chromedriver](./#).
        - [Firefoxdriver](./#).

---

### :notebook: 5/31/22

- Reviewed `pipenv` documentation in order to setup local development, outside of the VS Code devcontainer.
    - This is necessary to launch a local browser, because the devcontainer does not have a graphical browser.

- Setup `pipenv` on my local computer development environment using the [selenium_project](https://github.com/timothyhull/100daysofcode/main/blob/days/_73/selenium_project) directory:

    ```bash
    # Install pipenv
    pip install pipenv


    ```
