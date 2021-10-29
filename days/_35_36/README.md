# :calendar: Days 35 & 36: 10/24/2021-10/26/2021

---

## Topics

:clipboard: Refactoring / Pythonic Code

---

## Resources

:star: [Better Code Hub](https://bettercodehub.com)

:star: [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

---

## Tasks

:white_check_mark: :white_large_square: Choose code to refactor - [namedtuple-maker](https://github.com/timothyhull/namedtuple-maker)

:white_check_mark: Score code with [Better Code Hub](https://bettercodehub.com)

:white_check_mark: Complete [Code Challenge #30](https://codechalleng.es/challenges/30/)

:white_check_mark: Review for PEP 8 best practices

:white_check_mark: Review PEP 257 (docstrings) best practices

---

## Notes

### :notebook: 10/24/21

- Initial Better Code Hub score of 8/10
    - <img src='https://bettercodehub.com/edge/badge/timothyhull/namedtuple-maker?branch=main'>
- The two failed guidelines are:
    1. _Write Short Units of Code_
        - Applies to **namedtuple_maker.py** and **namedtuple_logger.py**.
        - The length of the functions is exacerbated by logging.
    2. _Keep Unit Interfaces Small_
        - Two functions have 3 parameters, and the best practice is 2.
        - **namedtuple_logger.py**

            ```python
            def initialize_logging(
                log_level: str = None,
                log_file: str = LOG_FILE,
                log_to_console: bool = False
            ) -> None:
            ```

        - **namedtuple_maker.py**

            ```python
            @named_tuple_converter
            def make_named_tuple(
                iterable_input: Iterable,
                attribute_names: Iterable[str] = None,
                auto_attribute_names: bool = False
            ) -> tuple:
            ```

---

### :notebook: 10/25/21

Refactoring notes:

- Reduce docstrings to a maximum of 72 characters.
    - [X] namedtuple_logger.py
    - [X] namedtuple_maker.py
    - [X] test_namedtuple_logger.py
    - [X] test_namedtuple_maker.py
- Break `import` statements into different groups:
    - Groups
        1. Python Standard Library
        2. Third-Party
        3. Local
    - [X] namedtuple_logger.py
    - [X] namedtuple_maker.py
    - [X] test_namedtuple_logger.py
    - [X] test_namedtuple_maker.py
- Ensure all functions with reachable endings use a `return` statement.
    - `return None` should be explicitly defined.
    - [X] namedtuple_logger.py
    - [X] namedtuple_maker.py
    - [X] test_namedtuple_logger.py
    - [X] test_namedtuple_maker.py
- Refactor to make the `graceful_exit` function a separate module.
    - [X] namedtuple_logger.py
    - [X] namedtuple_maker.py
    - [X] test_namedtuple_logger.py
    - [X] test_namedtuple_maker.py

---

### :notebook: 10/26/21

- Started review of PEP 257 (docstrings)
    - Updated namedtuple-maker docstring `'''` quotes with `"""` quotes.

---

### :notebook: 10/27/21

- Completed review of PEP 257 (docstrings)
    - Reformatted all docstrings to comply with PEP 257 guidelines.

---

### :notebook: 10/28/21

- Completed refactoring to the extend possible, with integrated logging (`Logbook`) code.
    - Updated docstrings.
    - Updated logging levels, removing invalid levels and ordering levels correctly.
    - Changed default logging to `CRITICAL` from `INFO`.
    - Updated `re` module namespace by changing the import syntax from `from re import compile, VERBOSE` to `import re`.
        - This makes the code more readable, since `import re` appears to be the standard way to use `re` module elements.
        - More closely complies with The Zen of Python, _"There should be one-- and preferably only one --obvious way to do it."_
    - Decided against migrating attribute name check functionality from `namedtuple_maker.py` to `namedtuple_maker_utils.py`, because the logging configuration would have made the implementation unnecessarily complex.
