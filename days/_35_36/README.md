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

:white_large_square: Review PEP 257 (docstrings) best practices

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
- [] Refactor to make the `graceful_exit` function a separate module.
    - [X] namedtuple_logger.py
    - [X] namedtuple_maker.py
    - [X] test_namedtuple_logger.py
    - [X] test_namedtuple_maker.py

---

### :notebook: 10/26/21

- Start review of PEP 257 (docstrings)
    - Updated namedtuple-maker docstring `'''` quotes with `"""` quotes.
