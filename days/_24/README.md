## :calendar: Day 24: 8/19/2021-8/22/2021

---

## Topics:

:clipboard: Write Your Own Decorator

---

## Resources:

:star: TBD

---

## Tasks:

:white_check_mark: Write a useful decorator

:white_check_mark: Add regex renaming functionality to replace mid-word spaces with **_**

:white_check_mark: Add option to auto-create `namedtuple` field names

:white_large_square: Create open-source release of decorator on GitHub and PyPi

---

## Notes:

#### :notebook: 8/19/21

- Ideas for a useful decorator:
    - [ ] Convert a text string into URL-encoded format.
    - [ ] Convert a text string into a code-safe format.
        - I.e. Convert "Demo Server #1" to "demo-server-1".
    - [X] **Convert a `tuple` to a `namedtuple`.**

- Created `pytest` tests in [test_name_that_tuple.py](test_name_that_tuple.py) to test for a decorated function that converts an iterable into a `namedtuple`.
- Created a decorated function in [name_that_tuple.py](name_that_tuple.py) that converts an iterable into a `namedtuple`.

---

#### :notebook: 8/20/21

- [test_name_that_tuple.py](test_name_that_tuple.py)
    - Completed docstrings.
    - Added `pytest.mark.parameterize` to test valid and invalid attribute names.

- [name_that_tuple.py](name_that_tuple.py)
    - Completed docstrings.
    - Imported the `typing` module to support `Callable` (function) and `Iterable` class typing.
    - Added the `validate_attribute_input` function to validate attribute input.
        - Used **regex** to locate invalid characters at the start of and remainder of an attribute string.
        - Automatically reformats invalid names using the `sub()` method of `re.compile`.
    - Added `ValueError` exception for length mismatches between the `iterable_input` and `attribute_names` arguments.

---

#### :notebook: 8/21/21

- [test_name_that_tuple.py](test_name_that_tuple.py)
    - Added `pytest` test to determine if a custom decorated function not found in [name_that_tuple.py](name_that_tuple.py) would work correctly.
    - Also tested to determine if setting the `auto_attribute_names` parameter to `True` would cause the decorator function `@named_tuple_converter` to automatically generate `namedtuple` attribute names.
    - Removed excess test data constants after updating automatic `namedtuple` attribute name reformatting regex rules in [name_that_tuple.py](name_that_tuple.py).
        - Space characters mid-attribute name are no longer removed but instead replaced with a **_** character.

- [name_that_tuple.py](name_that_tuple.py)
    - Modified regex automatic `namedtuple` attribute name reformatting rules.
        - Space characters mid-attribute name are no longer removed but instead replaced with a **_** character.
        - Space characters are stripped from the beginning and end of any attribute names.
    - Added an optional argument to the decorator function `@named_tuple_converter` named `auto_attribute_names` which, when set to `True` (default is `False`), will automatically name `namedtuple` attributes, when not supplied by the `attribute_names` argument.

---

#### :notebook: 8/22/21

- Start preparations for release of this code as an open-source project on [GitHub](https://github.com/timothyhull/namedtuple-maker) and PyPi.
    - Created VS Code development container.
    - Created [GitHub Repository](https://github.com/timothyhull/).
    - Created [GitHub Issues](https://github.com/timothyhull/issues) to track progress.
    - Created & verified [PyPi](https://pypi.org) account.

---

#### :notebook: 8/23/21

- Updated repository files in open-source [GitHub](https://github.com/timothyhull/namedtuple-maker) repository:
    - `devcontainer.json`
    - `requirements/requirements.txt`
    - Created linting and `pytest` automated CI/CD workflow testing.
