# :calendar: Day N: 1/4/2022

---

## Topics

:clipboard: TBDStructured API Clients with `uplink`

---

## Resources

:star: [TalkPython Movie Search API](https://movieservice.talkpython.fm)

---

## Tasks

:white_check_mark: Watch videos 12-13

:white_check_mark: Create a skeleton for an `uplink` API client application that searches the TalkPython Movie Search API.

:white_large_square: Create a `MovieSearchClient` class that uses `uplink` for API requests.

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
