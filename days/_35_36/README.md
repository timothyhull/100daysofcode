# :calendar: Days 35 & 36: 10/24/2021

---

## Topics

:clipboard: Refactoring / Pythonic Code

---

## Resources

:star: [Better Code Hub](https://bettercodehub.com)

---

## Tasks

:white_check_mark: :white_large_square: Choose code to refactor - [namedtuple-maker](https://github.com/timothyhull/namedtuple-maker)

:white_check_mark: Score code with [Better Code Hub](https://bettercodehub.com)

:white_check_mark: Complete [Code Challenge #30](https://codechalleng.es/challenges/30/)

:white_large_square: Review for PEP8 best practices

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
