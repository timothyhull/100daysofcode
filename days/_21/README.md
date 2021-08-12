## :calendar: Day 21: 8/10/2021-8/11/2021

---

## Topics:

:clipboard: `itertools`

---

## Resources:

:star: [PyBite 64](https://codechalleng.es/bites/64/)

:star: [PyBite 17](https://codechalleng.es/bites/17/)

:star: [PyBite 65](https://codechalleng.es/bites/65/)

---

## Tasks:

:white_check_mark: Complete PyBite 64

:white_large_square: Complete PyBite 17

:white_large_square: Complete PyBite 65

---

## Notes:

#### :notebook: 8/10/21

- Used [`itertools.zip_longest()`](https://docs.python.org/3/library/itertools.html#itertools.zip_longest) to [solve PyBite 64](pybite_64.py).
    - This function works similar to `zip()`, in that it combines multiple iterable objects into a `tuple` although `zip()` stops the combination process when it reaches the end of the shortest iterable specified.
    - For example, if one of the iterables in a `zip()` function has 5 elements and another has 7 elements, the `zip()` function will drop the last two elements of the longer iterable.
    - `itertools.zip_longest()` combines the iterables but instead of dropping elements in the longer iterable, it inserts another value for the shorter iterable (the default is `None`), to match with the longer iterable.

```python
# Three iterables of unequal lengths
names = 'John Paul George Ringo'.split()
hometown = 'liverpool liverpool liverpool'.split()
hair_color = 'brown'.split()

# Because 'hair_color' has one item, the zip() method will stop after one item
print(list(zip(names, hometown, hair_color)))
# Returns [('John', 'liverpool', 'brown')]

# zip_longest() will return all possible items and fill blanks with None
from itertools import zip_longest
from pprint import pprint
pprint(list(zip_longest(names, hometown, hair_color)))
""" Returns:
[('John', 'liverpool', 'brown'),
 ('Paul', 'liverpool', None),
 ('George', 'liverpool', None),
 ('Ringo', None, None)]
"""

# The 'fillvalue` kwarg will replace None fills with whatever its value is
pprint(list(zip_longest(names, hometown, hair_color, fillvalue='*')))
""" Returns:
[('John', 'liverpool', 'brown'),
 ('Paul', 'liverpool', '*'),
 ('George', 'liverpool', '*'),
 ('Ringo', '*', '*')]
```

- Used `itertools.combinations()` and `itertools.permutations()` to [solve PyBite 17](pybite_17.py).

---

#### :notebook: 8/11/21

- Used TDD methodology and created `pytest` tests in [`test_pybite_65.py`](test_pybite_65.py).
- Created functions to meet `pytest` criteria in [`pybite_65.py`](pybite_65.py).
- Success criteria progress:
    - [X] Get random letter draw.
    - [X] Get all variable length permutations of a letter draw via a helper function.
    - [X] Get all valid dictionary words from all permutations of a letter draw.
    - [ ] Score words based on individual letter values.
    - [ ] Return the letter with the highest score.
