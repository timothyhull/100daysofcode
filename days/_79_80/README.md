# :calendar: Day 79+80: 6/20/2022-6/27/2022

---

## Topics

:clipboard: Basic Database Access with SQLite3

---

## Resources

:star: ~~[SQLite DB browser tool](https://sqlitebrowser.org) - GUI-only tool~~

:star: [Python SQLite3 documentation](https://docs.python.org/3/library/sqlite3.html)

:star: [`sqlite-web` SQLite3 web interface](https://github.com/coleifer/sqlite-web)

---

## Tasks

:white_check_mark: Watched videos 1-4

:white_check_mark: Build a simple SQLite3 Jupyter Notebook that creates a database with a table and columns

:white_check_mark: Watch video 5

:white_check_mark: Watch video 6

:white_check_mark: Watch video 7

:white_check_mark: Watch video 8

:white_check_mark: Watch video 9

:white_check_mark: Watch video 10

---

## Notes

### :notebook: 6/21/22

- Watched videos 1-4
- SQLite3 is part of the Python Standard Library and imports with:

    ```python
    import sqlite3
    ```

- ~~Installed **SQLite Browser for Linux** in the development container with the commands:~~

    ```bash
    apt-get update
    apt-get install sqlitebrowser
    ```

    - ~~SQLite Browser is a GUI tool that interacts with SQLite databases.~~

- Created the file [days/_79/simple_db/simple_db.ipynb](https://github.com/timothyhull/100daysofcode/blob/main/days/_79/simple_db/simple_db.ipynb), to create a database with a table and columns.

---

### :notebook: 6/22/22

- Reviewed [days/_79/simple_db/simple_db.ipynb](https://github.com/timothyhull/100daysofcode/blob/main/days/_79/simple_db/simple_db.ipynb).

- Determined **SQLite Browser for Linux** requires a GUI terminal.
    - Identified [`sqlite-web`](https://github.com/coleifer/sqlite-web) as an alternative.
    - Installs with `pip`:

        ```bash
        # Install sqlite-web
        pip install sqlite-web

        # Run sqlite-web, default port is 8080
        # Set a different port with -p NNNN
        # Disable automatic browser launch with -x
        sqlite_web [options] /path/to/database-file.db
        ```

- Watched video 5.

---

### :notebook: 6/23/22

- Watched video 6.

- Created the file [days/_79/simple_db/generate_db.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_79/simple_db/generate_db.py) to generate test database files.

---

### :notebook: 6/24/22

- Watched video 7.

- Updated [days/_79/simple_db/simple_db.ipynb](https://github.com/timothyhull/100daysofcode/blob/main/days/_79/simple_db/simple_db.ipynb) with steps to insert data into the database file and query/return all rows.

---

### :notebook: 6/25/22

- Watched video 8.

- Created the file [days/_79/simple_db/populate_db.py](https://github.com/timothyhull/100daysofcode/blob/main/days/_79/simple_db/populate_db.py) to insert new DB rows.

---

### :notebook: 6/26/22

- Watched video 9.

- Added cells to [days/_79/simple_db/simple_db.ipynb](https://github.com/timothyhull/100daysofcode/blob/main/days/_79/simple_db/simple_db.ipynb) that query the DB and display both raw and friendly result data.

---

### :notebook: 6/27/22

- Watched video 10.
