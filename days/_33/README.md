# :calendar: Day 33: 9/30/21

---

## Topics

:clipboard: Logging

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Create file and function to initialize logging.

:white_large_square: Add logging to the [namedtuple-maker](https://github.com/timothyhull/namedtuple-maker) application.

:white_large_square: Add ability to log to the console.

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

- - Added logging statements to:
    - Decorator function initiation.
    - Function decorated with @wraps.
    - Call of decorated function.
