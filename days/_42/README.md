# :calendar: Day 42: 11/5/2021-11/7/2021

---

## Topics

:clipboard: JSON Data in Python

---

## Resources

:star: [PyBite 16](https://codechalleng.es/challenges/16/)

:star: [Twilio API](https://www.twilio.com/docs/sms/api)

:star: [`pytest` Reference for `requests_mock`](https://requests-mock.readthedocs.io/en/latest/pytest.html)

---

## Tasks

:white_check_mark: Choose a use case - send text messages with the Twilio API

:white_check_mark: Review Twilio API documentation

:white_check_mark: Build application framework

:white_check_mark: Update `send_msg` method to use the `_api_helper` method

:white_check_mark: Complete `twilio_app.py`

:white_check_mark: Populate docstrings and comments

:white_large_square: Complete basic `requests_mock` test

---

## Notes

### :notebook: 11/5/21

- Setup Twilio:
    - API credentials.
    - Phone number (+15034863861).
- Added `python-dotenv` and `requests-mock` to [`requirements.txt`](requirements.txt)
- Created [test_twilio_api.py](tests/test_twilio_api.py) with a `pytest` framework.
    - Temporarily bypassed TDD in order to become familiar with the Twilio API, and to re-familiarize with the `requests_mock` `pytest` fixture.
    - Need to create functional `pytest` tests and resume TDD.
- Created [twilio_api.py](pybite_16/twilio_api.py) to provide the `TwilioAPI` `class` object.
    - Created simple `__init__` method.
    - Created `send_msg` method to send an SMS message.
- Created [twilio_app.py](pybite_16/twilio_app.py) to create an instance of the `TwilioAPI` `class` object.
    - Successfully tested sending an SMS message with the following code:

    ```python
    from pybite_16.twilio_api import TwilioAPI

    twilio = TwilioAPI()

    msg = twilio.send_msg(
        account_sid=getenv('ACCOUNT_SID'),
        user_sid=getenv('USER_SID'),
        user_key=getenv('USER_KEY'),
        message_body='Python send_msg method test'
    )
    ```

---

### :notebook: 11/6/21

- Updated `.env` file and associated code.
- Refactored [twilio_api.py](pybite_16/twilio_api.py):
    - Structured `__init__` method to accept an unpacked dictionary of all environment variable values:

    ```python
    from pybite_16.twilio_api import TwilioAPI
    import dotenv

    dotenv.load_dotenv('../')
    twilio = TwilioAPI(**dotenv.dotenv_values())
    ```

    - All environment variables are passed to the `__init__` method and `TwilioAPI` methods can declare parameters only for the environment variables they need
        - The `**kwargs` parameter in the `__init__` method allows any environment variables not required by the `__init__` method to be available for other methods, without causing an exception due to undefined arguments.
    - Added new methods:
        - `_api_helper` to perform REST API requests, and avoid repeat use of the same `requests` code.
            - Created a `namedtuple` to simplify the code to choose an HTTP method for the `requests.request` method.

            ```python
            # namedtuple for simplified HTTP method selection
            HTTPMethod = namedtuple(
                typename='HTTPMethod',
                field_names=['get', 'post', 'put', 'delete']
            )
            HTTP_METHOD = HTTPMethod(
                get='GET',
                post='POST',
                put='PUT',
                delete='DELETE'
            )
            ```

        - `_api_auth` to perform an API authentication check during initialization of the `TwilioAPI` `class`.
            - Stores a variety of returned _sub-resource URIs_ in the variable `self.api_uris`.
            - Split `BASE_URL` into `BASE_URL` and `BASE_PATH` to make it simple to reference the sub-resource URIs.

            ```python
            BASE_URL = 'https://api.twilio.com'
            BASE_PATH = '/2010-04-01/Accounts'
            HTTP_ENCODING = 'json'
            ```

        - `_get_balance` to get the available account balance.
            - Created a dictionary to support a lookup of currency symbols (i.e. "$"), based on a currency code (i.e. "USD").

            ```python
            # Currency symbol lookup dictionary
            CURRENCY = {
                'USD': '$'
            }
            ```

    - Added automatic display/output of account name, account status, and account balance to the `__init__` method.

---

### :notebook: 11/7/21

- Updated the `send_msg` method to use the `_api_helper` method.
    - Added automatic display of current balance after sending a message.
- Created the `_display_balance` method to allow for reuse of the ability to display the current account balance.
- Tested using a decorator function to replace the `_api_helper` method.
    - Decorating `class` methods was a problem for using a decorator, because the methods set `self` attributes but return `None`.
    - The decorator function relies on the _decorated_ function returning a value to manipulate.
- Updated [twilio_app.py](pybite_16/twilio_app.py) to automatically instantiate an object from the `TwilioAPI` `class`, by way of the `main` function.
    - The shell command `ipython -i twilio_api.py` creates a `TwilioAPI` instance assigned to the variable `twilio`.

---

### :notebook: 11/8/21

- Populated docstrings in [twilio_api.py](pybite_16/twilio_api.py) and [twilio_app.py](pybite_16/twilio_app.py).
- Added, and refactored for, moving the to and from SMS numbers to the .env file.
    - Successfully tested `class` instantiation and methods.
