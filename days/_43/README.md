# :calendar: Day 43: 11/10/2021-11/11/2021

---

## Topics

:clipboard: JSON APIs and Search

---

## Resources

:star: [Talk Python Movie Search Service](https://movieservice.talkpython.fm)

---

## Tasks

:white_check_mark: Watch videos 1-7

:white_large_square: Watch video 8

---

## Notes

### :notebook: 11/10/21

- Watched videos 1-7
- Created files to support searching the TalkPython movie database via its REST API:
    - [api.py](movie_search/app/api.py) - API search tool.
        - Created program framework.
        - Created `find_movie_by_title` function, to search for movies by title.
    - [program.py](movie_search/program.py) - API search tool client interface.
        - Created program framework.
        - Created `main` function, to create search requests.
    - [test_api.py](movie_search/tests/test_api.py) - TDD `pytest` tests for `api.py`.
        - Created `pytest` and `request_mock` framework.
        - Created tests that use the `request_mock` `pytest` fixture.
            - `test_find_movie_by_title` - Performs mock API search.
            - `test_find_movie_by_title_exception` - Performs mock search request that generates an `HTTPError` exception.
