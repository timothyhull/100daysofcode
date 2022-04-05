# :calendar: Day 62: 3/26/2022-4/10/2022

---

## Topics

:clipboard: Using the Github API with Python

---

## Resources

:star: [Project suggestions ("Second + third day: practice!" section)](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/61-63-github-api/github-api.ipynb)

:star: [GitHub Profiler](https://github.com/clamytoe/Github-Profiler) example application

:star: [Flask web framework on PyPI](https://pypi.org/project/Flask)

:star: [Flask web framework documentation](https://palletsprojects.com/p/flask)

---

## Tasks

:white_check_mark: Watch video 7

:white_check_mark: Select project to build (GitHub Profiler)

:white_check_mark: Create application design framework outline

:white_check_mark: Create GitHub repository for the application

:white_check_mark: Build development and runtime container environments

:white_check_mark: Add Better Code Hub Git repository integration

:white_large_square: Write application

:white_large_square: Update CMD/ENTRYPOINT instruction in the application runtime Dockerfile

:white_large_square: Fill README file

---

## Notes

### :notebook: 3/26/22

- Watched video 7.
- Selected project to build (GitHub Profiler).
- Application design framework outline:
    - Single Docker container to run:
        - `SQLite` database.
        - `SQLAlchemy` ORM.
        - Python core application.
        - Flask web service.
        - `.env` file to support token-authenticated API access (increasing the rate limiting capacity).
    - Web form to accept a search string for a GitHub username.
    - API calls to GitHub using `PyGithub` to retrieve GitHub profile information.
        - Username.
        - Profile picture.
        - Bio.
        - Company.
        - Top N followers with profile pictures and clickable links to retrieve GitHub profile information.
        - Top N following with profile pictures and clickable links to retrieve GitHub profile information.
        - TOP N Starred repositories with profile pictures and clickable links to retrieve GitHub profile information.
        - Top N repositories, based on some criteria (number of commits, number of starts, number of forks, etc.)
        - Contribution activity (number of commits, PRs, etc.) in the last N months.
        - N most recent Gists
    - Temporary (in memory) storage of API data in `SQLite`.
    - Render API data in a readable, friendly way.
        - Display profile information, based on API call data.
        - List repositories with descriptive icons/emojis (a fork next to forked repositories, etc.)

---

### :notebook: 3/27/22

- Created [GitHub Profiler repository](https://github.com/timothyhull/github_profiler) framework.
    - Created development environment using VS Code development container.

---

### :notebook: 3/28/22

- Added `Flask` to:
    - [requirements/requirements.txt](https://github.com/timothyhull/github_profiler/blob/main/requirements/requirements.txt)
    - [requirements/requirements_dev.txt](https://github.com/timothyhull/github_profiler/blob/main/requirements/requirements_dev.txt)
- Added port forwarding for TCP 8080 to [.devcontainer/devcontainer.json](https://github.com/timothyhull/github_profiler/blob/main/.devcontainer/devcontainer.json)
    - Manually installed `Flask` in the development container.
    - Added the `EXPOSE` instruction to:
        - [Dockerfile](https://github.com/timothyhull/github_profiler/blob/main/Dockerfile)
        - [Dockerfile.dev](https://github.com/timothyhull/github_profiler/blob/main/Dockerfile.dev)

- Created initial `Flask` application file, [app/app.py](https://github.com/timothyhull/github_profiler/blob/main/app/app.py)
    - Successfully tested web service.

---

### :notebook: 3/29/22

- Refactored [app/app.py](https://github.com/timothyhull/github_profiler/blob/main/app/app.py) to transition from a `Flask.run` method call to a `flask run` shell command:
    - Removed `Flask.run` and constant values.

- Created initial `pytest` test in [tests/test_app.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_app.py).
    - Added `Flask` to - [requirements/requirements_pytest.txt](https://github.com/timothyhull/github_profiler/blob/main/requirements/requirements_pytest.txt).
    - Initial `pytest` test passes, and GitHub Actions workflows pass (due to having a `pytest` test available).

---

### :notebook: 3/30/22

- Added [Better Code Hub integration](https://bettercodehub.com/results/timothyhull/github_profiler).
    - Added badge to [README.md](https://github.com/timothyhull/github_profiler/blob/main/README.md).

---

### :notebook: 3/31/22

- Added GitHub Actions workflow badges to [README.md](https://github.com/timothyhull/github_profiler/blob/main/README.md).
- Followed the `Flask` tutorial through the [HTML Escaping](https://flask.palletsprojects.com/en/2.1.x/quickstart/#html-escaping) section.
- Created the `pytest` test function `test_hello` in [tests/test_app.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_app.py).
    - Created the function `hello` in [app/app.py](https://github.com/timothyhull/github_profiler/blob/main/app/app.py), using a TDD methodology to support passing `pytest` tests.
    - Used a custom route to pass a variable to the `hello` function, and display dynamic output.
    - Used the `markupsafe.escape` function to render all input as text, and prevent code injection attacks.

        ```python
        from flask import Flask
        from markupsafe import escape

        app = Flask(__name__)


        @app.route('/<name>/')  # <name> becomes a keyword argument
        def hello(name: str):
            return f'Hello, {escape(name)}.'  # Renders the value for name strictly as text (not any form of code)
        ```

---

### :notebook: 4/1/22

- Tested the [`url_for` method](https://flask.palletsprojects.com/en/2.1.x/quickstart/#url-building), which will automatically escape special characters.

    ```python
    from flask import Flask

    app = Flask(__name__)


    @app.route('/')
    def home() -> str:
        return 'This is a test'


    @app.route('/<name>/')  # <name> becomes a keyword argument
    def hello(name: str) -> str:
        return f'Hello, {name}.'


    with app.test_request_context():
    print(url_for('home'))
    print(url_for('home', next='/'))
    print(url_for('hello', name='Timmy'))
    ```

- Renamed web components from `app` to `web`:
    - [web/web.py](https://github.com/timothyhull/github_profiler/blob/main/web/web.py)
    - [tests/test_web.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_web.py)

- Created [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py) to interact with the GitHub API.

---

### :notebook: 4/2/22

- Tested GitHub authentication using an invalid GitHub token, to determine the exception `PyGithub` raises.

    ```shell
    github.GithubException.BadCredentialsException: 401 {"message": "Bad credentials", "documentation_url": "https://docs.github.com/rest"}
    ```

- Created the `pytest` file [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler.py) to test functions in [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py).
    - Created the `test_github_auth` function to test the `github_auth` function.
        - Created mock class (`Github_Mock`) for the `github.Github` object.
    - Started writing the `github_auth` function via TDD.
    - `pytest` test does not pass, and `github_auth` function does not yet work.

---

### :notebook: 4/3/22

- Conducted additional testing of the `test_github_auth` function in [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler.py).
    - Attempted to use `@patch(target='github.Github')`, to patch a class instance directly, instead of using `@patch.object(target=github, attribute='Github')`.
        - A `github.GithubException.BadCredentialsException` exception occurs, indicating that `unittest.mock.patch` does not intercept the call to `github.Github` in [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py).
    - A workaround to pass the `pytest` test is to replace the import `from github import Github` with `import github` in both [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler.py), and [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py).
        - Omitting the `from` keyword allows `unittest.mock.patch` to intercept the call to `github.Github`.

---

### :notebook: 4/4/22

- Created the `test_github_auth_login_exception` in [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler.py), to test for invalid credentials.
    - This test requires online connectivity to the GitHub API.
    - Used `pytest.mark.skipif` to conditionally skip the test when online connectivity to the GitHub API is not available.

        ```python
        from pytest import mark

        try:
            # Send a GET request to the GitHub API
            get(
                url=GITHUB_API_URL
            )

            # Set the github_api_online variable to True for successful connections
            github_api_online = True

        except ConnectionError:
            # Set the github_api_online variable to False for unsuccessful connections
            github_api_online = False

        @mark.skipif(
            condition='github_api_online == False'
        )
        def test_github_auth_login_exception() -> None:
            """ Truncated for brevity. """
        ```

- Updated the `github_auth` function in [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py) to support passing the `test_github_auth_login_exception` test.
