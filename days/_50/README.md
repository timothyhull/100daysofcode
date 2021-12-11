# :calendar: Day 50: 12/11/2020

---

## Topics

:clipboard: Measuring Performance

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Create a copy of the `movie_search` application from Day 43, in the Day 50 directory.

:white_check_mark: Setup the `movie_search` application to accept search keywords as command line arguments.

:white_large_square: Determine the 5 slowest methods in the `movie_search` application.

---

## Notes

### :notebook: 12/11/20

- Setup `movie_search` application for profiling by allowing the ability to pass keyword search input as a system argument (in `sys.argv`), bypassing the manual input of keyword search text.
    - This allows profiling to run without waiting for user input.
    1. Added the `keyword_argument_check` function to [program.py](movie_search/program.py).
    2. Added and successfully tested the `test_keyword_argument_check` function to [test_program.py](movie_search/tests/test_program.py).
