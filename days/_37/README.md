# :calendar: Day 37: 10/29/2021-11/1/2021

---

## Topics

:clipboard: Using CSV Data

---

## Resources

:star: [FiveThirtyEight GitHub Data](https://github.com/fivethirtyeight/data)

:star: [FiveThirtyEight GitHub Data - KSEA Weather](https://github.com/fivethirtyeight/data/tree/master/us-weather-history)

---

## Tasks

:white_check_mark: Watch videos 1-5 and create initial [`program.py`](weather_csv_demo/program.py) and [`research.py`](weather_csv_demo/research.py) files

:white_check_mark: Watch video 6 and implement `csv.DictReader` in [`research.py`](weather_csv_demo/research.py).

:white_check_mark: Watch video 7 and convert `str` data from [`seattle.csv`](weather_csv_demo/data/seattle.csv) to useful data types.

:white_check_mark: Watch video 8 and structure functions in [`research.py`](weather_csv_demo/research.py) to return and display the correct data to [`program.py`](weather_csv_demo/program.py).

:white_check_mark: Choose a data set from [FiveThirtyEight GitHub Data](https://github.com/fivethirtyeight/data) and propose a question to answer.

- [Bad Drivers data set](https://github.com/fivethirtyeight/data/tree/master/bad-drivers)
    - Answer a question regarding the comparison between drunk and distracted driving.

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

---

### :notebook: 11/1/21

- Updated [`research.py`](weather_csv_demo/research.py) with functions to support reusable data sorting and filtering:

    1. The `sort_records` function sorts weather records based on a specific CSV field, using a `lambda` function.
    2. The `create_result_set` function creates a `namedtuple` result set of the top N days from the sorted data (returned from `sort_records`).
    3. The `hot_days`, `cold_days`, and `wet_days` functions return the appropriate sorted top N results.

- Updated [`program.py`](weather_csv_demo/program.py) with code that runs functions from [`research.py`](weather_csv_demo/research.py) and displays output:

    ```bash
    root@b0498a0b5d4c:/workspaces/100daysofcode/days/_37/weather_csv_demo# ./program.py 

    Weather research for Seattle, 2014-2015

    The hottest 5 days:
    1. Date: 2014-8-11, Temperature: 96.0
    2. Date: 2014-7-1, Temperature: 94.0
    3. Date: 2015-6-27, Temperature: 92.0
    4. Date: 2014-8-4, Temperature: 91.0
    5. Date: 2014-7-12, Temperature: 90.0

    The coldest 5 days:
    1. Date: 2015-6-28, Temperature: 65.0
    2. Date: 2014-7-7, Temperature: 64.0
    3. Date: 2014-7-31, Temperature: 64.0
    4. Date: 2014-8-11, Temperature: 64.0
    5. Date: 2015-6-26, Temperature: 64.0

    The wettest 5 days:
    1. Date: 2015-3-15, Actual Precipitation: 2.2"
    2. Date: 2014-11-28, Actual Precipitation: 1.35"
    3. Date: 2014-10-22, Actual Precipitation: 1.26"
    4. Date: 2015-1-17, Actual Precipitation: 1.03"
    5. Date: 2015-2-5, Actual Precipitation: 1.03"
    ```

- Refactoring ideas:

    1. Create a `class` object in [`research.py`](weather_csv_demo/research.py) with an `__init__` function that requires a path to a CSV file.
    2. Use callable `class` methods to return the required data sets (hottest days, coldest days, etc.).
    3. Combine the `hot_days`, `cold_days`, and `wet_days` functions into a single function that sorts any data set.  Doing so should remove the need for a significant amount (2 x functions worth) of redundant code.
