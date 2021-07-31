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

#### :notebook: 7/29/21

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

---

#### :notebook: 7/30/21

- The `random.sample()` function chooses `N` values from a list object.
    - Effectively, `random.sample()` is `random.choice()` with a second argument, to specify the number of values.

```python
# Import modules
from random import choice, randint, sample

# Create a list
l = 'a b c d e f g h i j k l m n o p'.split()

# Use choice() to specify a single, random chioce
choice(l)

# Use randint() and sample() to specify a random number of chioces
sample(l, randint(1, 10))
```

- The `itertools.islice()` function allows **slicing** a generator just like a `list` except `itertools.islice()` returns an iterable object, instead of the sub-list.
    - This can be useful when a looping over a generator function with a `for` loop would produce an infinite loop.

```python
from random import randint

def random_generator_function():
    """ Start an infinite loop, to produce a genenerated result, indifintely.
        This does NOT start looping infinitely when called, only on-demand.
            Because of the yield statement.
    """

    while True:
        # Create two random numbers
        x = randint(1, 20)
        y = randint(1000, 2000)

        # Yield the random values
        yield f'My favor numbers are {x} and {y}'

# Call the generator function to assign a generator to a variablle
r = random_generator_function()

# Yield any number of values, indifintely, with the next() function
next(r)

# Produce an infinite loop
# list(r)
```

    - Create what is effectively a generator slice with `itertools.islice()`.
        - After iteration, the iterator will be empty...
        -...because it is an iterator of a generator.

```python
from itertools import islice

# Call the generator function to assign a generator to a variablle
r = random_generator_function()

# Create a generator 'slice' (iterator) with a length of 10 with islice
i = islice(r, 10)

# Iterate over the iterator object by converting the iterator to a list
list(i)

# Alternatively, use a loop to iterate over the iterator
for v in i:
    print(v)
```
