## :calendar: Day 12: 6/14/2021

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

:white_large_square: Re-review `pytest` PyBit documentation & code samples

:white_large_square: Implement a `pytest` fixture

:white_large_square: TBD

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



