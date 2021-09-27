# :calendar: Day 31: 9/22/2021-9/26/21

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

:white_large_square: Watch videos 6-8

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
  - `critical` – for errors that lead to termination
  - `error` – for errors that occur, but are handled
  - `warning` – for exceptional circumstances that might not be errors
    - `warn` - an alias for `warning`
  - `notice` – for non-error messages you usually want to see
  - `info` – for messages you usually don’t want to see
  - `debug` – for debug messages

- Alternatively, there is the `log()` method that takes the logging level (string or integer) as an argument.

- Other Logging Levels:
  - `fatal`
  - `notset`
  - `trace`

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

- To 
- Reviewed and revised [logging.ipynb](logging.ipynb) Jupyter Notebook.
- Inserted `init_logging` function into [starter_movie_search/program.py](starter_movie_search/program.py).
