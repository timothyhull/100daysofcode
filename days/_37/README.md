# :calendar: Day 37: 10/29/2021

---

## Topics

:clipboard: Using CSV Data

---

## Resources

:star: [FiveThirtyEight GitHub Data](https://github.com/fivethirtyeight/data)

:star: [FiveThirtyEight GitHub Data - KSEA Weather](https://github.com/fivethirtyeight/data)

---

## Tasks

:white_check_mark: Watch videos 1-5 and create initial [`program.py`](weather_csv_demo/program.py) and [`research.py`](weather_csv_demo/research.py) files

:white_check_mark: Watch video 6 and implement `csv.DictReader` in [`research.py`](weather_csv_demo/research.py).

:white_check_mark: Watch video 7 and convert `str` data from [`seattle.csv`](weather_csv_demo/data/seattle.csv) to useful data types.

:white_large_square: TBD

---

## Notes

### :notebook: 10/29/21

- Define the path to a file in a location independent/portable way:
    - Set the name of the file to determine the path for with a string that names the file.
        - Example, `file.csv`.
    - Get the full path to the current file with `__file__`.
    - Set the base folder by looking up the directory name of the current file with `os.path.dirname(__file__)`.
    - Set the full path to the file with `os.path.join`.

    ```python
    #!/usr/bin/env python3
    import os

    file_name = 'temp.csv'

    full_path = __file__
    print(f'The full file path is: "{full_path}"')

    dir_name = os.path.dirname(full_path)
    print(f'The full path directory is: "{dir_name}"')

    file_path = os.path.join(dir_name, file_name)
    print(f'The file path is: "{file_path}"')
    ```

    ```bash
    The full file path is: "/workspaces/100daysofcode/days/_37/weather_csv_demo/./file_path_test.py"
    The full path directory is: "/workspaces/100daysofcode/days/_37/weather_csv_demo/."
    The file path is: "/workspaces/100daysofcode/days/_37/weather_csv_demo/./temp.csv"
    ```

---

### :notebook: 10/30/21

- The `csv` module (part of the Python Standard Library) has a `DictReader` function that reads a CSV file and makes each line a row of data:

    ```python
    # Open the CSV file
    with open(
         file=file_name,
         mode='rt',
         encoding='utf-8') as file:

        # Use the csv.DictReader function to convert CSV data to a dictionary
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            break

        # Each row is a dictionary object, with the header being the key, and the data being the value
        {'date': '2014-7-1', 'actual_mean_temp': '77', 'actual_min_temp': '60', 'actual_max_temp': '94', 'average_min_temp': '54', 'average_max_temp': '73', 'record_min_temp': '45', 'record_max_temp': '94', 'record_min_temp_year': '1948', 'record_max_temp_year': '2014', 'actual_precipitation': '0.00', 'average_precipitation': '0.03', 'record_precipitation': '0.75'}
    ```

    - The `DictReader` function can only read data when a file is open.
    - To make the result of a `DictReader` function available outside of a file open context manager, convert the `DictReader` into another iterable object (like a `list`):

    ```python
    # Open the CSV file
    with open(
         file=file_name,
         mode='rt',
         encoding='utf-8') as file:

        # Use the csv.DictReader function to convert CSV data to a dictionary
        reader = list(csv.DictReader(file))

    print(f'The reader object type is: {type(reader)}')
    print()

    for row in reader:
        print(f'The row object type is {type(row)}')
        print()

        print('The row data is:')
        print(row)
        print()

        print(
            'The value object type for the "actual_min_temp" key is: '
            f'{type(row.get("actual_min_temp"))}'
        )
        print()
        break
    ```

- All values within each dictionary row are strings.
    - Integer values require conversion before performing sorting or other math operations.

---

### :notebook: 10/31/21

- Refactored [`research.py`](weather_csv_demo/research.py) to return data that supports mathematical operations:
    - Moved initialization of the path to [`seattle.csv`](weather_csv_demo/data/seattle.csv) outside of the `init` function, to constants (`CSV_BASE_PATH` and `CSV_FULL_PATH`).
    - Created am `init_csv_data` function that:

        1. Reads the CSV file.
        2. Converts the CSV file data to a list of dictionaries.
        2. Returns a `namedtuple` object (`Record`) with the CSV file names as `namedtuple` attribute names.
        4. Returns the list of dictionaries with the CSV file data (`csv_data`).

    - Created a `parse_row` function that:

        1. Converts numeric string values in `csv_data` dictionaries to `float` objects.
        2. Converts a CSV row (dictionary in the `csv_data` `list` object) to a `namedtuple` object (`record`).

    - Updated the `init` function to:

        1. Create the `Record` `namedtuple` object and retrieve the `csv_data` dictionary (by calling the `init_csv_data` function) and creating a list of `namedtuple` objects (`data`) with the original CSV string values converted into `float` values (by looping over `csv_data` and calling the `parse_row` for each row/dictionary in the `csv_data` `list`).
