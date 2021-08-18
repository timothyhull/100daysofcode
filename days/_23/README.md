## :calendar: Day 23: 8/16/2021

---

## Topics:

:clipboard: Decorators practical challenge

---

## Resources:

:star: [Advanced Uses of Python Decorators](https://www.codementor.io/@sheena/advanced-use-python-decorators-class-function-du107nxsv)

---

## Tasks:

:white_check_mark: Complete [PyBite 22](https://codechalleng.es/bites/22/)

:white_large_square: TBD

---

## Notes:

#### :notebook: 8/16/21

- Started PyBite 22.
    - Unable to complete the challenge using the materials covered in the video lessons although one of the articles mentioned in the lesson has a reference to an article on [Advanced Uses of Python Decorators](https://www.codementor.io/@sheena/advanced-use-python-decorators-class-function-du107nxsv).
        - I am unable to pass an argument into a decorator successfully.
    - A skim of the article indicates I need to create a function that returns a decorator in order to successfully complete the task.
    - I thought I could complete this challenge in one day although this may be a good opportunity to implement some `pytest` tests, given more time.

#### :notebook: 8/16/21

- Wrote `pytest` tests for [`pybite_22.py`](pybite_22.py) in [`test_pybite_22.py`](test_pybite_22.py).
    - The first test uses `pytest.mark.parameterize` to pass values as **arguments** to the function `get_text()`.
    - The second test uses `unittest.mock.patch` to mock **`input()`** function values `get_text()`.
    - Both functions use the same input data compare that to the same expected results data.
