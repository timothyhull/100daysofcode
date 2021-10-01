# :calendar: Day 31: 9/22/2021-9/28/21

---

## Topics

:clipboard: Logging

---

## Resources

:star: Python [Logbook](https://logbook.readthedocs.io/en/stable/) documentation

:star: Logbook PyPI documentation

:star: Python [native logging module](https://docs.python.org/3/library/logging.html) documentation.

---

## Tasks

:white_check_mark: Watch videos 1-2

:white_check_mark: Watch video 3

:white_check_mark: Review notes and Jupyter notebook

:white_check_mark: Watch video 4

:white_check_mark: Watch video 5

:white_check_mark: Watch video 6

:white_check_mark: Watch video 7

:white_check_mark: Watch video 8

:white_check_mark: Watch videos 9-11

---

## Notes

### :notebook: 9/22/21

- Watched videos 1-2
- Logging improves observability.
- The Python `Logbook` module is a simple to use module for log files.
  - 3rd party module, installable with `pip`.
    - `pip install logbook`
  - Created by **Armin Ronacher**, the creator of the `Flask` web application framework.

- Alternative is the `logging` module in the Python Standard Library.
  - `Logger` Offers more flexibility that the `logging` module.
  - Has built-in notifiers that can send log messages to a mobile phone, desktop computer, etc.

- Logging Levels:
  - `fatal` – for errors that lead to termination.
  - `error` – for errors that occur, but are handled.
  - `warn` – for exceptional circumstances that might not be errors.
  - `info` – for messages you usually don’t want to see.
  - `debug` – for debug messages.
  - `trace` - finer level logging than debug.

- Alternatively, there is the `log()` method that takes the logging level (string or integer) as an argument.

- Other Logging Levels:
  - `critical`
    - Similar to `fatal`.
  - `warning`
    - An alias for `warn`
  - `notice`
    - Similar to `info`.
    – For non-error messages you usually want to see.
  - `notset`
    - Logging disabled.

---

### :notebook: 9/23/21

- Watched video 3.
- Reviewed logger syntax.

---

### :notebook: 9/24/21

- Created [logging.ipynb](logging.ipynb) Jupyter Notebook for notes.
- Revised notes from videos 1-2 (9/22/21).

---

### :notebook: 9/25/21

- Reviewed and revised [logging.ipynb](logging.ipynb) Jupyter Notebook.
- Inserted `init_logging` function into [starter_movie_search/program.py](starter_movie_search/program.py).

---

### :notebook: 9/26/21

- Added `logbook.Logger` commands to [starter_movie_search/program.py](starter_movie_search/program.py), to support logging for exceptions.

### :notebook: 9/27/21

- Added `logbook.Logger` commands to [starter_movie_search/api.py](starter_movie_search/api.py), to support logging for exceptions.
  - Updated log level in the `init_logging` function to `TRACE` in [starter_movie_search/program.py](starter_movie_search/program.py) (previously set to `INFO`) because `TRACE` log messages do not appear with a maximum logging level of `INFO`.

---

### :notebook: 9/28/21

- Updated the call to the `init_logging` function to include an argument for the `filename` parameter in [starter_movie_search/program.py](starter_movie_search/program.py).
  - A filename argument will, based on the logic configured in the `init_logging` function, will direct all logging output to the specified file, instead of STDOUT.
