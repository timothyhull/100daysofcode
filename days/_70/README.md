# :calendar: Day 70: 5/17/2022-5/20/2022

---

## Topics

:clipboard: Excel Automation with `openpyxl`

---

## Resources

:star: [`openpyxl` on PyPI](https://pypi.org/project/openpyxl)

:star: [`openpyxl` documentation](https://openpyxl.readthedocs.io/en/stable)

---

## Tasks

:white_check_mark: Watch videos 1-4

:white_check_mark: Watch video 5

:white_check_mark: Watch video 6

:white_large_square: Watch videos 7-8

---

## Notes

### :notebook: 5/17/22

- `openpyxl` installs via Python pip:

    ```bash
    pip install openpyxl
    ```

    ```python
    from openpyxl import load_workbook
    ```

- _Workbook_ versus _Worksheet_:
    - The **.xlsx** file is the **workbook**.
    - Each tab within a **workbook** is a **worksheet**.

- Loading a workbook and reading worksheet names:

    ```python
    from openpyxl import load_workbook

    workbook = load_workbook('workbook_name.xlsx')

    worksheets = (workbook.sheetnames) # Returns a list of sheet names
    ```

- The `active` attribute of a workbook refers to the worksheet that was most recently edited:

    ```python
    active_worksheet = workbook.active
    ```

- Created [./blob/main/days/_70/openpyxl_automation/xl_automation.py](./blob/main/days/_70/openpyxl_automation/xl_automation.py) to support `openpyxl` testing.

---

### :notebook: 5/18/22

- Watched video 5.
    - Getting a cell value only requires that you index a `Worksheet` object by a cell coordinate ("C5", for example).

        ```python
        from openpyxl import load_workbook
        workbook = load_workbook('workbook_name.xlsx')

        worksheet = workbook[workbook.worksheets[0]]

        print(worksheet['L5'].value)
        ```

- Added `get_profit_total` to [./blob/main/days/_70/openpyxl_automation/xl_automation.py](./blob/main/days/_70/openpyxl_automation/xl_automation.py), to support gathering a total of many cells in a column.
    - The function needs additional work.

---

### :notebook: 5/19/22

- Reviewed the `get_profit_total` function in [./blob/main/days/_70/openpyxl_automation/xl_automation.py](./blob/main/days/_70/openpyxl_automation/xl_automation.py).

- Watched video 6.
    - The `openpyxl` `max_row` attribute of a worksheet displays an integer showing the highest row number that contains a value.

        ```python
        from openpyxl import load_workbook
        workbook = load_workbook('workbook_name.xlsx')

        worksheet = workbook[workbook.worksheets[0]]
        worksheet.max_row
        # Returns row number 703
        ```

- Revised the `get_profit_total` function in [./blob/main/days/_70/openpyxl_automation/xl_automation.py](./blob/main/days/_70/openpyxl_automation/xl_automation.py) to use the `openpyxl.Worksheet.max_rows` attribute as the end value for the `range` method.
