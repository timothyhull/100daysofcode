# :calendar: Day 62: 3/26/2022-4/10/2022

---

## Topics

:clipboard: Using the Github API with Python

---

## Resources

:star: [Project suggestions ("Second + third day: practice!" section)](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/61-63-github-api/github-api.ipynb)

:star: [GitHub Profiler](https://github.com/clamytoe/Github-Profiler) example application

---

## Tasks

:white_check_mark: Watch video 7

:white_check_mark: Select project to build (GitHub Profiler)

:white_large_square: Create application design framework outline

:white_large_square: Create GitHub repository for the application

:white_large_square: Build development and runtime container environments

:white_large_square: Write application

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
