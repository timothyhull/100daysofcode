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

            def Tires(self):
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
