# :calendar: Day 59+60: 1/16/2022-1/25/2022

---

## Topics

:clipboard: Twitter Data Analysis With Python

---

## Resources

:star: [RealPython article: Building a web app with Bottle, SQLAlchemy, and the Twitter API](https://realpython.com/building-a-simple-web-app-with-bottle-sqlalchemy-twitter-api/)

:star: [PyBites article: Parsing Twitter Geo Data and Mocking API Calls by Example](https://pybit.es/articles/twitter-api-geodata-mocking/)

---

## Tasks

:white_check_mark: Watch video 9

:white_check_mark: Choose a project from the options in the last cell of [this notebook](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/58-60-twitter-api/twitter-api.ipynb)

:white_check_mark: Define application design/goals

:white_check_mark: Setup Git repository

:white_check_mark: Connect Git repository to Better Code Hub

:white_check_mark: Setup application framework (devcontainer, README, file structure)

:white_check_mark: Setup webhook to automatically perform bettercodehub.com analysis on push and PR events

:white_large_square: Setup CI/CD pipelines for `yamllint`, `flake8`, and `bandit` checks

:white_large_square: Add Better Code Hub and CI/CD build status to README

:white_large_square: Write application

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

    1. [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json) - Development container configuration.
    2. [.github.workflows/linting.yaml](.github.workflows/linting.yaml) - GitHub action configuration for file linting and static code analysis.
    3. [requirements/requirements.txt](requirements/requirements.txt) - Python packages.
    4. [.bettercodehub.yml](.bettercodehub.yml) - bettercodehub.com configuration file.
    5. [.markdownlint.json](.markdownlint.json) - `markdownlint` rule exclusions.
    6. [Dockerfile](Dockerfile) - Development container Dockerfile.
    7. [LICENSE](LICENSE) - Apache 2.0 license.
