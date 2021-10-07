# :calendar: Day 33: 9/30/21-10/6/21

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

:white_large_square: Review logging file output.

:white_large_square: Add ability to pass the log level as an argument (`./namedtuple-maker.py --log-level=DEBUG`).

:white_large_square: Add ability to log to the console (`./namedtuple-maker.py --log-to-console=True`).

:white_large_square: Add ability to display docstring in a terminal (`./namedtuple-maker.py --help`).

:white_large_square: Add validation to the `make_named_tuple` to confirm iterable objects are passed in (try/except for `TypeError`).

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
