## :calendar: Day 12: 6/14/2021-6/18/2021

---

## Topics:

:clipboard: `pytest` Fixtures

---

## Resources:

:star: [PyBit `pytest` Fixtures Overview](https://pybit.es/pytest-fixtures.html)

:star: [`pytest` Fixtures Documentation](https://docs.pytest.org/en/latest/reference/reference.html?highlight=fixture#pytest.fixture)

---

## Tasks:

:white_check_mark: Review `pytest` PyBit documentation & code samples

:white_check_mark: Re-review `pytest` PyBit documentation & code samples

:white_check_mark: Implement a `pytest` fixture

---

## Notes:

#### :notebook: 6/14/21

- Reviewed `pytest` PyBit documentation and attempted refactoring of **test_setup_webex.py** `pytest` code.
  - Unable to successfully/effectively use a **fixture** in a refactor although the data in the function may not be condusive to a fixture.
  - The code doed does not successfully execute tests because the `return_value` of the `patch.object` function needs to have a `.status` attribute and it does not; it is simply a `string` with a status.
- This was good practice and the plan is to mock up a different data set tomorrow.

```python
# namedtuple to store mocked person details response from Webex
Me = namedtuple('Me', 'arg_value return_value')


# Create fixture for webex_api mock function reuse
@pytest.fixture()
def mock_webex_status():
    status_checks = [
        # Valid statuses
        ('active', 'active'),
        ('meeting', 'meeting'),
        ('presenting', 'presenting'),
        ('AccessTokenExpired', 'AccessTokenExpired'),

        # Invalid statuses
        ('new_status', UNKNOWN_STATUS),
        (True, UNKNOWN_STATUS),
        (False, UNKNOWN_STATUS),
        (None, UNKNOWN_STATUS)
    ]

    statuses = []
    for status in status_checks:
        statuses.append(Me(*status))

    return statuses


def test_webex_status(mock_webex_status):
    for mock in mock_webex_status:
        # Mock the Webex API call and response in setup_webex.webex_api
        with patch.object(
            setup_webex,
            'webex_api',
            return_value=mock.arg_value
        ):
            # Call setup_webex.get_status
            status = get_status(ACCESS_TOKEN)

            # Confirm the expected status matches the actual status
            assert status == mock.return_value

            # Display the expected and actual responses
            print(f'\nWebex status: {mock.arg_value}\n'
                  f'  Interpreted status: {status}')
```



---

#### :notebook: 6/15/21

- Reviewed `pytest` fixture reference and Smart Meeting Light code to determine if there is a use case for a fixture.
  - There are cases where it would be necessary to pass certain data into many `pytest` functions although, at this point, there is no need to computer anything so a `constant` variable, set within the **global** scope is sufficient,
  - The Smart Meeting Light app, at this time (as far as I can tell without having test coverage for most of the app) may a be a poor candidate for a `pytest` fixture test.
  - Further test development for Smart Meeting Light may reveal a use case.



---

#### :notebook: 6/16/21

- `pytest` fixture video lesson (mistakenly skipped before starting exercises)
  - Describes the article I've been working from.
- Started scratch code to build and test a simple progrem with a `pytest` fixture.
  - Program code [name_game.py](name_game.py)
  - Program test [test_name_game.py](test_name_game.py)



---

#### :notebook: 6/17/21

* Continued work on scratch `pytest` fixture app.
  * Program code [name_game.py](name_game.py)
  * Program test [test_name_game.py](test_name_game.py)
* Using TDD methodology to write tests, fail tests, and then write code to pass tests.
  * Added additional tests and supporting code



---

#### :notebook: 6/18/21

- Completed initial program code ([name_game.py](name_game.py)) and program tests ([test_name_game.py](test_name_game.py)).
  - **Renamed original test file to [test_without_fixture.py](test_without_fixture.py):**
  - New test file name is [test_with_fixture.py](test_with_fixture.py).
- All tests pass for both test files.
