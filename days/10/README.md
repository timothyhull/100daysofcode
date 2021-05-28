## :calendar: Day 10: 5/25/21

---

## Topics:

:clipboard: `pytest`

---

## Resources:

:star: [Hitchhiker's Guide to Python - Testing Your Code](https://docs.python-guide.org/writing/tests/)

:star: [`pytest` Coverage Testing with `pytest-cov`](https://pypi.org/project/pytest-cov/)

---

## Tasks:

:white_check_mark: Watch videos 1-4

:white_check_mark: Watch video 5

:white_check_mark: Review video 5 `pytest` and `pytest-cov` exercises

:white_large_square: Watch next video(s)

---

## Notes:

#### :notebook: 5/25/21

:telescope: [Jupyter Notebook](pytest.ipynb) for introduction to `unittest` and `pytest`



---

#### :notebook: 5/26/21

:telescope: [Jupyter Notebook](10a/pytest_2.ipynb) for defining `pytest` tests for a file with multiple functions.

* **VIM** fast-switching shortcuts
  * While in **VIM**, `ctrl-z` switches back to the terminal, without exiting (suspending VIM only)
  * To return to **VIM**, type `fg` (foreground)

* Test for `pytest` coverage in a given file
  * Understand which lines of code are and are note tested

```bash
# The last argument is the directory to check test files for coverage
# Test files are those that start with 'test'
pytest --cov-report term-missing --cov='.'
```



---

#### :notebook: 5/27/21

:telescope: [Jupyter Notebook](10a/pytest_2.ipynb) for defining `pytest` tests for a file with multiple functions.

- Testing multiple user input values uses the `@patch` decorator with the `builtins.input` attribute argument.
- The next (keyword) argument is `side_effect` which is a list of different user input values.
- Define a function for testing (beginning with the word **test** and use and include a sequential test for each item in the `side_effect` list:
  - Use `assert` statements for each value that **should not** cause the function under test to raise an `Exception`.
  - Use the **context manager** with the `pytest.raises` method for input that **should** generate an `Exception`.

```python
import pytest

@patch(
  'builtins.input',
  # Assume the first two values are valid and the remainder would raise a ValueError
  side_effect=[12, "1", 'abc', -13, None]
)
def test_function():
  # side_effect[0]
  assert function_to_test() == 12
  # side_effect[1]
  assert function_to_test() == "1"
  # side_effect[2]
  with pytest.raise(ValueError):
    function_to_test()
  # side_effect[3]
  with pytest.raise(ValueError):
    function_to_test()
  # side_effect[4]
  with pytest.raise(ValueError):
    function_to_test()

```

