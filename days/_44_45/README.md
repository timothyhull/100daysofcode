# :calendar: Days 44+45: 11/13/2021-11/14/2021

---

## Topics

:clipboard: JSON APIs and Search

---

## Resources

:star: [Talk Python to Me API](https://search.talkpython.fm)

---

## Tasks

:white_check_mark: Setup application framework

:white_check_mark: Create program that returns and displays movie search results

:white_check_mark: Replace dictionary results with a namedtuple

:white_check_mark: Write code to open the search results in a web browser

---

## Notes

### :notebook: 11/13/21

- Created TDD program framework with:
    - [test_program.py](tests/program.py) - user interface `pytest` tests
    - [program.py](program.py) - user interface
    - [api.py](tests/api.py) - api interface `pytest` tests
    - [api.py](api/api.py) - API interface

---

### :notebook: 11/14/21

- Replaced dictionary results with a namedtuple.
- Wrote code to open the search results in a web browser.
    - Code does not work when run within a container.
