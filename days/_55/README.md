# :calendar: Day 55: 12/25/2021

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

:white_large_square: Research the use of the `super()` method

:white_large_square: Rewrite `pytest` tests to mock the HTTP requests, using the `requests_mock` fixture

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
    3. [test/test_program.py](test/program.py) - `pytest` tests for **program.py**.
    4. [test/test_blog_client.py](test/blog_client.py) - `pytest` tests for **blog_client.py**.

- Wrote the first `pytest` test for [app/program.py](app/program.py) to read API data using `uplink` in [app/blog_client.py](app/blog_client.py).
    - Successfully completed test.
