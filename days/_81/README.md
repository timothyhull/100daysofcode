# :calendar: Day 81: 6/28/2022-7/5/22

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
    - `get_user_input` - Collects user input data for DB record.
    - `add_db_records` - Adds new rows to the DB.
        - **Both functions are incomplete.**

---

### :notebook: 6/29/22

- Completed the `get_user_input` and `add_db_records` functions in [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py).

- Added functions to [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py):
    - `quit_program` - Quit the program.
    - `display_menu` - Display a menu of options for user input.

- Tested inputs and data validation.

---

### :notebook: 6/30/22

- Updated variable and function names for reusability.
    - `UserInput` --> `DBData`
    - `display_menu` --> `display_main_menu`
    - `get_user_input` --> `get_db_query_input`
    - `user_input` --> `new_record_input`
- Revised the `display_menu` function.
- Corrected instances of using the `display_banner` function without printing the result/return value.
- **Added functionality to allow a user to return to the main menu.**
- added the `query_db` function to either get all DB rows, or search for a specific row using the `name` field.
- Added looping over the main menu, to allow a user to use the menu selections indefinitely

---

### :notebook: 7/1/22

- Functionally decomposed [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py), separating all but the `main` function to separate files:
    - [`DTFLDB/db_data.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_data.py)
    - [`DTFLDB/db_insert.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_insert.py)
    - [`DTFLDB/db_query.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_query.py)
    - [`DTFLDB/db_setup.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_setup.py)
    - [`DTFLDB/display_banner.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/display_banner.py)
    - [`DTFLDB/display_main_menu.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/display_main_menu.py)
    - [`DTFLDB/get_db_query_input.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/get_db_query_input.py)
    - [`DTFLDB/get_new_record_input.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/get_new_record_input.py)
    - [`DTFLDB/quit_program.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/quit_program.py)

---

### :notebook: 7/2/22

- Refactored files in the [`DTFLDB`](https://github.com/timothyhull/100daysofcode/tree/main/days/_81/DTFLDB) folder, migrating all constants to shared constants in the `db_data` module.

- Created the framework for the function `update_db_record` in [[`DTFLDB/db_insert.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_insert.py), to update a record in the DB.

- Added code framework to the `main` function in [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py) to support updating a DB record.

- Sorted query results by name in [`DTFLDB/db_query.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_query.py).

---

### :notebook: 7/3/22

- Updated application to support code reuse and updating a DB record:
    - [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py):
        - Moved constants to [`DTFLDB/db_data.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_data.py).
        - Added function calls to `get_db_record_user_input` and `update_db_record`, to get user input for a DB record to update and update a DB record, respectively.
    - [`DTFLDB/db_data.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_data.py):
        - Added constants migrated from [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py).
    - [`DTFLDB/db_insert.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_insert.py):
        - Corrected SQL `UPDATE` clause syntax.
    - [`DTFLDB/db_query.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_query.py):
        - Updated `SELECT` SQL clause to use a `LIKE` operator and support partial name matches, instead of the `=` operator and explicit name matches only.
    - [`DTFLDB/display_main_menu.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/display_main_menu.py):
        - Migrated multiple instances of printing the text `* Invalid menu selection *` to the `invalid_menu_input` function in [`DTFLDB/output_messages.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/output_messages.py)

- Added new modules in the [`DTFLDB`](https://github.com/timothyhull/100daysofcode/tree/main/days/_81/DTFLDB) folder:
    - [`DTFLDB/get_db_record_selection.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/get_db_record_selection.py)
    - [`DTFLDB/output_messages.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/output_messages.py)

- Need to find or add a key/ID column to the DB, to prevent updating multiple records that match a `WHERE` clause.

---

### :notebook: 7/4/22

- Added new column (`id`) to the constant `DB_COLUMN_NAMES` in [[`DTFLDB/db_data.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_data.py) to serve as a DB primary key using the following syntax:

    ```python
    DB_COLUMN_SQL = (
    '('
    'id INTEGER PRIMARY KEY, '
    'name TEXT, '
    'outbound_interest_score INT, '
    'inbound_interest_score INT, '
    'num_tries INT ,'
    'fl_reason TEXT'
    ')'
    )
    ```

- Updated the `add_db_record` and `update_db_record` functions in [`DTFLDB/db_insert.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_insert.py) to support the new `id` DB column.

- Updated the `get_db_record_user_input` function in [`DTFLDB/get_db_record_selection.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/get_db_record_selection.py) to support the new `id` DB column.

- Updated the `query_db` and `display_query_results` functions in [`DTFLDB/db_query.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_query.py) to support the new `id` DB column.

---

### :notebook: 7/5/22

- Updated terminology across all `.py` files in the [`_81`](https://github.com/timothyhull/100daysofcode/tree/main/days/_81) folder by changing instances of _entry_ and _entries_ to _record_ and _records_, respectively.

- Created the file [`DTFLDB/db_delete.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_delete.py) with the function `delete_db_record`, to delete a record from the DB.

- Updated the file [`dt_fl_db.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/dt_fl_db.py) with functions to call the `delete_db_record` function in [`DTFLDB/db_delete.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_delete.py).

- Successfully tested functionality of all menu options in [`DTFLDB/db_delete.py`](https://github.com/timothyhull/100daysofcode/blob/main/days/_81/DTFLDB/db_delete.py).
