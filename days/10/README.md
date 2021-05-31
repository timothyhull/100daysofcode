## :calendar: Day 10: 5/25/21-5/30/21

---

## Topics:

:clipboard: `pytest`

---

## Resources:

:star: [Hitchhiker's Guide to Python - Testing Your Code](https://docs.python-guide.org/writing/tests/)

:star: [`pytest` Coverage Testing with `pytest-cov`](https://pypi.org/project/pytest-cov/)

:star: [`pytest` `capfd` documentation #1](https://docs.pytest.org/en/6.2.x/capture.html)

:star: [`pytest` `capfd` documentation #2](https://docs.pytest.org/en/2.1.0/capture.html)

---

## Tasks:

:white_check_mark: Watch videos 1-4

:white_check_mark: Watch video 5 and complete exercise

:white_check_mark: Review video 5 `pytest` and `pytest-cov` exercises

:white_check_mark: Watch video 6 and complete exercisd

:white_check_mark: Review video 6 `pytest` and `pytest-cov` exercises

:white_check_mark: Watch video 7 and complete notes

:white_large_square: Watch next video(s)

---

## Notes:

#### :notebook: 5/25/21

:snake: [Exercise code](_1_unittest_vs_pytest).

:telescope: [Jupyter Notebook](pytest.ipynb) for introduction to `unittest` and `pytest`



---

#### :notebook: 5/26/21

:snake: [Exercise code](_2_mock_tests).

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



---

#### :notebook: 5/28/21

* Build coin flip guesing function to produce a boolean.

```python
# Check for heads/tails and return a boolean (True/False)
# Return a boolean (True/False)
def coin_flip(choice):
    choices = [
        'heads',
        'tails'
    ]
    print(str(choice.lower()))
    if choice.lower() not in choices:
        raise ValueError('Enter "heads" or "tails"')

    coin = random.choice(choices)
    if coin == choice.lower():
        return True
    else:
        return False
```



---

#### :notebook: 5/29/21

:telescope: [Jupyter Notebook](10a/pytest_2.ipynb) four using `capfd` to validate content printed to **stdout**.

* Use `capfd` to test a programs printing to **stdout**.
* Run `pytest` with the `-v` option to print detailed output for each test:

```bash
# Run pytest without -v, which displays the result for all tests
pytest
==================================================== test session starts ====================================================
platform linux -- Python 3.9.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /workspaces/100daysofcode/days/10/_2_mock_tests
plugins: cov-2.12.0, anyio-3.1.0
collected 3 items                                                                                                           

test_for_pytest_testing.py ...                                                                                        [100%]

===================================================== 3 passed in 0.07s =====================================================

# Run pytest -v, which displays results for each individual test
pytest -v
==================================================== test session starts ====================================================
platform linux -- Python 3.9.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/100daysofcode/days/10/_2_mock_tests
plugins: cov-2.12.0, anyio-3.1.0
collected 3 items                                                                                                           

test_for_pytest_testing.py::test_get_random_num PASSED                                                                [ 33%]
test_for_pytest_testing.py::test_get_user_input PASSED                                                                [ 66%]
test_for_pytest_testing.py::test_coin_flip PASSED                                                                     [100%]

===================================================== 3 passed in 0.07s =====================================================

```



- Run `pytest` with the `-s` option to display anything a function under tests prints to **stdout** .

```bash
# Combined here with the -v option also
pytest -vs
==================================================== test session starts ====================================================
platform linux -- Python 3.9.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/100daysofcode/days/10/_2_mock_tests
plugins: cov-2.12.0, anyio-3.1.0
collected 3 items                                                                                                           

test_for_pytest_testing.py::test_get_random_num PASSED
test_for_pytest_testing.py::test_get_user_input PASSED
test_for_pytest_testing.py::test_coin_flip 
You chose Heads, you got Tails.


PASSED

===================================================== 3 passed in 0.07s =====================================================
```



---

#### :notebook: 5/30/21

* The python `zip()` method creates **n** length tuples with **n** iterables as inputs.
  * Effictively combines multiple iterables into a `tuple` object (another iterable).
    * If the iterables are of different lenghts, `zip` stops assembling `tuple` objects whenever it exhausts all values from the shortest iterable.
  * Like a `generator` object, a `zip` object will `yield` values via iteration.

```python
# List #1
l1 = ['Tim', 'Sara', 'Lily', 'Ella']

# List #2, intentionally longer than List #1, to show that zip stops assembly when exausting the shorter list (List #1)
l2 = [41, 40, 13, 10, 99]

# Create a zip object, combining both lists
z = zip(l1, l2)

# Iterate over the zip object, outputting each tuple
for n in z:
  print(n)

# Another option is to create tuples on-the-fly, during iteration
for zipped in zip(l1, l2):
  print(zipped)
```



- Relative to `pytest`, the `zip` method is useful for comparing expected and actual content to STDOUT, by zipping a list of expected outputs with a list of actual outputs.

```python
# Import unittest.mock.patch in order to perform mock tests of STDIN values
from unittest.mock import patch

# Pass @patch.object the 'builtins.input' attribute, to capture input from the 'input()' method
# Specify the mock inputs with the 'side_effect' kwarg
@patch.object(
  'builtins.input',
  side_effect=['1', '2', '3', '4']
)

# Create a test function with a placeholder argument (inp) for mock input plus an argument (capfd) for the outputs printed by the program
def test_expected_vs_actual(inp, capfd):
  # Expected outputs
  expected = [
    '1',
    '2',
    '3',
    '4'
  ]

  # Actual printed outputs
  output = capfd.readouterr()[0] # Produces a multi-line string of inputs, with blank lines
  
  # Create a list from the `output` variable
  actual = [
    '''
    o.strip() - the value added to the list with all white space and new lines removed
    o - loop local variable for each iteration of 'output'
    output.split('\n') - convert the multi-line string into a list, each list item being 														 separated by the '\n' character (some list items will be '\n')
    if o.strip() - include the current iteration value only if a non-zero length string 											 remains after calling the strip() method.  This will exclude list items 										 which have a value of '\n'
    '''
    o.strip() for o in output.split('\n')
    if o.strip()
  ]
```



---

#### :notebook: 5/31/21

##### Test-Driven Deployment

:snake: [Exercise code](_3_fizz_buzz_tdd).

The process of writing tests, in the smallest of blocks, before writing any code to pass those tests.

- Each test should be a single `assert` statement, for example:
  - `assert function_to_test(1) == 1`
- Then write code to satisfy that test

```python
# Create a test function with a single assert statement
def test_function_to_test():
  assert function_to_test(1) == 1

# Then write code to satisfy that test
def function_to_test(number):
  return 1

# Cause the test to fail by adding another assert
def test_function_to_test():
  assert function_to_test(1) == 1
  assert function_to_test(2) == 2

# Update the function so it will pass the test
def function_to_test(number):
  return number
```



The `pytest` method `pytest.mark.parametrize` allows you to create **tuples** of **argument** and return **values** which may be passed to a single `assert` statement.

- This is in contrast to typing many `assert` statements:

```python
import pytest

# Call the pytest.mark.parameterize method with a decorator for the test function
@pytest.mark.paramertize(
  # The first argument specifies variable names for the tuple indices
	'arg_value, return_value',
  # The second argument is a list of tuples for each argument and expected return value
  [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
  ]
)
# Define the test function and pass it the variable names from the decorator
def test_function_to_test(arg_value, return_value):
  assert function_to_test(arg_value) == return_value
```

