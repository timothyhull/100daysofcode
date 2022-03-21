# :calendar: Day 61: 3/18/2022-3/22/2022

---

## Topics

:clipboard: Using the Github API with Python

---

## Resources

:star: [PyGithub](https://pypi.org/project/PyGithub/) on PyPI
:star: [GitPython](https://pypi.org/project/GitPython/) on PyPI
:star: [GitHub API Rate Limiting Documentation](https://docs.github.com/en/rest#rate-limiting)

---

## Tasks

:white_check_mark: Watch videos 1-2

:white_large_square: Watch video 3

:white_large_square: TBD

---

## Notes

### :notebook: 3/18/22

- Watched videos 1-2.
- Created [./github_api.ipynb](./github_api.ipybnb) Jupyter Notebook.
- Setup `PyGithub` user object.

---

### :notebook: 3/19/22

- Watched video 3.
- Updated notes in [./github_api.ipynb](./github_api.ipybnb)

---

### :notebook: 3/20/22

- Refactored [./github_api.ipynb](./github_api.ipybnb) to support switching to any GitHub account with the constants `GITHUB_USER` and `GITHUB_USER_2`, plus the `PyGithub` object `github_user`.
- Watched video 4.
- Wrote the `get_repo_stats` function to collect user repositories and sort by most popular (star count).
    - Unable to successfully run the function due to API rate limiting, will test again tomorrow.
