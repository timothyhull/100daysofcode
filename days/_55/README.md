# :calendar: Day 55: 12/25/2021-1/1/2022

---

## Topics

:clipboard: TBDStructured API Clients with `uplink`

---

## Resources

:star: [`uplink` Documentation](https://uplink.readthedocs.io/en/stable/index.html)

:star: [`uplink` on PyPI](https://pypi.org/project/uplink/)

:star: [TalkPython APIs for consuming web services with Python](https://consumerservicesapi.talkpython.fm)

---

## Tasks

:white_check_mark: Watch videos 1-6

:white_check_mark: Create initial application framework and `pytest` test framework

:white_check_mark Research the use of the `super()` method

:white_check_mark: Rewrite `pytest` tests to mock the HTTP requests, using the `requests_mock` fixture

:white_check_mark: Watch video 7

:white_check_mark: Watch video 8

:white_check_mark: Create HTTP error handling for globally, for the `BlogClient` class

:white_check_mark: Remove `raise_for_status()` references from `program.py`

:white_check_mark: Watch video 9

:white_large_square: Update `program.py` with function content that allows `pytest` tests in `test_program.py` to pass

---

## Notes

### :notebook: 12/25/21

- `uplink` is a declarative HTTP client for Python.
    - Simplifies the process and amount of code required to interact with an API (versus using the `requests` package, for example).
    - **Note** - when an organization publishes a Python SDK or installable package to interact with their API, use that instead of `uplink`, or `requests` for that matter.
        - The company will maintain the codebase, whereas `uplink` is open-source.

- `uplink` uses `requests` as its underlying HTTP client provider, by default.
    - Response objects will be of type `requests.models.Response`.
    - It is possible to use other HTTP client providers.

- To use the `uplink` client, create a class with an argument that includes `uplink.Consumer`:

    ```python
    import uplink

    class BlogClient(uplink.Consumer):

        # Create an init function that calls the __init__ function of uplink.Consumer
        def __init__(self):
            super.__init__(base_url='http://baseurl.local')

        # Create a decorated function to make an HTTP GET call to an endpoint
        @uplink.get('api/endpoint')
        def get_all_data(self):
            # No further code required in this function
    ```

- Instantiate the BlogClient class, and call the `get_all_data` function.

    ```python
    import BlogClient

    # Instantiate a copy of the BlogClient class
    blog_client = BlogClient()

    # Call the get_all_data method and assign the result to a variable
    result = blog_client.get_all_data()

    # The result variable will be a Response object from the requests package
    result.raise_for_status()
    print(result.text)
    ```

- Created the following files:

    1. [app/program.py](app/program.py) - UI for HTTP API client.
    2. [app/blog_client.py](app/blog_client.py) - HTTP API application.
    3. [tests/test_program.py](tests/test_program.py) - `pytest` tests for **program.py**.
    4. [tests/test_blog_client.py](tests/test_blog_client.py) - `pytest` tests for **blog_client.py**.

- Wrote the first `pytest` test for [app/program.py](app/program.py) to read API data using `uplink` in [app/blog_client.py](app/blog_client.py).
    - Successfully completed test.

---

### :notebook: 12/26/21

- The `super()` method allows for calling methods of an inherited class by a parent class.

    - This will be the inherited class:

        ```python
        class RaceCars():

            def __init__(self):
                self.tires = 4
                self.adjustment_points = 2
                self.fire_extinguishers = 2
                self.top_hatch = 'Optional'
                print('Race cars are fast.')

            def tires(self):
                print(f'Race cars have {self.tires} tires.')
        ```

    - This is the parent class, inheriting `RaceCars`:

        ```python
        class Toyota(RaceCars):

            def __init__(self):
                # The call to super().__init__() will initialize the RaceCars class
                super().__init__()
                self.jgr_cars = 4
                self.jgr_car_numbers = {
                    '11': {
                        'driver': 'Hamlin'
                    },
                    '18': {
                        'driver': 'Busch'
                    },
                    '19': {
                        'driver': 'Truex Jr.'
                    },
                    '20': {
                        'driver': 'Bell'
                    }
                }
                self.championships = 2

            def jgr_info(self):
                print(f'JGR has {self.jgr_cars} cars:')
                for num, driver in self.jgr_car_numbers.items():
                    print(f'  {driver.get("driver", "??")} drives car #{num}.')

                print(
                    f'\nEach car has {self.adjustment_points} '
                    'adjustment points.'
                )

            def jgr_champs(self):
                print(f'Toyota has {self.championships} championship trophies.')
        ```

    - Creating an instance of `Toyota` will run the `__init__` method in `RaceCars`, and make `RaceCars` methods and attributes available to the `Toyota` instance:

        ```python
        # This will print 'Race cars are fast.'
        t = Toyota()

        # This will print the number of tires defined in RaceCars
        t.tires

        # This will use properties of both Toyota and RaceCars
        t.jgr_cars()
        ```

---

### :notebook: 12/27/21

- Restructured `pytest` tests in [tests/test_program.py](tests/test_program.py) and [tests/test_blog_client.py](tests/test_blog_client.py).
    - Setup separate `requests_mock` objects in each file, to test the nuanced differences between creating a class instance and calling a class method directly, and reading the result of a class instance method call from a function.
    - Created tests to confirm raising of `HTTPError` exceptions.
    - Created the `test_get_user_input` function in [test/test_program.py](test/program.py), and created the `get_user_input` in [app/program.py](app/program.py)
        - Tests multiple user input values against separate expected STDOUT output results.
    - All tests successfully pass.

---

### :notebook: 12/28/21

- Watched a portion of video 7.
    - Attempting to create function to collect a specific blog entry selection, by user input.
        - Work in-progress.
- Updated `pytest` tests to support further testing.

---

### :notebook: 12/29/21

- Completed video 7.
    - Completed functions that collect and display a specific blog entry selection, by user input.
- Updated `pytest` tests to support new functionality.
    - `pytest` coverage report:

    ```bash
    root@50c4c4310ffd:/workspaces/100daysofcode/days/_55# pytest -v --disable-warnings --cov-report=term-missing --cov='.'
    ==================================================== test session starts ====================================================
    platform linux -- Python 3.9.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /usr/local/bin/python
    cachedir: .pytest_cache
    rootdir: /workspaces/100daysofcode/days/_55
    plugins: requests-mock-1.9.3, cov-3.0.0, anyio-3.3.4
    collected 8 items                                                                                                           

    tests/test_blog_client.py::test_get_all_entries PASSED                                                                [ 12%]
    tests/test_blog_client.py::test_get_all_entries_error PASSED                                                          [ 25%]
    tests/test_blog_client.py::test_get_entry PASSED                                                                      [ 37%]
    tests/test_blog_client.py::test_get_entry_error PASSED                                                                [ 50%]
    tests/test_program.py::test_get_user_input PASSED                                                                     [ 62%]
    tests/test_program.py::test_get_user_input_stdout PASSED                                                              [ 75%]
    tests/test_program.py::test_read_entries PASSED                                                                       [ 87%]
    tests/test_program.py::test_read_entries_error PASSED                                                                 [100%]

    ----------- coverage: platform linux, python 3.9.8-final-0 -----------
    Name                        Stmts   Miss  Cover   Missing
    ---------------------------------------------------------
    app/blog_client.py             13      0   100%
    app/program.py                 59     16    73%   38-42, 48-55, 119, 152-154, 172-178, 182
    tests/test_blog_client.py      37      0   100%
    tests/test_program.py          41      0   100%
    ---------------------------------------------------------
    TOTAL                         150     16    89%


    =============================================== 8 passed, 6 warnings in 0.67s ===============================================
    ```

---

### :notebook: 12/30/21

- The `uplink` module has a concept of **response handlers** that provide a way to decorate functions that handle HTTP responses from HTTP requests created by `uplink`.
    - The syntax is:

    ```python
    import requests
    import uplink

    @uplink.response_handler
    def handle_http_error(
        response: requests.models.Response
    ) -> requests.models.Response:

    """ Handle HTTP errors from uplink client requests. """

    # Check for HTTP errors, and raise an exception if necessary
    response.raise_for_status()

    # Return the response object if no errors are found
    return response
    ```

- Created the following files;

    1. [app/uplink_helper.py](app/uplink_helper.py) - Helper application for `uplink` response handlers.
    3. [tests/test_uplink_helper.py](tests/test_uplink_helper.py) - `pytest` tests for **uplink_helper.py**.

- Unable to successfully create a `pytest` test that raises an exception:
    - Attempted using the `requests_mock.get` arguments/values `status_code=404` and `exc=HTTPError`.
    - Further testing required.

---

### :notebook: 12/31/21

- Updated `pytest` tests in [tests/test_uplink_helper.py](tests/test_uplink_helper.py) to pass.
    - Unable to successfully "mock" a `requests.models.Response` object.
    - The test doesn't effectively perform a test of the function.

---

### :notebook: 1/1/22

- Removed `raise_for_status` method calls from all `Python` and `pytest` files.
    - Imported the `handle_http_error` function into [app/blog_client.py](app/blog_client.py) from [app/uplink_helper.py](app/uplink_helper.py).
    - Decorated the `BlogClient` class with the `handle_http_error` function.
        - This applies the decorator (raising an exception for HTTP errors) to all methods within the `BlogClient` class.
    - Successfully performed all `pytest` tests.

- Created the `test_write_entry` and `test_write_entry_error` test functions in [tests/test_blog_client.py](tests/test_blog_client.py).
    - Used the `requests_mock` fixture to send a mock HTTP post request with a mock `status_code` response attribute of `201`.
    - Used the `requests_mock` fixture to send a mock HTTP post error request with a mock `status_code` response attribute of `401`.
- Created the `BlogClient` method `write_entry` in [app/blog_client.py](app/blog_client.py) to write a new blog entry.
    - Decorated the `write_entry` method with the `@uplink.post` decorator.
    - Created the parameter `**kwargs` with a type of `uplink.Body`.
        - By default, `uplink` attempts to send POST requests with the `Content-Type` header set to `x-www-form-urlencoded`.
        - In the case of this API, the `Content-Type` header must be set to `application/json`.
        - Decorate the entire `BlogClient` class with `@uplink.json`, to change the `Content-Type` header for all methods in the class.

            ```python
            @uplink.json
            @handle_http_error
            class BlogClient(uplink.Consumer):
                """ Class content omitted. """
            ```

- **Digit grouping** is a numeric `int` formatting technique that adds commas as separators to large numbers (1000+).
    - Reformats numbers like `1456` to `1,456`.
    - The syntax to apply string formatting to a Python f-string is:

        ```python
        # Syntax with a number as an integer
        number = 54321
        f'This string reformats {number}, with a comma separator to {number:,}.'

        # Syntax with a number as a string
        number = '54321'
        f'This string reformats {number}, with a comma separator to {int(number):,}.'
        ```
