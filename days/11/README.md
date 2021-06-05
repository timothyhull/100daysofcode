## :calendar: Day 11: 6/1/2021-6/3/2021

---

## Topics:

:clipboard: Testing with `pytest`

---

## Resources:

:star: [PyBite 39](https://codechalleng.es/challenges/39/): Writing tests with `pytest`

:star: PyBites to review `pytest` code

:star: [`pytest` examples](https://docs.pytest.org/en/latest/example/index.html)

:star: [Fake JSON API for testing (JSON Placeholder)](https://jsonplaceholder.typicode.com)

:star: [`requests-mock` documentation](https://requests-mock.readthedocs.io/en/latest/index.html)

:star: [Python **requests** exception documentation](https://jsonplaceholder.typicode.com)

:star: [`pytest` **fixtures** documentation](https://docs.pytest.org/en/6.2.x/fixture.html)

---

## Tasks:

:white_check_mark: Perform functional test HTTP request with `request-mock`

:white_large_square: Add additional tests to `requests-mock`

:white_large_square: Complete PyBite 39

---

## Notes:

#### :notebook: 6/1/21

- Attempted to implement `requests-mock` to test the [Smart Meeting Light](https://github.com/wwt/smart-meeting-light) application but unsuccessful.
  - Basic testing from documentation fails, further reading and testing required

```python
In [1]: import pytest

In [2]: import requests

In [3]: def test_simple(requests_mock):
   ...:     requests_mock.get('http://test.com', text='data')
   ...:     assert 'data' == requests.get('http://test.com').text
   ...: 

In [4]: test_simple()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-b4991577aa6b> in <module>
----> 1 test_simple()

TypeError: test_simple() missing 1 required positional argument: 'requests_mock'

```



---

### :notebook: 6/2/21

- Determine how to test the `msg_banner` function in `helper_methods` with `pytest`.
  - Unable to read the `capfd` printed output from the Smart Meeting Light `msg_banner` function.
  - Requires further testing.

```python
#!/usr/bin/env pytest

"""Test functions in ../app/setup/helper_methods.py
"""

# Imports
import pytest
from helper_methods import msg_banner
from unittest.mock import patch

# Constants
TEST_MSG_1 = 'Test'


def test_msg_banner(capfd):
    msg_banner('test this message')

    out, _ = capfd.readouterr()
    print(capfd.readouterr())
    # assert TEST_MSG_1 in out
    # assert '-' * len(TEST_MSG_1) in out
```

```bash
# The test indicates it passes but the capfd.readouterr() does not show the printed output.
pytest -sv
==================================================================================== test session starts =====================================================================================
platform linux -- Python 3.9.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/smart-meeting-light/tests
plugins: requests-mock-1.9.3, cov-2.12.1
collected 1 item                                                                                                                                                                             

test_helper_methods.py::test_msg_banner CaptureResult(out='', err='')
PASSED

===================================================================================== 1 passed in 0.07s ======================================================================================
```



- I am not clear why although the following, independant [code](msg_banner.py) works and the [test](test_msg_banner.py) runs correctly.

```python
# msg_banner.py
#!/usr/bin/env python3


def msg_banner(msg):
    ret = f'\n{msg}\n'
    print(ret)
```

```python
# test_msg_banner.py
#!/usr/bin/env pytest

from msg_banner import msg_banner


def test_msg_banner(capfd):
    msg_banner('test')
    print(capfd.readouterr())
```

```bash
pytest -vs
==================================================================================== test session starts =====================================================================================
platform linux -- Python 3.9.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/100daysofcode/days/11
plugins: cov-2.12.0, anyio-3.1.0
collected 1 item                                                                                                                                                                             

test_msg_banner.py::test_msg_banner CaptureResult(out='\ntest\n\n', err='')
PASSED

===================================================================================== 1 passed in 0.08s ======================================================================================
```



---

#### :notebook: 6/3/21

:snake: [Functional **requests-mock** example](http_request)

* Check `pytest` **fixtures** with `pytest --fixtures`.
  * **Fixtures** are pre-coded test functions to simplify the process of conducting certain tests.
  * The Python **requests-mock** module automatically acts as its own fixture and will appear as a fixture in the output of the `pytest --fixtures` command.
    * Simply pass `requests_mock` to the test function as a parameter to use it's methods:

```python
# See the linnk above (functional requests-mock example) for full details
def test_http_request(requests_mock):
    """Test function which mocks an HTTP requests using the
       requests module.
    """

    """Create a mock get request, supply the necessary arguments,
       based on whatever the function under test requires.
    """
    requests_mock.get(
        url=URL,
        json=JSON
    )

    """With the request mocked, call the function under test.
       The function under test will use the mocked (not the actual) request.
    """
    r = http_request(url=URL)
    assert r.json() == '{}'
```



---

#### :notebook: 6/4/21

* Successfully tested `requests_mock` with the `raise_for_status()` method:

```python
# Test function, mocks a bad status code (>= 400) and makes sure the calling function
# raises an HTTPError as a result
def test_http_request_raise_for_status(requests_mock):
    """Test function which mocks an invalid status code to make sure
       the function under test raises an HTTP exception.
    """
    requests_mock.get(
        url=URL,
        status_code=400
    )

    with raises(requests.exceptions.HTTPError):
        http_request(url=URL)
```

```python
# Function under test, uses the raise_for_status message to raise an exception for a bad
# status code (>= 400)
# The try/except blocks are not necessary for the test to work, only r.raise_for_status()
def http_request(url=URL):
    try:
        r = requests.get(
            url=url,
            headers=HEADERS,
            timeout=TIMEOUT
        )

        r.raise_for_status()

        return r

    # Catch raise_for_status exceptions
    except requests.exceptions.HTTPError as e:
        print(f'{e!r}')
        raise
```

* Tests for other exceptions like `requests.exceptions.ConnectTimeout` are not successful.
  * `requests_mock` will create the exception although the function under test does not respond one way or the other to the raised exception (with `pytest.raises()`).

```python
# Test function
def test_http_connect_timeout(requests_mock):
    # Test function which mocks a connection timeout exception.
    requests_mock.get(
        url=URL,
        exc=requests.exceptions.ConnectTimeout
    )

    """Use the pytest.raises() function to determine if the function
       under test raises the ConnectTimeout exception.
    """
    # It does not matter if the function under test handles this exception or not
    # The pytest passes either way, which is wrong.  The pytest should fail if the function
    # under test is not configured to handle this exception.
    with raises(requests.exceptions.ConnectTimeout):
        http_request(url=URL)
```

```python
# Function under test
def http_request(url=URL):
    try:
        r = requests.get(
            url=url,
            headers=HEADERS,
            timeout=TIMEOUT
        )

        return r

    # Catch connection timeouts
    # The pytest passes even if this exception handling doesn't exist
    except requests.exceptions.ConnectTimeout as e:
        print(f'{e!r}')
        raise
```

