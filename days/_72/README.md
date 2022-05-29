# :calendar: Day 72: 5/22/2022-5/28/2022

---

## Topics

:clipboard: Excel Automation with `openpyxl`

---

## Resources

:star: [`openpyxl` on PyPI](https://pypi.org/project/openpyxl)

:star: [`openpyxl` documentation](https://openpyxl.readthedocs.io/en/stable)

---

## Tasks

:white_check_mark: Determine source data for challenge to populate a spreadsheet with `openpyxl`

:white_check_mark: Write application code

---

## Notes

### :notebook: 5/22/22

- Project is to create an LoE as code, sourced from a YAML file.
    - Created local Git repository (`loe_as_code`).

---

### :notebook: 5/23/22

- Created initial project files:
    - [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py) - main application.
    - [test_generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_generate_loe.py) - `pytest` tests for [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py).

- Created the function `create_new_workbook` in [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py), to create a new Excel spreadsheet file.

- Created the function `test_create_new_workbook` in [test_generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_generate_loe.py), to create a new Excel spreadsheet file.

- All `pytest` tests pass.

---

### :notebook: 5/24/22

- Created the function `create_new_workbook` in [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py), to remove spreadsheet files in the data directory.

- Created the function `test_clear_workbook_dir` in [test_generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_generate_loe.py), to test removing all files from the data directory.
    - Used `unit.mock.patch.object` to mock the function call and return value.

- Refactored the function `test_create_new_workbook` in [test_generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_generate_loe.py) to use `unit.mock.patch.object`, to mock the function call and return value.

- All `pytest` tests pass.

---

### :notebook: 5/25/22

- Created the function `read_source_data` in [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py), to read LoE source YAML data from a file.

- Created the function `test_read_source_data` in [test_generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_generate_loe.py), to test reading LoE source YAML data from a file.
    - Used `unit.mock.patch.object` to mock the function call and return value.

- All `pytest` tests pass.

---

### :notebook: 5/26/22

- Created the function `create_loe` in [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py), to create an LoE from project source data.

---

### :notebook: 5/27/22

- Attempted to refactor the content of [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py) such that it works within a dedicated class.
    - Created the file [loe_object.py](https://github.com/timothyhull/loe_as_code/blob/main/app/loe_object.py) to support the LoE class object.
    - Most of the functionality works, although further testing is necessary to write new values to cells (in the `create_loe`) method.

---

### :notebook: 5/28/22

- Revised the `create_loe` method in [loe_object.py](https://github.com/timothyhull/loe_as_code/blob/main/app/loe_object.py) to correctly assign values to cell objects in a workbook.

- Created the file [test_loe_object.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_loe_object.py) by duplicating [test_generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_generate_loe.py).
    - Refactored [test_loe_object.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_loe_object.py) imports and name spaces to test the methods in the `LoEObject` class of [loe_object.py](https://github.com/timothyhull/loe_as_code/blob/main/app/loe_object.py).

- Refactored [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py) such that it only calls methods of the `LoEObject` class in [loe_object.py](https://github.com/timothyhull/loe_as_code/blob/main/app/loe_object.py), using the `main` function.

- Refactored [test_generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/tests/test_generate_loe.py) to mock a call to the `main` function in [generate_loe.py](https://github.com/timothyhull/loe_as_code/blob/main/app/generate_loe.py).
