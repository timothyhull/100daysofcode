## :calendar: Day 11: 6/1/2021

---

## Topics:

:clipboard: Testing with `pytest`

---

## Resources:

:star: [PyBite 39](https://codechalleng.es/challenges/39/): Writing tests with `pytest`

:star: PyBites to review `pytest` code

:star: [`pytest` examples](https://docs.pytest.org/en/latest/example/index.html)

:star: [`requests-mock` documentation](https://requests-mock.readthedocs.io/en/latest/index.html)

---

## Tasks:

:white_large_square: Complete PyBite 39

:white_large_square: TBD

---

## Notes:

#### :notebook: 6/1/2021

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



