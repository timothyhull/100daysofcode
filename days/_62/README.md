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

:star: [SQLite3 Documentation (docs.python.org)](https://docs.python.org/3/library/sqlite3.html)

:star: [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/14/orm/index.html)

<!-- :star: [SQLite3 Documentation (sqllite.org)](https://www.sqlite.org/docs.html) -->

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
    - All `pytest` tests pass.

---

### :notebook: 4/5/22

- Created the framework for the `pytest` function `test_get_github_user` in [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler.py), to test fetching a `github.NamedUser.NamedUser` or `github.AuthenticatedUser.AuthenticatedUser` object.
    - Used `iPython` to test fetching a user profile with the `github.Github.get_user` method.
    - Determined passing a username argument to the lone parameter (`login`) results in a `github.NamedUser.NamedUser` object, whereas passing no username argument results in a `github.AuthenticatedUser.AuthenticatedUser` object, even without authenticating the `github.Github` object with a token.
        - Without supplying a token, calling methods of the `github.AuthenticatedUser.AuthenticatedUser` result in a 401 error:

            ```shell
            GithubException: 401 {"message": "Requires authentication", "documentation_url": "https://docs.github.com/rest/reference/repos#list-repositories-for-the-authenticated-user"}
            ```

---

### :notebook: 4/6/22

- Created the test class `Github_Auth_Mock` in [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler.py), to mock the `github.AuthenticatedUser.AuthenticatedUser` object.
    - This class will provide object mocking the forthcoming `get_github_user` function.

---

### :notebook: 4/7/22

- Added the `get_user` method to the test class `Github_Mock` in [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler.py), to mock calls to the `github.Github.get_user` method.
- Created the function `get_github_user` in [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py), to retrieve Github user data.
    - All `pytest` tests pass, however the `get_github_user` throws an `AssertionError` exception when run outside of `pytest`.
    - Troubleshooting required.

---

### :notebook: 4/8/22

- Corrected the `AssertionError` in the `get_github_user` function for [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py).
    - `AssertionError` was the result of setting the default value for the `login` parameter in the `github.Github.get_user` method to `None`.
        - The only types allowed for the `login` parameter are `str` and `github.GithubObject._NotSetType`.
        - Updated the `get_github_user` definition to use the `Union` type class with the correct types.
        - Set the default value for the `login` parameter to `github.GithubObject.NotSet`.
    - All `pytest` tests pass and the `get_github_user` function runs correctly.

---

### :notebook: 4/9/22

- Added the `get_repos` method to the test class `Github_Auth_Mock` in [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler.py), to mock calls to the `github.AuthenticatedUser.AuthenticatedUser.get_repos` method.
- Created the function `get_github_repos` in [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py), to retrieve Github user repos.
    - All `pytest` tests pass.

---

### :notebook: 4/10/22

- Created database models file [db/db_models.py](https://github.com/timothyhull/github_profiler/blob/main/db/db_models.py).
    - Created `Repos` class to model each GitHub repo.

---

### :notebook: 4/11/22

- Created the `pytest` file [tests/test_db_models.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_db_models.py) to test classes and methods in [db/db_models.py](https://github.com/timothyhull/github_profiler/blob/main/db/db_models.py).
    - Created the test `test_repos` to test the `__repr__` method in an instance of the `Repos` class.
    - Test successfully passes.

---

### :notebook: 4/12/22

- Updated [db/db_models.py](https://github.com/timothyhull/github_profiler/blob/main/db/db_models.py) attribute naming and order for simplicity.
- Revised the `get_github_repos` function in [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py) to return a `list` of `namedtuple` objects, instead of a `github.PaginatedList.PaginatedList` object.
    - Updated `pytest` tests to pass correctly, although the test file needs cleanup around the `GitHub_PaginatedList_Mock` class.

---

### :notebook: 4/13/22

- Conducted testing to get private repos with the `AuthenticatedUser.AuthenticatedUser.get_repos` method.
    - Trued using the `git_user` parameters/arguments `visibility='private'` and `type='private`'.
    - Unable to retrieve private repositories.
- Replaced instances of the `last_modified` attribute with `updated_at`.
    - `last_modified` returned `None` for all repositories.

---

### :notebook: 4/14/22

- Created initial database interaction file, [db/db_helper.py](https://github.com/timothyhull/github_profiler/blob/main/db/db_helper.py).
- Created initial database `pytest`, [tests/db_helper.py](https://github.com/timothyhull/github_profiler/blob/main/tests/db_helper.py).
- Tested the `Sqlite3` module by creating the initial database file [db/github_profiler.db](https://github.com/timothyhull/github_profiler/blob/main/db/github_profiler.db).
    - Performed initial testing using `iPython`.

---

### :notebook: 4/15/22

- Tested using `Pathlib.Path` and `os.path.abspath` in the file [db/db_helper.py](https://github.com/timothyhull/github_profiler/blob/main/db/db_helper.py), to to generate the path to the database file automatically:

    ```python
    # Import modules
    from os.path import abspath, dirname, join
    from Pathlib import Path

    # Determine current directory
    DB_FILE_NAME = 'my_db.db'
    CURRENT_DIR = Path(dirname(__file__))
    ABS_PATH = abspath(CURRENT_DIR)
    DB_NAME = join(ABS_PATH, DB_FILE_NAME)
    ```

---

### :notebook: 4/18/22

- Added `*args` and `**kwargs` parameters to `Github_Auth_Mock.get_repos` in [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler.py).
    - Corrects `pytest` failure caused by the `get_github_repos` function in [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py), due to the keyword argument `affiliation` that is valid in `github.AuthenticatedUser.AuthenticatedUser` class, although did not exist in the `Github_Auth_Mock` class.

- Updated constants in [db/db_helper.py](https://github.com/timothyhull/github_profiler/blob/main/db/db_helper.py).
- Created SQLAlchemy engine object with the `sqlalchemy.create_engine` method, and created an `sqlalchemy.orm.session` object bound to the `sqlalchemy.create_engine` object:

    ```python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine(
        url='sqlite+pysqlite:///:memory:',
        echo=True,
        future=True
    )

    session = Session(
        engine
    )
    ```

- Created database tables with the SQLAlchemy `sqlalchemy.ext.declarative.declarative_base.metadata.create_all` function, bound to the `engine` object.

    ```python
    from db.db_models import BASE

    BASE.metadata.create_all(engine)
    ```

- Queried the `Repos` table of the database

    ```python
    from db.db_models import Repos

    session.query(Repos).all()
    ```

---

### :notebook: 4/19/22

- Refactor existing code in [db/db_helper.py](https://github.com/timothyhull/github_profiler/blob/main/db/db_helper.py) as a function (`_create_session`).

---

### :notebook: 4/20/22

- **Follow-up from 4/13/22**
    - Refreshed GitHub access token and added permission to access private repositories to the token.
    - Requesting repos with [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py) now returns all repos, public and private.

- Updated [db/db_models.py](https://github.com/timothyhull/github_profiler/blob/main/db/db_models.py):
    - Updated `Repos` docstring to show class attributes (database columns).
    - Added `private` column (`bool`) to store repository private status.
    - Updated `Repos` `__repr__` function with private repository information.

- Updated `pytest` tests to support the `Repos` class `private` attribute/DB column:
- [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler).
- [tests/test_db_models.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_db_models.py).

- Added new functions to [db/db_helper.py](https://github.com/timothyhull/github_profiler/blob/main/db/db_helper.py):
    - `commit_session`: commit staged changes to the database.
    - `truncate_tables`: clear all database table rows.
    - `get_repos`: get all repos from the database.
    - `add_repos` add repos to the database.

- Updated the `get_github_repos` function in [app/github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/app/github_profiler.py) to use the`login` attribute for the `repo.owner` attribute.
    - Returns a string of the repo owner instead of a class instance:

    ```python
    print(repo.owner)
    # NamedUser(login="timothyhull")

    print(repo.owner.login)
    # 'timothyhull'
    ```

---

### :notebook: 4/25/22

- Corrected failing `pytest` test `test_get_github_repos` in [tests/test_github_profiler.py](https://github.com/timothyhull/github_profiler/blob/main/tests/test_github_profiler).

    ```shell
    pytest -v
    =========================================================================== test session starts ============================================================================
    platform linux -- Python 3.10.4, pytest-7.1.1, pluggy-1.0.0 -- /usr/local/bin/python
    cachedir: .pytest_cache
    rootdir: /workspaces/github_profiler
    plugins: cov-3.0.0
    collected 7 items                                                                                                                                                          

    tests/test_db_models.py::test_repos PASSED                                                                                                                           [ 14%]
    tests/test_github_profiler.py::test_github_auth PASSED                                                                                                               [ 28%]
    tests/test_github_profiler.py::test_github_auth_login_exception PASSED                                                                                               [ 42%]
    tests/test_github_profiler.py::test_get_github_user PASSED                                                                                                           [ 57%]
    tests/test_github_profiler.py::test_get_github_repos FAILED                                                                                                          [ 71%]
    tests/test_web.py::test_home PASSED                                                                                                                                  [ 85%]
    tests/test_web.py::test_hello PASSED                                                                                                                                 [100%]

    ================================================================================= FAILURES =================================================================================
    __________________________________________________________________________ test_get_github_repos ___________________________________________________________________________

    github_mock_repos_obj = <MagicMock name='get_repos' id='140262883150144'>

        @patch(
            target='github.AuthenticatedUser.AuthenticatedUser.get_repos'
        )
        def test_get_github_repos(
            github_mock_repos_obj: MagicMock
        ) -> None:
            """ Test the get_github_repos function.
        
                Mock the github.PaginatedList.PaginatedList object returned by
                the github.AuthenticatedUser.AuthenticatedUser.get_repos
                method.
        
                Args:
                    github_mock_auth_obj (unittest.mock.MagicMock):
                        Mock of the github.AuthenticatedUser object.
        
                Returns:
                    None.
            """
        
            # Call the get_github_repos function with a mock AuthenticatedUser object
    >       gh_repos = get_github_repos(
                github_user_object=Github_Auth_Mock()
            )

    tests/test_github_profiler.py:257: 
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    github_user_object = <test_github_profiler.Github_Auth_Mock object at 0x7f917f50a2c0>

        def get_github_repos(
            github_user_object: AuthenticatedUser
        ) -> List:
            """ Get a user's GitHub repos.
        
                Calls the get_repos method on the
                github.AuthenticatedUser.AuthenticatedUser github_user.
        
                Args:
                    github_user (github.AuthenticatedUser.AuthenticatedUser):
                        github.AuthenticatedUser.AuthenticatedUser object for
                        a GitHub user.
        
                Returns:
                    repo_list (List):
                        List of GitHubRepo namedtuple objects for each GitHub
                        repos.
            """
        
            # Get a list of repos for a GitHub user
            repos = github_user_object.get_repos(
                affiliation=GITHUB_AFFILIATION
            )
        
            # Create a list to hold each repo as a list item
            repo_list = []
        
            # Loop over the repos PaginatedList object
            for repo in repos:
        
                # Create a GitHubRepo namedtuple object for the current repo iteration
                repo_object = GitHubRepo(
                    name=repo.name,
                    description=repo.description,
    >               owner=repo.owner.login,
                    private=repo.private,
                    url=repo.url,
                    updated_at=repo.updated_at
                )
    E           AttributeError: 'str' object has no attribute 'login'

    app/github_profiler.py:143: AttributeError
    ========================================================================= short test summary info ==========================================================================
    FAILED tests/test_github_profiler.py::test_get_github_repos - AttributeError: 'str' object has no attribute 'login'
    ======================================================================= 1 failed, 6 passed in 1.49s ======================================================================== 
    ```

    - Added the mock class `MockGithubRepositoryOwner` with a `login` attribute to match the `login` attribute of the `owner` object returned by GitHub for a repo.

    ```python
    # GitOwnerLogin mock class definition object
    class MockGithubRepositoryOwner:
        """ Mock of the PyGithub Repository class.

            The full path to the mocked object is:
                github.Repository.Repository.owner

            The object type for the path to the mock attribute
            'self.login' is:
                github.NamedUser.NamedUser
        """

        def __init__(
            self,
            owner: str
        ) -> None:

            """ Class initializer.

                Args:
                    owner (str):
                        Name of the repository owner to populate the
                        'login' attribute.

                Returns:
                    None.
            """

            self.login = owner
    ```

    - Updated the `MOCK_GITHUB_USER` constant value using :

    ```python
    MOCK_GITHUB_USER = MockGithubRepositoryOwner(owner='timothyhull')
    ```

    - All `pytest` tests pass.

- Updated load of environment variables in ... such that the script attempts to load `.env` files from the `./` directory and also the user's working directory:

    ```python
    from dotenv import load_dotenv
    from os import getcwd
    from os.path import join

    # Load environment variables from the directory of this script
    load_dotenv(
        dotenv_path='./.env'
    )

    # Load environment variables from the script user's working directory
    load_dotenv(
        dotenv_path=join(
            getcwd(), '.env'
        )
    )
    ```
