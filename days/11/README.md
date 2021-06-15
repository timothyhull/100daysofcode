## :calendar: Day 11: 6/1/2021-6/13/2021

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

:closed_book: [Stack Overflow `pytest` `requests_mock` article​ #1](https://stackoverflow.com/questions/41314953/pytest-how-to-force-raising-exceptions-during-unit-testing)

:closed_book: [Stack Overflow `pytest` `requests_mock` article #2](https://stackoverflow.com/questions/50964786/mock-exception-raised-in-function-using-pytest)

:closed_book:[​ Requests Mocking with `unittest` blog](https://bhch.github.io/posts/2017/09/python-testing-how-to-mock-requests-during-tests/)

---

## Tasks:

:white_check_mark: Perform functional test HTTP request with `request-mock`

:white_check_mark: Add additional tests to `requests-mock`

:white_check_mark: Review mock test notes

:x: Troubleshoot `requests-mock` pytests exception handling

- Unable to successfully mock request exception handling

:white_check_mark: `pytest` `setup_webex.get_status` with a context manager

:white_check_mark: `pytest` `setup_webex.get_status` with multiple values using `parameterize`

:white_check_mark: Implement `pytest` tests in GitHub Actions **check-syntax** action

:white_check_mark: Complete PyBite 39

:white_large_square: `pytest` `setup_webex.get_status` with a decorator

:white_large_square: Mock tests with try/catch blocks in `setup_webex.get_status` 

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



---

#### :notebook: 6/5/21

* Attempted to use `unitest.mock.patch` in order to simulate the mock HTTP request.
  * The test either sends a _real_ HTTP request to the target (which defeats the purpose of a mock test) or the function under test does not catch the mocked exception:

```python
# Test function
from unittest.mock import patch
@patch(
    'http_request.http_request',
    side_effect=[requests.exceptions.ConnectTimeout]
)
def test_api(requests_mock):
    requests_mock.get(
        url=URL,
        exc=requests.exceptions.ConnectTimeout
    )

    # The use of this code block is what generates the undesired, real (not mocked) HTTP request
    # Strictly speaking, calling http_request() sends a real HTTP request
    with raises(requests.exceptions.ConnectTimeout):
        http_request(url=URL)
```



---

#### :notebook: 6/6/21

* Conducted additional testing and cannot find a way in which this code accurately tests the code under test:

```python
# This portion of the code works, to create a mock GET request, with an exception
def test_http_connect_timeout_exception(requests_mock):
    requests_mock.get(
        url=URL,
        exc=requests.exceptions.ConnectTimeout
    )

# If the exception in the pytest.raises() method does not match the function's exc kwarg,
# requests_mock will fail with a message (below)
with pytest.raises(requests.exceptions.ReadTimeout):
        http_request(url=URL)
```

```bash
# Exception for mismatched exceptions between requests_mock.get and pytest.raises()
def get_response(self, request):
        # if an error was requested then raise that instead of doing response
        if self._exc:
>           raise self._exc
E           requests.exceptions.ConnectTimeout
```

```python
# When the two exception statements match, pytest does not appear to be able to actually
# test/assert that the function under test can catch/andle a given exception

# This portion of the code works, to create a mock GET request, with an exception
def test_http_connect_timeout_exception(requests_mock):
    requests_mock.get(
        url=URL,
        exc=requests.exceptions.ConnectTimeout
    )

# The tests will ALWAYS pass when the exceptions match
with pytest.raises(requests.exceptions.ConnectTimeout):
        http_request(url=URL)
```



---

#### :notebook: 6/7/21

* Conducted additional testing of `requests_mock` using links referenced in documentation.
  * No success/changes with test variants.



---

#### :notebook: 6/8/21

- Switching from mocking tests with `requests_mock` to producing a mock test that helps resolve a recurring `KeyError` exception in the Smart Meeting Light app.
  - Partial success mocking up function but further testing is necessary.
  - The challenge is mocking up the `webex_api` function, which is called by the function under test, `setup_webex`.
  - This test works although further understanding and testing with a **decorator** is necessary.
    - Also need to determine the cause of a **deprecation warning** which occurs seemingly when a `pytest` script imports anything from the **setup_webex.py** file.

```python
# Test file (test_setup_webex.py)

#!/usr/bin/env pytest

# Imports
import setup_webex
from collections import namedtuple
from setup_webex import get_status
from unittest.mock import patch

# Constants
ACCESS_TOKEN = '12345'
UNKNOWN_STATUS = 'unknown'

# namedtuple for Webex person details
Me = namedtuple('Me', 'status')
me = Me('available')


def test_default_status():
    with patch.object(
        setup_webex,
        'webex_api',
        return_value=me
    ):
        assert get_status(ACCESS_TOKEN) == UNKNOWN_STATUS

```



```shell
# Test response (fail result is by design)

pytest -sv test_setup_webex.py 
============================================================================ test session starts =============================================================================
platform linux -- Python 3.9.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/smart-meeting-light/tests
plugins: requests-mock-1.9.3, cov-2.12.1
collected 1 item                                                                                                                                                             

test_setup_webex.py::test_default_status FAILED

================================================================================== FAILURES ==================================================================================
____________________________________________________________________________ test_default_status _____________________________________________________________________________

    def test_default_status():
        with patch.object(
            setup_webex,
            'webex_api',
            return_value=me
        ):
>           assert get_status(ACCESS_TOKEN) == UNKNOWN_STATUS
E           AssertionError: assert 'available' == 'unknown'
E             - unknown
E             + available

test_setup_webex.py:24: AssertionError
============================================================================== warnings summary ==============================================================================
../../../usr/local/lib/python3.9/site-packages/future/standard_library/__init__.py:65
  /usr/local/lib/python3.9/site-packages/future/standard_library/__init__.py:65: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
    import imp

-- Docs: https://docs.pytest.org/en/stable/warnings.html
========================================================================== short test summary info ===========================================================================
FAILED test_setup_webex.py::test_default_status - AssertionError: assert 'available' == 'unknown'
======================================================================== 1 failed, 1 warning in 0.23s ========================================================================

```



- Helpful resources:
  - https://stackoverflow.com/questions/57924201/python-mock-mocking-a-function-inside-the-function-im-testing
  - http://fgimian.github.io/blog/2014/04/10/using-the-python-mock-library-to-fake-regular-functions-during-tests/
  - :star: [Section 1](https://izziswift.com/python-mocking-a-function-from-an-imported-module/)



---

#### :notebook: 6/9/21

* Determined the cause of warnings generated by `pytest` for the file `setup_webex.py`.  
  * The `webexteamssdk` package performs a deprecation.
  * Resolved by creating a file at **/tests/pytest.ini** with the following content:

```ini
[pytest]
filterwarnings =
    # Disable webexteamssdk deprecation warnings
    ignore:.*the imp module.*:DeprecationWarning

# Disable all warnings
# adopts = -p no:warnings
```



- Resolved the problem of passing a namespace properly to a test function using a **mock** value when using the `from` keyword to import a module.
  - Simply use the path that follows `from` as the namespace in the `unittest.mock.patch.object` function

```python
# Import the file and function under test
from setup_webex import get_status

# Test function with mock return value for the 'webex_api' in the 'setup_webex.py' file
def test_default_status():
    with patch.object(	# Setup context manager for creating a mock return value for webex_api
        setup_webex,		# Namespace to reference (base file name)
        'webex_api',		# Function to create a mock value for
        return_value=me # Value to return from the mock function call
    ):
```



* Test now passes and requires further troubleshooting of function logic.
  * Setting `status = UNKNOWN_STATUS` at the top of the function is overwritten by the `status = me.status` line , even when a `KeyError` is thrown by the line `webex_status[status]`.

```python
#!/usr/bin/env pytest

# Imports
import setup_webex
from collections import namedtuple
from pytest import raises
from setup_webex import get_status
from unittest.mock import patch

# Constants
ACCESS_TOKEN = '12345'
STATUS = False
UNKNOWN_STATUS = 'unknown'

# namedtuple for Webex person details
Me = namedtuple('Me', 'status')
me = Me(STATUS)


def test_default_status():
    with patch.object(
        setup_webex,
        'webex_api',
        return_value=me
    ):
        print(get_status(ACCESS_TOKEN))
        # with raises(KeyError):
        #     get_status(ACCESS_TOKEN) is not None
        # assert get_status(ACCESS_TOKEN) != None
```



---

#### :notebook: 6/10/21

- Continue `pytest` testing of Smart Meeting Light application.
  - Added doc strings to **test_setup_webex.py**
  - Successfully mocked multiple `pytest` activities using `parameterize`
  - Isolated root cause of intermittant `KeyError` exceptions
    - The `pass` in `except KeyError as exception` did not, as thought, prevent the `try` block from setting an invalid status response from Webex
    - Replacing `pass` with `status = UNKNOWN_STATUS` resolves the problem
    - Updated LucidChart flow chart with the change

---

#### :notebook: 6/11/21

* Refactored and documented **test_webex_status.py** 
* Started process to incorporate `pytest` tests into the smart-meeting-light GitHub Actions automated tests.
  * Unable to successfully run tests becuse environment variables do not persist following a `docker export` in the **build** stage.
  * An alternative approach may be to use `docker commit`, `docker save`, and `docker import`.



---

#### :notebook: 6/12/21

- Performed troubleshooting of `pytest` test failures in the GitHub Action test environment container.

  - The test container does not persist environment variables from the **build** stage which causes import errors during the `pytest` run.
    - The `PYTHONPATH` environment variable is required in order to allow Python to locate the files in **/app/setup**.
  - Tested a variety of `docker commit`, `docker save`, and `docker import` command options without success.
    - Wrote SED to capture an imported, abbreviated Image SHA hash, for tagging

  ```sh
  # Extracts the first 12 characters of the 'sha256: long_hash'
  IMG=$(docker import requirements/test-env.tar | sed -E 's/^(.+:)(.{12})(.+$)/\2/')
  docker tag $IMG test-env-image
  ```

- Unable to determine root cause of failures.



---

#### :notebook: 6/13/21

* Corrected issues with refactoring automated tests in GitHub Actions.
  * After extensive troubleshooting, replaced the `docker import` command with the `docker load` command.
    * `docker import` should only be used for importing exported **Containers** (as images).
    * `docker load` should be used for Images exported using `docker save`.
* Added documentation comments to automated tests.
* All GitHub actions run correctly.

