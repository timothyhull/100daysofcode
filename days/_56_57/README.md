# :calendar: Day 56+57: 1/4/2022 - 1/6/2022

---

## Topics

:clipboard: TBDStructured API Clients with `uplink`

---

## Resources

:star: [TalkPython Movie Search API](https://movieservice.talkpython.fm)

---

## Tasks

:white_check_mark: Watch videos 12-13

:white_check_mark: Create a skeleton for an `uplink` API client application that searches the TalkPython Movie Search API

:white_check_mark: Create a `MovieSearchClient` class that uses `uplink` for API requests

:white_check_mark: Add global HTTP error handling to the `MovieSearchClient` class

:white_large_box: Create a UI to interact with API client application

---

## Notes

### :notebook: 1/4/22

- Created application and `pytest` framework files:

    1. [app/movie_search.py](app/movie_search.py) - UI for the Movie Search application.
    2. [app/api_client.py](app/api_client.py) - API client for the Movie Search application.
    3. [tests/test_movie_search.py](tests/test_movie_search.py) - `pytest` tests for the Movie Search application.
    4. [tests/test_api_client.py](tests/test_api_client.py) - `pytest` tests for the Movie Search application.

- Created initial `pytest` tests in [tests/test_api_client.py](tests/test_api_client.py).
    - Created the `pytest` fixture `movie_search_client` to create an instance of the `MovieSearchClient`.
    - Created the `test_title_search` function to test the `MovieSearchClient.title_search` method.
        - Setup mock JSON data sets for each of the three API endpoints.
        - Setup mock HTTP request for a single test.
- Created the `MovieSearchClient` class in [app/api_client.py](app/api_client.py).
    - Created `__init__`, `title_search`, `director_search`, and `imdb_code_search` methods.
        - Used `uplink` decorators to create HTTP requests for each `MovieSearchClient` method.
    - All `pytest` tests passing.

---

### :notebook: 1/5/22

- Completed `pytest` tests in [tests/test_api_client.py](tests/test_api_client.py).
    - Added additional tests:

        1. `test_title_search_error` - test for proper HTTP errors handling in the `MovieSearchClient.title_search` method.
        2. `test_director_search` - test the proper functionality of the `MovieSearchClient.director_search` method.
        3. `test_director_search_error` - test for proper HTTP errors handling in the `MovieSearchClient.director_search` method.
        4. `test_imdb_code_search` - test the proper functionality of the `MovieSearchClient.imdb_code_search` method.
        5. `test_imdb_code_search_error` - test for proper HTTP errors handling in the `MovieSearchClient.imdb_code_search` method.

- Added the `handle_http_error` function to [app/api_client.py](app/api_client.py).
    - Decorated with the `@uplink.response_handler` method.
    - Decorated the entire `MovieSearchClient` class with the handle_http_error to provide global HTTP error handling with the `raise_for_status()` method.

- Completed code in [app/api_client.py](app/api_client.py) to support passing all `pytest` tests.
        - All `pytest` tests pass.

---

### :notebook: 1/6/22

- Defined required program steps with line comments using the `main` function in [app/movie_search.py](app/movie_search.py).
- Created initial `pytest` tests in [tests/test_movie_search.py](tests/test_movie_search.py):

    1. `test_display_keyboard_interrupt_message`
    2. `test_display_banner`
    3. `test_invalid_input_error`
    4. `test_select_menu_option`

- Wrote functions in [app/movie_search.py](app/movie_search.py) to support passing `pytest` tests:

    1. `display_keyboard_interrupt_message`
    2. `display_banner`
    3. `invalid_input_error`
    4. `select_menu_option`

- All `pytest` tests pass.
    - `pytest` coverage report

        ```bash
        root@50c4c4310ffd:/workspaces/100daysofcode/days/_56_57/movie_search# pytest --disable-warnings -v --cov-report=term-missing --cov='.'
        ==================================================== test session starts ====================================================
        platform linux -- Python 3.9.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /usr/local/bin/python
        cachedir: .pytest_cache
        rootdir: /workspaces/100daysofcode/days/_56_57/movie_search
        plugins: requests-mock-1.9.3, cov-3.0.0, anyio-3.3.4
        collected 10 items                                                                                                          

        tests/test_api_client.py::test_title_search PASSED                                                                    [ 10%]
        tests/test_api_client.py::test_title_search_error PASSED                                                              [ 20%]
        tests/test_api_client.py::test_director_search PASSED                                                                 [ 30%]
        tests/test_api_client.py::test_director_search_error PASSED                                                           [ 40%]
        tests/test_api_client.py::test_imdb_code_search PASSED                                                                [ 50%]
        tests/test_api_client.py::test_imdb_code_search_error PASSED                                                          [ 60%]
        tests/test_movie_search.py::test_display_keyboard_interrupt_message PASSED                                            [ 70%]
        tests/test_movie_search.py::test_display_banner PASSED                                                                [ 80%]
        tests/test_movie_search.py::test_invalid_input_error PASSED                                                           [ 90%]
        tests/test_movie_search.py::test_select_menu_option PASSED                                                            [100%]

        ----------- coverage: platform linux, python 3.9.8-final-0 -----------
        Name                         Stmts   Miss  Cover   Missing
        ----------------------------------------------------------
        app/api_client.py               22      0   100%
        app/movie_search.py             38     14    63%   99-101, 106-107, 125-139, 143
        tests/test_api_client.py        49      0   100%
        tests/test_movie_search.py      30      3    90%   138-142
        ----------------------------------------------------------
        TOTAL                          139     17    88%


        ============================================== 10 passed, 6 warnings in 0.67s ===============================================
        ```

---

### :notebook: 1/7/22

- Added `test_keyword_input` function to [tests/test_movie_search.py](tests/test_movie_search.py).
    - Created `keyword_input` function in [app/movie_search.py](app/movie_search.py), to support passing `pytest` tests.

- Resolved issue of `pytest` tests for a `side_effect` of input values failing to run tests using a loop over the test function using the keyword argument of the `@patch` fixture.
    - All side effects need their own function call, and cannot be looped over the keyword argument of the `@patch` fixture.

---

### :notebook: 1/8/22

- Added `test_get_search_results` function to [tests/test_movie_search.py](tests/test_movie_search.py).
    - Created `get_search_results` function in [app/movie_search.py](app/movie_search.py), to support passing `pytest` tests.
    - All `pytest` tests pass.
