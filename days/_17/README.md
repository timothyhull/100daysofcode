## :calendar: Day 17: 7/27/2021

---

## Topics:

:clipboard: Practical Exercise With Generators

---

## Resources:

:star: [Jupyter Notebook for day 17](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/16-18-listcomprehensions-generators/list-comprehensions-generators.ipynb)

---

## Tasks:

:white_check_mark: Create pytest and primary functions to create title case and reversed name order lists

:white_check_mark: Create pytest and primary functions to create a title case list, using a generator

:white_large_square: Create pytest and primary functions to randomly create first name pairs, using a generator

:white_large_square: Complete Day 17 exercise

---

## Notes:

#### :notebook: 7/27/21

- Created `pytest` functions in [test_name_pairs.py](test_name_pairs.py) to test for titled names and reversed names, using list comprehensions and generators.

- Created functions to successfully pass tests in [name_pairs.py](name_pairs.py)

  - All tests passing.

---

#### :notebook: 7/28/21

- Created `pytest` function `test_random_name_pairs` in [test_name_pairs.py](test_name_pairs.py) to pairs of first names.

- Created function `random_name_pairs` in [name_pairs.py](name_pairs.py) to create random name pairs but unable to produce the desired result.

- Need to revise `test_random_name_pairs` to ensure the names are unique and to test capfd for the correct, printed output.
