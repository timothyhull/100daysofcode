# :calendar: Day 72: 5/22/2022-5/31/2022

---

## Topics

:clipboard: Excel Automation with `openpyxl`

---

## Resources

:star: [`openpyxl` on PyPI](https://pypi.org/project/openpyxl)

:star: [`openpyxl` documentation](https://openpyxl.readthedocs.io/en/stable)

---

## Tasks

::white_check_mark:: Determine source data for challenge to populate a spreadsheet with `openpyxl`

:white_large_square: TBD

---

## Notes

### :notebook: 5/22/22

- Project is to create an LoE as code, sourced from a YAML file.
    - Created local Git repository (`loe_as_code`).

### :notebook: 5/23/22

- Created initial project files:
    - [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py) - main application.
    - [test_generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_generate_loe.py) - `pytest` tests for [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py).

- Created the function `create_new_workbook()` in [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py), to create a new Excel spreadsheet file.

- Created the function `create_new_workbook()` in [test_generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_generate_loe.py), to create a new Excel spreadsheet file.
    - All `pytest` tests pass.
