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

- Need to revise `test_random_name_pairs` to ensure the names are unique and to test `capfd` for the correct, printed output.

---

#### :notebook: 7/28/21

- Updated `pytest` function `test_random_name_pairs` in [test_name_pairs.py](test_name_pairs.py) to consume the generator, one `next()` function at a time.
  - Used `capfd` to test for the output _name_1 is paired with name_2_.

```python
def test_random_name_pairs(capfd) -> None:
    """ Test for a list of title case name pairings, chosen at random.
        Use capfd to test for valid print output.

        Args:
            None.

        Returns:
            None.
    """

    name_pairs = random_name_pairs()
    for _ in name_pairs:
        n = next(name_pairs)
        out = capfd.readouterr()[0]
        assert f'{n[0]} is paired with {n[1]}' in out
```

- Updated function `random_name_pairs` in [name_pairs.py](name_pairs.py) to use the `split()` method on each `name_1` and `name_2`.
  - This allows me to `print()` and `yield` only the first names of the players (per the directions), using the index `0` of the `list` that results from a `split()` of the `str` _first last_.

```python
def random_name_pairs(names: list = NAMES) -> GeneratorType:
    """ Converts a list of first and last names to a generator that
        pairs two first names randomly.

        Args:
            names (list):
                A list of names.

        Returns:
            name_pair (GeneratorType).
                Generator of random name pairings
    """

    # Create a copy of names, to avoid impacting the global NAMES
    names = copy(names)
    while len(names) > 1:
        name_1 = choice(names)
        names.remove(name_1)

        name_2 = choice(names)
        names.remove(name_2)

        print(f'{name_1.split()[0]} is paired with {name_2.split()[0]}')

        # yield the first name from name_1, name_2
        yield name_1.split()[0], name_2.split()[0]
  ```
