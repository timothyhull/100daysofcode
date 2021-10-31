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

:white_check_mark: Watch videos 1-5

:white_large_square: TBD

---

## Notes

### :notebook: 10/28/21

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
    print(f'The full path directory is: {dir_name}')

    file_path = os.path.join(dir_name, file_name)
    print(f'The file path is: {file_path}')
    ```

    ```bash
    The full file path is: "/workspaces/100daysofcode/days/_37/weather_csv_demo/./file_path_test.py"
    The full path directory is: /workspaces/100daysofcode/days/_37/weather_csv_demo/.
    The file path is: /workspaces/100daysofcode/days/_37/weather_csv_demo/./temp.csv
    ```
