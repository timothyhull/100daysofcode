# :calendar: Day 33: 9/30/21-10/15/21

---

## Topics

:clipboard: Logging

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Create file and function to initialize logging.

:white_check_mark: Add logging to the [namedtuple-maker](https://github.com/timothyhull/namedtuple-maker) application.

:white_check_mark: Review logging file output.

:white_check_mark: Add validation to the `make_named_tuple` to confirm iterable objects are passed in (try/except for `TypeError`).

:white_check_mark: Add ability to pass the log level as an environment variable (`export LOG_LEVEL=DEBUG`).

:white_check_mark: Add ability to log to the console (`export LOG_TO_CONSOLE=True`).

:white_check_mark: Update `namedtuple-maker` `pytest` tests to check for new exceptions.

:white_large_square: Add `pytest` to logging file.

---

## Notes

### :notebook: 9/30/21

- Inserted placeholder into the `namedtuple_maker.py` file.
- Started developing file named `namedtuple-logger.py`, to host all logging functions

---

### :notebook: 10/1/21

- Added basic logging initializer to `namedtuple_logger.py`.
- Unable to write logging messages within `namedtuple_maker.py`, requires further troubleshooting.

---

### :notebook: 10/2/21

- Added basic logging initializer to `namedtuple_logger.py`.
- Performed troubleshooting on inability to write log messages within `namedtuple_maker.py`.
    - Found the invalid expression `application_log.info = ('Log message')`.
    - Corrected to `application_log.info('Log message'`.
- Added logging statements to:
    - Initialize the application log.
    - Log regular expression compilations.
    - Log attribute name inputs.

---

### :notebook: 10/3/21

- Added logging statements to:
    - Decorator function initiation.
    - Function decorated with @wraps.
    - Call of decorated function.

---

### :notebook: 10/4/21

- Added logging statements to:
    - Remainder of decorator function.
    - Performed testing and reformatting.

---

### :notebook: 10/5/21

- Added logging statements to:
    - `make_named_tuple` function.
    - Tested converting different object types to a tuple, for try/except testing of `TypeError`.
        - The scenario intends to gracefully handle errors where the object type passed to the `iterable_input` and `attribute_names` parameters are not iterable.

---

### :notebook: 10/6/21

- Added logging statements to:
    - `make_named_tuple` function.
- Tested log output generation from both `pytest` run and from call of the `run_make_named_tuple` function:

```python
from namedtuple_maker.namedtuple_maker import *
run_make_named_tuple()
```

---

### :notebook: 10/7/21

- Reviewed log file output and updated formatting/order of log statements.
- Added exception handling for non-iterable object passed in the `iterable_input` parameter of the `make_named_tuple` function.

---

### :notebook: 10/8/21

- Changed default logging level in `namedtuple_maker.py` from `DEBUG` to `INFO`.
- Added code to support setting the logging level by way of the environment variable `LOG_LEVEL`.
    - Example:

```bash
# Set the environment variable
export LOG_LEVEL=DEBUG

# Open a REPL
ipython
```

```python
# Import the namedtuple_maker module and check the log file
from namedtuple_maker.namedtuple_maker import *
```

---

### :notebook: 10/9/21

- Setup framework to support console-based logging output, as an optional alternative to file-based logging.

---

### :notebook: 10/10/21

- Reorganize code to add `FileNotFoundError` exception handling for the `logbook.TimedRotatingFileHandler`.
    - Using **iPython**, unable to catch the any exception related to the `TimedRotatingFileHandler` using a **try/except** block.

---

### :notebook: 10/11/21

- Unable to determine the reason a `FileNotFoundError` exception is not caught by any `except` block.
    - Leaving the except block in the code, even if non-functional.
- Added the `.strip().upper()` methods in the check for a valid log level:
    - `if log_level.upper().strip() not in LOG_LEVELS:`
- Added `graceful_exit` function, to prevent repeating code to gracefully exit after a caught exception.
- Added code to support setting the logging destination to a file (the default setting) or to the console by way of the environment variable `LOG_TO_CONSOLE`.
    - Example:

```bash
# Set the environment variable
export LOG_TO_CONSOLE=True

# Open a REPL
ipython
```

```python
# Import the namedtuple_maker module and observer console log output
from namedtuple_maker.namedtuple_maker import *
```

---

### :notebook: 10/12/21

- Unsuccessfully attempted to write a `pytest` test function that would test for a gracefully raised error message in the `make_named_tuple` function.
    - Unable to read from the `pytest` fixtures `capsys` and `capfd` without using the `raise` keyword within the `make_named_tuple` function, and throwing a non-graceful exception.
- Determined the best course of action is to use a custom function within the `pytest` file that does not gracefully handle exceptions.
    - Used `pytest.raises` to effectively test for a `TypeError` when a non-iterable value is passed as an argument to the `iterable_input` parameter.

---

### :notebook: 10/13/21

- Created the `pytest` file test_namedtuple_logger.
    - Established framework, test scenario ideas, and started development of first test.

---

### :notebook: 10/14/21

- Unsuccessfully tested `assert` statements with:
    - `capfd`
    - `capsys`
    - `caplog`
- Even though the `logbook.StreamHandler` method specifies `stdout` as the argument to the `stream` kwarg, the built-in `pytest` **cap___** fixtures do not see log output in `stdout`.

---

### :notebook: 10/15/21

- Confirmed that `pytest` **cap___** fixture only see log output to `stdout` with the `pytest -s` option.
    - Successfully configured `test_initialize_logging_to_console` (with `pytest -s`).
