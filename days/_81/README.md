# :calendar: Day 81: 6/28/2022

---

## Topics

:clipboard: Basic Database Access with SQLite3

---

## Resources

:star: [Python SQLite3 documentation](https://docs.python.org/3/library/sqlite3.html)

:star: [`SQLite Viewer extension for VS Code](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)

:star: [`SQLite Viewer web app](https://sqliteviewer.app)

---

## Tasks

:white_check_mark: Install SQLite Viewer extension for VS code

:white_large_square: Write application that uses an SQLite database

---

## Notes

### :notebook: 6/27/22

- Installed and tested SQLite Viewer extension for VS code.

- Created the file [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py) to host the SQLite application.

- Wrote the following functions:
    - `display_banner` - Displays program start and end banners.
    - `check_db_suffix` - Verifies the DB file name has the correct file extension `.sqlite`, or adds the correct extension.
    - `create_connect_db` - Creates and/or connects to a SQLite DB file.
    - `create_db_tables` - Creates the DB tables, or handles the `sqlite.OperationalError` exception gracefully and continues.
    - `main` - Runs the main application.

---

### :notebook: 6/28/22

- Refactored [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py) functions to return printable message strings.

- Added functions to [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py):
    - `get_user_input` - Collects user input data for DB entry.
    - `add_db_entries` - Adds new rows to the DB.
        - **Both functions are incomplete.**
