# :calendar: Days 38 & 39: 11/2/2021-11/3/2021

---

## Topics

:clipboard: Using CSV Data

---

## Resources

:star: [Bad Drivers data set](https://github.com/fivethirtyeight/data/tree/master/bad-drivers)

---

## Tasks

:white_check_mark: Write a program that uses CSV data to answer questions about bad drivers by state

:white_check_mark: Build application framework

:white_check_mark: Complete `pytest` tests, `BadDrivers` `class`, and `program.py`.

---

## Notes

### :notebook: 11/2/21

- Created application framework

```bash
| program.py  # Main program
| app/
| --> bad_drivers.py  # Classes and methods that work with CSV data
| data/
| --> bad-drivers.csv  # CSV data
| tests/
| --> test_research.py  # Tests for research.py
```

- Created initial test function `test_bad_drivers_init` in [test_bad_drivers.py](driver_csv_demo/tests/test_bad_drivers.py).
    - Tests for the presence of the `data` attribute in the `BadDrivers` class.
- Created `BadDrivers` `class` object in [bad_drivers.py](driver_csv_demo/app/bad_drivers.py).
    - `__init__` method reads in a CSV data file and sets the `data` attribute to a list of CSV results returned by `csv.DictReader`.

---

### :notebook: 11/3/21

- Completed `pytest` tests, `BadDrivers` `class`, and `program.py`.
