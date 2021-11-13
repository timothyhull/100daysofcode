# :calendar: Day 43: 11/10/2021-11/12/2021

---

## Topics

:clipboard: JSON APIs and Search

---

## Resources

:star: [Talk Python Movie Search Service](https://movieservice.talkpython.fm)

---

## Tasks

:white_check_mark: Watch videos 1-7

:white_check_mark: Watch video 8

:white_check_mark: Add docstrings and comments

:white_large_square: Watch video 9

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
    - [test_api.py](movie_search/tests/test_api.py) - TDD `pytest` tests for [api.py](movie_search/app/api.py).
        - Created `pytest` and `request_mock` framework.
        - Created tests that use the `request_mock` `pytest` fixture.
            - `test_find_movie_by_title` - Performs mock API search.
            - `test_find_movie_by_title_exception` - Performs mock search request that generates an `HTTPError` exception.

---

### :notebook: 11/11/21

- Added test file [test_program.py](movie_search/tests/test_program.py):
     - Provides TDD `pytest` tests for [program.py](movie_search/program.py).
     - Performed a significant amount of troubleshooting to simulate user input and `assert` that the user input appeared in the `capsys` output.
        - I thought the `unittest.mock.patch` decorator would perform a test of each listed `side_effect` that I could compare to the `capsys` output, with only **one** call of the `program.main` function.
        - Instead, I had to call `program.main` once for each `side_effect`:

        ```python
        from unittest.mock import patch

        INPUT_KEYWORDS = [
            'terminator',
            'run',
            'home'
        ]

        @patch(
            'builtins.input',
            side_effect=INPUT_KEYWORDS
        )
        def test_main_program_output(
            user_input,
            capsys: _pytest.capture.capsys,
        ) -> None:
            # Loop over the side_effect values, call the program.main function, and search for each side_effect within capsys
            for keyword in INPUT_KEYWORDS:
                program.main()
                out = capsys.readouterr().out
                assert keyword in out

            return None
        ```

- Added an `input` function to `api.py`, to allow user input for search keywords.
- Refactored `program.py` to use a `namedtuple`.
    - Using type hints in the `find_movie_by_title` function allowed VS Code to provide field name suggestions when formatting output.

    ```python
    from collections import namedtuple
    from typing import List
    import requests

    Movies = namedtuple(
        typename='Movies',
        field_names=[
            'imdb_code',
            'title',
            'director',
            'keywords',
            'duration',
            'genres',
            'rating',
            'year',
            'imdb_score'
        ]
    )

    # Added type hint "List[Movies]"
    def find_movie_by_title(keyword: str) -> List[Movies]:
        url = f'{BASE_URL}/{ENDPOINTS.name}/{keyword}'

        response = requests.get(
            url=url,
            timeout=5
        )

        response.raise_for_status()

        movies = []
        for movie in response.json()['hits']:
            movies.append(Movies(**movie))

        return movies
    ```

    - Adding the type hint `List[Movies]` allowed VS Code to help auto-complete movie result attributes in formatted strings:

    ```python
    from app import api

    response = api.find_movie_by_title(keyword)

    for index, movie in enumerate(response, 1):
        print(
            # Typing "movie." would show auto-complete options for the Movie namedtuple object fields (year, rating, etc.)
            f'{index}. {movie.title} ({movie.year})\n'
            f'\tRating: {movie.rating}\n'
            f'\tIMDB Score: {movie.imdb_score}\n'
            f'\tIMDB Code: {movie.imdb_code}'
        )
    ```

---

### :notebook: 11/12/21

- Added docstrings and comments to all program and test .py files.
