# :calendar: Day 59+60: 1/16/2022-3/15/2022

---

## Topics

:clipboard: Twitter Data Analysis With Python

---

## Resources

:star: [RealPython article: Building a web app with Bottle, SQLAlchemy, and the Twitter API](https://realpython.com/building-a-simple-web-app-with-bottle-sqlalchemy-twitter-api/)

:star: [PyBites article: Parsing Twitter Geo Data and Mocking API Calls by Example](https://pybit.es/articles/twitter-api-geodata-mocking/)

:star: [PyBites example application repository](https://github.com/pybites/pytip)

:star: [SQLAlchemy on PyPI](https://pypi.org/project/SQLAlchemy/)

:star: [SQLAlchemy documentation](https://www.sqlalchemy.org)

:star: [pgAdmin documentation](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html)

:star: [pgadmin on Docker Hub](https://hub.docker.com/r/dpage/pgadmin4/)

:star: [Bottle documentation](http://bottlepy.org/docs/dev/)

---

## Tasks

:white_check_mark: Watch video 9

:white_check_mark: Choose a project from the options in the last cell of [this notebook](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/58-60-twitter-api/twitter-api.ipynb)

:white_check_mark: Define application design/goals

:white_check_mark: Setup Git repository

:white_check_mark: Connect Git repository to Better Code Hub

:white_check_mark: Setup application framework (devcontainer, README, file structure)

:white_check_mark: Setup webhook to automatically perform bettercodehub.com analysis on push and PR events

:white_check_mark: Setup CI/CD pipelines for `yamllint`, `flake8`, and `bandit` checks

:white_check_mark: Setup CI/CD pipeline for `pytest` testing

:white_check_mark: Add Better Code Hub and CI/CD build status to README

:white_large_square: Read project article on RealPython

:white_large_square: Write application

:white_large_square: Fill README.md content

---

## Notes

### :notebook: 1/16/22

- Reviewed project options, and selected the option to [build a web app with Bottle, SQLAlchemy, and the Twitter API](https://realpython.com/building-a-simple-web-app-with-bottle-sqlalchemy-twitter-api/).
    - I will build the application using a TDD methodology, [mocking API calls to Twitter](https://pybit.es/articles/twitter-api-geodata-mocking/) with `@patch.object`.
    - I will develop the application in a separate, public repository so I can use [Better Code Hub](https://www.bettercodehub.com) to perform code analysis.
    - I will look to use other techniques I've learned in the 100DaysOfCode course, including:

        1. Decorators
        2. Classes
        3. Pytest Fixtures
        4. Logging

---

## :notebook: 1/17/22

- Application design & goals:

    1. Read tweets from the handle **@wwt_inc**.
    2. Store tweets in some form of an SQL database.
    3. Build a web interface that displays the top hashtags and mention counts, and the tweets with the most likes and retweets.
    4. Create a search form to search tweets in the database.

- Created [Git repository](https://github.com/timothyhull/ww_tweeter/) for project.
- Connected project to [Better Code Hub](https://bettercodehub.com/results/timothyhull/ww_tweeter).
- Created initial test and function, to support Better Code Hub integration.

---

## :notebook: 1/18/22

- Created core repository files:

    1. [.devcontainer/devcontainer.json](https://github.com/timothyhull/ww_tweeter/blob/main/.devcontainer/devcontainer.json) - Development container configuration.
    2. [.github.workflows/linting.yaml](https://github.com/timothyhull/ww_tweeter/blob/main/.github.workflows/linting.yaml) - GitHub action configuration for file linting and static code analysis.
    3. [requirements/requirements.txt](https://github.com/timothyhull/ww_tweeter/blob/main/requirements/requirements.txt) - Python packages.
    4. [.bettercodehub.yml](https://github.com/timothyhull/ww_tweeter/blob/main/.bettercodehub.yml) - bettercodehub.com configuration file.
    5. [.markdownlint.json](https://github.com/timothyhull/ww_tweeter/blob/main/.markdownlint.json) - `markdownlint` rule exclusions.
    6. [Dockerfile](https://github.com/timothyhull/ww_tweeter/blob/main/Dockerfile) - Development container Dockerfile.
    7. [LICENSE](https://github.com/timothyhull/ww_tweeter/blob/main/LICENSE) - Apache 2.0 license.

- Setup webhook integration between GitHub and BetterCodeHub

---

## :notebook: 1/19/22

- Setup CI/CD pipelines for `yamllint`, `flake8`, and `bandit` checks.
    - Added new files:

        1. [.bandit.yml](https://github.com/timothyhull/ww_tweeter/blob/main/.bandit.yml) - `bandit` configuration file.
        2. [.flake8](https://github.com/timothyhull/ww_tweeter/blob/main/.flake8) - `flake8` configuration file.
        3. [.yamllint](https://github.com/timothyhull/ww_tweeter/blob/main/.yamllint) - `yamllint` configuration file.
        4. [requirements/requirements_linting.txt](https://github.com/timothyhull/ww_tweeter/blob/main/requirements/requirements_linting.txt) - Requirements file for linting and static code analysis.

- Setup CI/CD pipeline for `pytest` testing.
    - Added new files:

        1. [requirements/requirements_pytest.txt](https://github.com/timothyhull/ww_tweeter/blob/main/requirements/requirements_pytest.txt) - Requirements file for `pytest` tests.
        2. [.github.workflows/pylint.yaml](https://github.com/timothyhull/ww_tweeter/blob/main/.github.workflows/pylint.yaml) - GitHub action configuration for `pytest` tests.

- All CI/CD pipelines pass.

---

## :notebook: 1/20/22

- Added GitHub badges to the [README.md](https://github.com/timothyhull/ww_tweeter/blob/main/README.md) file:

    1. GitHub Action status for linting & static code analysis.
    2. GitHub Action status for `pytest` tests.
    3. Better Code Hub quality score.

---

## :notebook: 1/21/22

- Removed `sys.path.append` lines, due to `PYTHONPATH` environment variable set in Dockerfile.
- Set environment variables in a `.env` file.
- Tested loading environment variables with `dotenv.load_dotent()` in [app/ww_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/ww_tweeter.py)
- Created new files for Twitter API integration:

    1. [tests/test_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_tweeter.py) - `pytest` tests for `tweeter.py`.
    2. [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter/tweeter.py) - Application code for Twitter API integration.

- Setup file framework in [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter/tweeter.py):

    1. Imports.
    2. `namedtuple` object for tweets.
    3. Constants for Twitter API authentication (loaded from the .env file).

    - Withholding TDD methodology until after I can read tweets from **@wwt_inc**, and understand the data set to build mock Twitter API calls with, for testing.

---

## :notebook: 1/22/22

- Started TDD process:

    1. Created the `test_twitter_auth` and `test_get_tweets` functions in [tests/test_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_tweeter.py).
    2. Created the `twitter_auth` and `get_tweets` functions in [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter/tweeter.py) to meet `pytest` test requirements.

        - Successfully passing tests with the `test_twitter_auth` function.
        - No code written in the `test_get_tweets` function yet.

---

## :notebook: 1/23/22

- Completed the `get_tweets` function in [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter/tweeter.py).
    - The function returns an object containing tweets from the Twitter API.
    - Tested using `itertools.islice` to limit the quantity of the tweets that require processing into a list.
- Worked on mocking a `tweepy.Cursor` object with `unittest.mock.patch.object`.
    - Successfully completed a mock of the `tweepy.Cursor` with some trial and error, although the mock requires a review and refactoring

---

## :notebook: 1/24/22

- Refactored the mock of the `tweepy.Cursor` object:
    - Removed `namedtuple` instances, because the field names cannot start with an underscore, and the tweet data returned by `tweepy.Cursor` is in an attribute named `_json`.
    - Created a `Status` class to mimic the `Status` class in the `tweepy.Cursor` response.
        - The `Status` class includes attributes for tweet data `_api` and `_json`.

- All `pytest` tests pass.

---

## :notebook: 1/25/22

- Updated the `get_tweets` function in [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter/tweeter.py) so that it returns a limited number of results, using `itertools.islice`.
    - Updated the `test_get_tweets` function in [tests/test_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_tweeter.py) to test for the slice limit.

- Started research to determine how to setup a model, view, controller style application that used Docker Compose to build separate containers for each element.
    - Unable to keep a PostgreSQL container build running (immediately exits with a status code of 0).

---

## :notebook: 1/26/22

- Used article at [https://graspingtech.com/docker-compose-postgresql/](https://graspingtech.com/docker-compose-postgresql/) to successfully bring a PostgreSQL container online successfully.
    - Unable to connect to the container using a web browser via [http://localhost:5432](http://localhost:5432) with an error that requires further troubleshooting.
    - `invalid length of startup packet` (full log below)

    ```bash
    bash# ww-tweeter % docker compose up  
    [+] Running 2/2
    ⠿ Network ww-tweeter_default  Created                                                                                  0.0s
    ⠿ Container ww-tweeter-db-1   Created                                                                                  0.1s
    Attaching to ww-tweeter-db-1
    ww-tweeter-db-1  | The files belonging to this database system will be owned by user "postgres".
    ww-tweeter-db-1  | This user must also own the server process.
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | The database cluster will be initialized with locale "en_US.utf8".
    ww-tweeter-db-1  | The default database encoding has accordingly been set to "UTF8".
    ww-tweeter-db-1  | The default text search configuration will be set to "english".
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | Data page checksums are disabled.
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
    ww-tweeter-db-1  | creating subdirectories ... ok
    ww-tweeter-db-1  | selecting dynamic shared memory implementation ... posix
    ww-tweeter-db-1  | selecting default max_connections ... 100
    ww-tweeter-db-1  | selecting default shared_buffers ... 128MB
    ww-tweeter-db-1  | selecting default time zone ... Etc/UTC
    ww-tweeter-db-1  | creating configuration files ... ok
    ww-tweeter-db-1  | running bootstrap script ... ok
    ww-tweeter-db-1  | performing post-bootstrap initialization ... ok
    ww-tweeter-db-1  | syncing data to disk ... ok
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | Success. You can now start the database server using:
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  |     pg_ctl -D /var/lib/postgresql/data -l logfile start
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | initdb: warning: enabling "trust" authentication for local connections
    ww-tweeter-db-1  | You can change this by editing pg_hba.conf or using the option -A, or
    ww-tweeter-db-1  | --auth-local and --auth-host, the next time you run initdb.
    ww-tweeter-db-1  | waiting for server to start....2022-01-27 04:12:52.961 UTC [49] LOG:  starting PostgreSQL 14.1 (Debian 14.1-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
    ww-tweeter-db-1  | 2022-01-27 04:12:52.964 UTC [49] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
    ww-tweeter-db-1  | 2022-01-27 04:12:52.970 UTC [50] LOG:  database system was shut down at 2022-01-27 04:12:52 UTC
    ww-tweeter-db-1  | 2022-01-27 04:12:52.975 UTC [49] LOG:  database system is ready to accept connections
    ww-tweeter-db-1  |  done
    ww-tweeter-db-1  | server started
    ww-tweeter-db-1  | CREATE DATABASE
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | waiting for server to shut down....2022-01-27 04:12:53.239 UTC [49] LOG:  received fast shutdown request
    ww-tweeter-db-1  | 2022-01-27 04:12:53.241 UTC [49] LOG:  aborting any active transactions
    ww-tweeter-db-1  | 2022-01-27 04:12:53.243 UTC [49] LOG:  background worker "logical replication launcher" (PID 56) exited with exit code 1
    ww-tweeter-db-1  | 2022-01-27 04:12:53.244 UTC [51] LOG:  shutting down
    ww-tweeter-db-1  | 2022-01-27 04:12:53.257 UTC [49] LOG:  database system is shut down
    ww-tweeter-db-1  |  done
    ww-tweeter-db-1  | server stopped
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | PostgreSQL init process complete; ready for start up.
    ww-tweeter-db-1  | 
    ww-tweeter-db-1  | 2022-01-27 04:12:53.365 UTC [1] LOG:  starting PostgreSQL 14.1 (Debian 14.1-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
    ww-tweeter-db-1  | 2022-01-27 04:12:53.365 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
    ww-tweeter-db-1  | 2022-01-27 04:12:53.365 UTC [1] LOG:  listening on IPv6 address "::", port 5432
    ww-tweeter-db-1  | 2022-01-27 04:12:53.369 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
    ww-tweeter-db-1  | 2022-01-27 04:12:53.374 UTC [63] LOG:  database system was shut down at 2022-01-27 04:12:53 UTC
    ww-tweeter-db-1  | 2022-01-27 04:12:53.381 UTC [1] LOG:  database system is ready to accept connections
    ww-tweeter-db-1  | 2022-01-27 04:13:15.075 UTC [86] LOG:  invalid length of startup packet
    ww-tweeter-db-1  | 2022-01-27 04:13:15.085 UTC [87] LOG:  invalid length of startup packet
    ww-tweeter-db-1  | 2022-01-27 04:13:16.118 UTC [88] LOG:  invalid length of startup packet
    ww-tweeter-db-1  | 2022-01-27 04:13:16.127 UTC [89] LOG:  invalid length of startup packet
    ```

---

## :notebook: 1/27/22

- Solved PostgreSQL connectivity issue...a web browser cannot connect to the database (TCP 5432).
- Added a **pgAdmin** container to the [docker-compose.yml](https://github.com/timothyhull/ww_tweeter/blob/main/docker-compose.yml) file that listens on HTTP 8080.
    - Successfully connected from pgAdmin to the PostgreSQL database although a dedicated Docker network with automatic DNS is a better strategy than manually looking up an IP address.
- Optimization of the Docker Compose implementation is necessary to limit the number of files and folders required to support the application (`_dockerfiles`, `.env`, `.dockerignore`, etc.)

---

## :notebook: 1/28/22

- Modifed PGSQL startup script to support database structure in the RealPython article.
    - One new DB creates, but not the other.
    - Requires further troubleshooting.
- Optimize Docker Compose implementation.
    - Established Docker network which seems to work, and support auto-DNS.
    - Requires further testing.

---

## :notebook: 1/29/22

- Modified the [docker-compose.yml](https://github.com/timothyhull/ww_tweeter/blob/main/docker-compose.yml) file to mount a local volume named `db` in the `db` container.
    - Manually created two databases in the `db` container:

        ```sql
        create database ww_tweeter;
        create database ww_tweeter_test;
        ```

- Updated environment variables in `.env` files with database credentials and a URL.

- Migrated the main/development [Dockerfile](https://github.com/timothyhull/ww_tweeter/blob/main/Dockerfile) to [Dockerfile.dev](https://github.com/timothyhull/ww_tweeter/blob/main/Dockerfile.dev) and repurposed the original [Dockerfile](https://github.com/timothyhull/ww_tweeter/blob/main/Dockerfile) to use within the [docker-compose.yml](https://github.com/timothyhull/ww_tweeter/blob/main/docker-compose.yml) file.
    - Modified the `CMD` instruction to read `CMD ["tail", "-f", "/dev/null"]` in order to establish a long-running process that keeps the container alive.

- Docker Compose now brings up the `db`, `db_admin`, and `app` containers.

---

## :notebook: 1/30/22

- Moved temporary Python files to the [_gitignore](https://github.com/timothyhull/ww_tweeter/blob/main/_gitignore) directory:
    - [_gitignore/ww_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/_gitignore/ww_tweeter.py)
    - [_gitignore_/test_ww_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/_gitignore/test_ww_tweeter.py)

- Created [pytest.ini](https://github.com/timothyhull/ww_tweeter/blob/main/pytest.ini) configuration file to add options that ignore `pytest` tests in the [_gitignore](https://github.com/timothyhull/ww_tweeter/blob/main/_gitignore), and disable `pytest` warnings.
    - The `tweepy` package raises the following `pytest` warning:

        ```bash
        DeprecationWarning: OAuthHandler is deprecated; use OAuth1UserHandler instead.
        ```

- Started review of database code in the [PyBites example repository](https://github.com/pybites/pytip).
- Added `SQLAlchemy` to the [requirements/requirements.txt](https://github.com/timothyhull/ww_tweeter/blob/main/requirements/requirements.txt) file.

---

## :notebook: 2/1/22

- Updated environment variables `DB_URL` and `DB_TEST_URL` to reflect the correct URL and database names.
- Reviewed [`SQLAlchemy` documentation](https://docs.sqlalchemy.org/en/14/), spefically the [Mapper Configuration](https://docs.sqlalchemy.org/en/14/orm/mapper_config.html).
    - The documentation is more advanced than my skill level with `SQLAlchemy`, so I started reviewing the [Object Relational Tutorial (1.x API)](https://docs.sqlalchemy.org/en/14/orm/tutorial.html).
    - Performed troubleshooting on connection attempts to the PostgreSQL database:

        1. Exception - `NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres`

            ```python
            from os import getenv
            from sqlalchemy import create_engine

            DB_TEST_URL = getenv('DB_TEST_URL')
            engine = create_engine(DB_TEST_URL, echo=True)

            # Exception thrown
            NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres
            ```

            - The problem was the format of the database URL:
            - The URL protocol handler was `postgres://` and `SQLAlchemy` requires that the URL protocol handler be `postgresql://`.

        2. Exception - `ModuleNotFoundError: No module named 'psycopg2'`

            ```python
            from os import getenv
            from sqlalchemy import create_engine

            DB_TEST_URL = getenv('DB_TEST_URL')
            engine = create_engine(DB_TEST_URL, echo=True)

            # Exception thrown
            ModuleNotFoundError: No module named 'psycopg2'
            ```

            - The problem was due to a missing Python package, `psycopg2-binary`.
            - Installed the missing package with `pip install psycopg2-binary` and database connections are now successful.
            - Added `psycopg2-binary` to the [requirements/requirements.txt](https://github.com/timothyhull/ww_tweeter/blob/main/requirements/requirements.txt) file.

    - The tutorial is somewhat lengthy and requires more time to review thoroughly.

---

## :notebook: 2/2/22

- Created the [app/\_\_dev\_\_](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__) folder for SQLAlchemy tutorial code.
    - Created [sqlalchemy_tutorial.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/sqlalchemy_tutorial.py)
    - It will be helpful to create a volume mount to the Docker Compose application, so code changes locally are available in the Docker Compose container without performing a rebuild.

---

## :notebook: 2/3/22

- Created dedicated Docker Compose development environment, to support code changes from the VS Code development container, via volume mounts, without having to tear down and rebuild the Docker containers.
- Created [docker-compose-dev.yml](https://github.com/timothyhull/ww_tweeter/blob/main/docker-compose-dev.yml) for the development environment with the following:

    - Volume mounts for:

        1. [./app](https://github.com/timothyhull/ww_tweeter/blob/main/app/)
        2. [./tests](https://github.com/timothyhull/ww_tweeter/blob/main/tests/)
        3. [./pytest.ini](https://github.com/timothyhull/ww_tweeter/blob/main/app/pytest.ini)

    - Container, network, volume, and alias names that end in `_dev`.
    - `command:` paramater, to overwrite the `CMD` instruction in [Dockerfile.dev](https://github.com/timothyhull/ww_tweeter/blob/main/Dockerfile.dev) with a long-running process (`["tail", "-f", "/dev/null"]`).

Updated [Dockerfile.dev](https://github.com/timothyhull/ww_tweeter/blob/main/Dockerfile.dev) to remove the [./requirements](https://github.com/timothyhull/ww_tweeter/blob/main/requirements/) folder after `pip` installations completes.

---

## :notebook: 2/4/22

- Create database named `ww_tweeter_test` in the `db_dev` container.

    ```sql
    create database ww_tweeter_test;
    ```

- Worked through sections in the [Object Relational Tutorial (1.x API)](https://docs.sqlalchemy.org/en/14/orm/tutorial.html):
    - Updated [sqlalchemy_tutorial.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/sqlalchemy_tutorial.py):
        - Created the `User` class to define a **users** table mapping.
        - Created the `create_db_engine` function to create an `sqlalchemy.engine.Engine`.
        - Created the `get_user_schema`function to display a copy of the **users** table schema.

---

## :notebook: 2/5/22

- Updated [sqlalchemy_tutorial.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/sqlalchemy_tutorial.py):
    - Added the `repr` function to display the contents of the `get_user_schema` function.
        - Eliminates the need to use the `._schema_item_copy` attribute of `User.__table__` to display the schema.
    - Added display of user attributes to the `main` function, by creating an instance of a `User` class via a call of the `get_user_schema` function.

---

## :notebook: 2/6/22

- Updated [sqlalchemy_tutorial.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/sqlalchemy_tutorial.py):
    - Added the `config_session_db_engine` function, to create a class instance from the `sqlalchemy.orm.Session` class.
        - Added display of `sqlalchemy.orm.Session` instance to the `main` function, by updating the `Session` class, with the previously created `engine` instance, via a call of the `config_session_db_engine` function.
    - Added the `add_db_session_user_object` function, to add `User` objects to the instance of the `sqlalchemy.orm.Session` class.
        - Returned multiple exceptions, with one recommend disabling automatic transaction flushing:
        - Disabled automation transaction flushing seems to correct the problem:

            ```python
            Session = sessionmaker(
                autoflush=False
            )
            ```

        - Returned an error indicating the `users` table does not exist; perhaps because the table does not yet exist in the database itself:

            ```bash
            psycopg2.errors.UndefinedTable: relation "users" does not exist
            LINE 2: FROM users 
            ```

- Corrected docstrings.

---

## :notebook: 2/7/22

- Troubleshot the `psycopg2.errors.UndefinedTable: relation "users" does not exist` error.
    - Determined that the `users` table is not automatically created, and requires the following command to call `create_all` method of the `declarative_base()` object.

        ```python
        BASE.metadata.create_all(engine)
        ```

    - The `declarative_base().metadata.create_all(engine)` call created tables for any class objects with the `declarative_base` object passed as an argument directly to the class:

        ```python
        # Example (truncated)
        class User(BASE):
        ```

    - Created the `create_db_tables()` function to call create database tables.

---

## :notebook: 2/8/22

- Converted the value of the `autoflush=False` argument in `Session = sessionmaker(autoflush=)` to a constant named `AUTO_FLUSH.`
    - The default value of the `autoflush` parameter is `True`.
    - When set to `False`, the database tables are not automatically created.
- Conducted testing with the `session.query(User)` method, and struggled to produce accurate and consistent results.
    - The tutorial is written for **SQLite** which may have some differences from **PostgreSQL**.
    - Further testing is necessary.

---

## :notebook: 2/9/22

- Reviewed [sqlalchemy_tutorial.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/sqlalchemy_tutorial.py) to address issues from the previous day:
    - Found an error in the code at line 55.

        ```python
        # The nickname field in the __repr__ method was set to `self.fullname`
        # Corrected to read `self.nickname`
        f'nickname={self.nickname})>'
        ```

    - Correcting this line allows the the application to behave exactly the tutorial describes, when working interactively.
    - Repeated runs of the application as a script does not work as expected, after the first run.
    - Requires interactive testing to troubleshoot.

- Created the `commit_db_session` function, to separate the `session.commit` method call from the `add_db_session_user_object` function.
- Removed the `session.dirty` function call in the `add_db_session_user_object` function, because it did not serve a purpose
- Tested database queries using the [SQLAlchemy Queries documentation](https://docs.sqlalchemy.org/en/14/orm/tutorial.html#querying)

---

## :notebook: 2/10/22

- The SQLAlchemy documentation indicates the `User` objected added to the `session` object, via `session.add(User)` should have the same Python identity as the result returned from a `session.query` call.
    - This appears to work properly once, and then the identities do not match afterword.
    - This does not seem to impact DB operations.
- Completed relevant SQLAlchemy tutorial steps, and ready to test writing and reading Twitter data from the PostgreSQL database.

---

## :notebook: 2/11/22

- Updated the [docker-compose-dev.yml](https://github.com/timothyhull/ww_tweeter/blob/main/docker-compose-dev.yml) and [docker-compose.yml](https://github.com/timothyhull/ww_tweeter/blob/main/docker-compose.yml) files to persist **pgadmin** configuration and connection information between container instances.
    - Initially attempted to mount persistent storage with a Docker volume, but the web **pgadmin** web service would not start properly.
    - Required the following mappings:

        ```yaml
        # docker-compose-dev.yml
        volumes:
          - ./_dockerfiles/db_admin_dev/pg_admin:/var/lib/pgadmin
          - ./_dockerfiles/db_admin_dev/pg_admin:/pgadmin4/servers.json

        # docker-compose.yml
        volumes:
          - ./_dockerfiles/db_admin/pg_admin:/var/lib/pgadmin
          - ./_dockerfiles/db_admin/pg_admin:/pgadmin4/servers.json
        ```

---

## :notebook: 2/12/22

- Created [tests/test_db_models.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db_models.py) to for `pytest` tests of [app/db/db_models.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db_models.py).
    - Created [app/db/db_models.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db_models.py) to create models for database tables (`hashtag` and `tweets`).
    - Based class construction on the [PyTip repo `models.py`](https://github.com/pybites/pytip/blob/master/tips/models.py) and the SQLAlchemy tutorial file [app/\_\_dev\_\_/sqlalchemy_tutorial.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/sqlalchemy_tutorial.py).

---

## :notebook: 2/13/22

- Initiated application with initial build of containers using `docker compose up -d --build`.
    - Configured database connectivity and dark theme in the **pgadmin** container.
    - Initialized `wwt_tweeter` and `ww_tweeter_pytest` databases with the following commands in the **db** container:

    ```bash
    # Connect to db container
    docker exec -it <container_name> /bin/bash

    # Run psql binary before creating databses
    psql
    ```

    ```sql
    create database wwt_tweeter;
    create database wwt_tweeter_pytest;
    ```

- Created database interaction framework in [app/db/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py)
- Created database interaction test framework in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py)

---

## :notebook: 2/14/22

- Add code to the `_create_session` function in [app/db/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py).
    - Requires further testing.
    - Requires `pytest` test.

---

## :notebook: 2/15/22

- Tuned [Dockerfile](https://github.com/timothyhull/ww_tweeter/blob/main/Dockerfile) to support development and testing.
- Added code to the `test_create_session` tests in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    - Test is successful without mocking the test `sqlalchemy.orm.Session` object.
    - Mocking the `sqlalchemy.orm.Session` object requires further testing and troubleshooting.

---

## :notebook: 2/16/22

- Created [class_method_attribute_testing.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/class_method_attribute_testing.py) to conduct testing of class method attribute methods.

- Added code to the `test_create_session` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    - Mocking the `sqlalchemy.orm.Session` object requires further testing and troubleshooting.

---

## :notebook: 2/17/22

- Added code to the `test_create_session` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    - Successfully mocked the `sqlalchemy.orm.Session` object using a class method attribute that calls its own method:
        - `class.method().attribute.method()`

---

## :notebook: 2/18/22

- Added code to the `truncate_tables` function in [app/db/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py).
    - Function removes all entries from the `TweetData` and `Hashtag` tables.
    - Need to create a `pytest` test that mocks the `session.query().delete()` method.

---

## :notebook: 2/19/22

- Created [class_method_method_testing.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/class_method_attribute_testing.py) to conduct testing of class method methods.

- Added code to the `test_truncate_tables` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    - Partially mocked the `sqlalchemy.orm.Session` and `sqlalchemy.orm.Query` objects.
    - Requires further testing and troubleshooting.

---

## :notebook: 2/20/22

- Continued testing of `test_truncate_tables` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    - Consolidated mock two separate `sqlalchemy.orm.Session` objects by moving the `get_bind` method to the `SessionMock` class.
    - Unable to successfully mock an `sqlalchemy.orm.Session` object.
    - Requires further testing and troubleshooting.

---

## :notebook: 2/21/22

- Completed testing of `test_truncate_tables` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    - Removed multiple `patch.object` decorators, only using a single `patch.object` decorator to mock a `sqlalchemy.orm.Session` object.
    - Added an optional `session` parameter to the `truncate_tables` function in [app/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py), to allow passing a mock `sqlalchemy.orm.Session` object.
    - `pytest` tests successfully pass.

---

## :notebook: 2/22/22

- Added code to the `get_hashtags` function in [app/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py), to retrieve and sort all hashtags from the `hashtags` table.
    - Manually inserted mock hashtag data into the database for testing, and removed data with the `truncate_tables` function.
    - Need to develop a `pytest` test for the `get_hashtags` function.

---

## :notebook: 2/23/22

- Added code to the `test_get_hashtags` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    - Tested mocking the results of a call to an `sqlalchemy.orm.Query.order_by.all` object method.
    - Requires further testing and troubleshooting, and may require a refactor of the existing `QueryMock` class to support more than the single method (`delete`) used in the `test_truncate_tables` method.

---

## :notebook: 2/24/22

- Created [class_inheritance_testing.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/class_inheritance_testing.py) to conduct testing of class inheritance with attribute methods.

- Updated mock class framework in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py) to support proper function of the `test_get_hashtags` function.
    - `pytest` tests successfully pass.

---

## :notebook: 2/25/22

- Created the `commit_session` function in [app/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py), to refactor session commits into a dedicated function, and avoid writing repetitious code.

- Created the `test_commit_session` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    - All `pytest` tests pass.

---

## :notebook: 2/26/22

- Created the `add_hashtags` function in [app/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py), to add new hashtags to the database.
    - Successfully added hashtags to the database using mock dictionary data in an interactive shell:

        ```python
        # Mock hashtag data
        NEW_HASHTAGS = {
            'hashtag_1': 10,
            'hashtag_2': 20,
            'hashtag_3': 30,
        }

        # Add new hashtags
        add_hashtags(NEW_HASHTAGS)

        # Get hashtags
        hashtags = get_hashtags()
        print(hashtags)
        ''' [<Hashtag(name=hashtag_1, count=10)>,
        <Hashtag(name=hashtag_2, count=20)>,
        <Hashtag(name=hashtag_3, count=30)>] '''

        # Remove hashtags
        truncate_tables()
        ```

- Created the `test_add_hashtags` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    - Added the `add` method to the `SessionMock` class, to support mock calls to the `sqlalchemy.orm.Session.add` method.
        - `add` method adds a mock transaction to the `self.transactions` list for each object (database table row) added.
    - All `pytest` tests pass.

---

## :notebook: 2/27/22

- Refactored tests in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py) to use a `pytest` fixture to create a mock `sqlalchemy.orm.Session` object, using the `SessionMock` class.

- Created the `test_get_tweets` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).

- Created the `get_tweets` function in [app/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py), to support collecting tweet data from the database.
    - `pytest` tests require further testing.

---

## :notebook: 2/28/22

- Removed the `OrderByMock` class in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).
    The `order_by` method in the `OrderMock` class should return an `OrderMock` class object.
- Added the `filter` method to mock calls to the `sqlalchemy.orm.Query.filter` method.
- Updated the `repr_string` in the `TweetData` class in [app/db/db_models.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db_models.py), so that it prints all fields in a tweet.

---

## :notebook: 3/1/22

- Created the `test_add_tweets` test in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).

- Created the `add_tweets` function in [app/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py), to support adding tweet data to the database.
    - `add_tweets` requires additional code to function properly.

---

## :notebook: 3/2/22

- The `isinstance` method compares an object to an object class and, via two arguments, and returns `True` or `False` depending on whether or not the object is an instance of the object class.
    - Useful for determining if an object is of a certain type, without using a `type` method:

        ```python
        # Use isinstance to determine if an object is an instance of a class
        my_dict = {'a': 1}

        isinstance(
            my_dict,  # object instance
            dict,     # object class
        )
        ''' Returns True '''

        # This is an alternative to the type method
        type(my_dict) == dict
        ''' Returns True '''
        ```

    - `isinstance` supports inline conditional logic:

        ```python
        my_dict = {'a': 1}

        # Set or reset the value of my_dict based on the object type
        my_dict = my_dict if isinstance(my_dict, list) else my_dict.items()
        ''' Returns dict_items([('a', 1)]) '''
        ```

- Completed and tested the `add_tweets` function in [app/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py)
    - All `pytest` tests pass.

---

## :notebook: 3/3/22

- Reviewed [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter/tweeter.py) to recall how it works.
- Reviewed the [pybites twitter repository example](https://github.com/pybites/pytip/blob/master/tasks/import_tweets.py) to understand its operation.
    - Successfully tested importing tweets into the database using an interactive Python shell:

        ```bash
        # Run tweeter.py in an interactive shell
        ipython -i app/tweeter/tweeter.py
        ```

        ```python
        # Import db.py in the 'db' namespace to avoid naming conflicts
        from app.db import db

        # Create Twitter authentication object
        auth = twitter_api_auth()

        # Get tweets from Twitter
        tweets = get_tweets(api_object=auth)

        # Add tweets to the database
        db.add_tweets(tweets=list(tweets))

        # Get tweets from the database
        db_tweets = db.get_tweets()

        # Remove tweets from the database
        db.truncate_tables()
        ```

    - Importing hashtags into the database requires further analysis of the pybites repository example.

---

## :notebook: 3/4/22

- Renamed the `get_tweets` function in [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter/tweeter.py) to avoid namespace conflict with `get_tweets` in [app/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py).
    - New function name is `get_top_n_tweets`.
    - Updated function name in [tests/test_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_tweeter.py) to `test_get_top_n_tweets`.

- Imported the `add_tweets` and `truncate_tables` functions from [app/db.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db.py) into [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter/tweeter.py).
    - Added both functions to the `main` function, and tweets are now read from Twitter and imported into the database (after the tables are cleared).

- Created [counter_testing.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/__dev__/counter_testing.py) to determine the purpose use of the [pybites `get_hashtag_counter` function](https://github.com/pybites/pytip/blob/master/tasks/import_tweets.py#L38).
    - Need to review the `Counter` object and the `VALID_HASHTAG` regular expression syntax.

---

## :notebook: 3/5/22

- Created the `test_hashtag_counter` test function in [tests/test_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_tweeter.py).
    - Mock class objects require modification to support the `hashtag_counter` function.

- Created the `hashtag_counter` function in [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter/tweeter.py), to support counting hashtags from the tweet text

---

## :notebook: 3/7/22

- Updated the `test_hashtag_counter` test function in [tests/test_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_tweeter.py) to function properly.
    - Wrapped `TWEET_MOCK` in a list, to make the object iterable and allow capture of tweet data by the `hashtag_counter` function.
    - All `pytest` tests pass.

- Created the `test_import_hashtags` test function in [tests/test_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_tweeter.py).
    - Created initial framework only, further development and testing required.

- Created the `import_hashtags` function in [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter.py), to support importing hashtags and counts into the database.
    - Added the to the `main` function, and hashtags with counts, extracted from actual tweets, are now imported into the database (after the tables are cleared).
    - Required extending the length of the `hashtags` table `name` field from 20 to 40 characters in [app/db/db_models.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/db/db_models.py):

        ```python
        class Hashtag(BASE):
            """ Create table for hashtags and hitcounts.

                Args:
                    BASE (sqlalchemy.ext.declarative.declarative_base)
            """

            # Assign table name
            __tablename__ = 'hashtags'

            # Assign table columns
            id = Column(
                type_=Integer,
                primary_key=True
            )
            name = Column(String(40))
            count = Column(Integer)

            ''' Truncated for brevity. '''
        ```

---

## :notebook: 3/8/22

- Removed the `test_import_hashtags` test function in [tests/test_tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_tweeter.py).
    - Testing already takes place in [tests/test_db.py](https://github.com/timothyhull/ww_tweeter/blob/main/tests/test_db.py).

- Removed the `import_hashtags` functions from [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter.py).
    - Added direct call to `add_hashtags` from the `main` function.

- Updated `import` statement in [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter.py) from `from app.db.db import (function_1, function_2, etc.)` to `from app.db import db`.
    - This ensures the `db._create_session` function always runs, which creates database tables if they do not exist.
    - Without this function running, an exception would return if the database tables did not exist.

- Refactored [app/tweeter/tweeter.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/tweeter.py) such that the `TWEET_SLICE` constant can accept a value of `None` and return all tweets.
    - Updated the `TWEET_SLICE` constant default to a value of 500.

---

## :notebook: 3/9/22

- Started development process to use `bottle` as a web/view service in the app.
    - Added `bottle` to the [requirements/requirements.txt](https://github.com/timothyhull/ww_tweeter/blob/main/requirements/requirements.txt) and [requirements/requirements_pytest.txt](https://github.com/timothyhull/ww_tweeter/blob/main/requirements/requirements_pytest.txt) files.
    - Started review of [bottle documentation](http://bottlepy.org/docs/dev/).
    - Started review of database code in the [PyBites example repository](https://github.com/pybites/pytip).

- Created web application framework:
    - Created the following files:
        - [_dockerfiles/web/\_\_dev\_\_/bottle_testing.py](https://github.com/timothyhull/ww_tweeter/blob/main/_dockerfiles/web/__dev__/bottle_testing.py) - to support `bottle` tutorial walk-through.
        - [app/web/web.py](https://github.com/timothyhull/ww_tweeter/blob/main/app/web/web.py) - to support final web application.
        - [_dockerfiles/web/requirements.txt](https://github.com/timothyhull/ww_tweeter/blob/main/_dockerfiles/web/requirements.txt) - to support Python package installation.
        - [_dockerfiles/web/Dockerfile](https://github.com/timothyhull/ww_tweeter/blob/main/_dockerfiles/web/Dockerfile) - to support web app container image.
    - Updated the following files with instructions for the `web` container:
        - [docker-compose.yml](https://github.com/timothyhull/ww_tweeter/blob/main/docker-compose.yml)
        - [docker-compose-dev.yml](https://github.com/timothyhull/ww_tweeter/blob/main/docker-compose-dev.yml)
    - **web** container starts and exits immediately, and requires further troubleshooting.
