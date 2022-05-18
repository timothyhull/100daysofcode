# :calendar: Day 70: 5/17/2022

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

:white_large_square: Watch videos 5-8.

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
