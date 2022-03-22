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

:white_check_mark: Watch video 3

:white_check_mark: Watch video 4

:white_check_mark: Watch video 5 and create a GitHub gist

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

---

### :notebook: 3/21/22

- Watched video 5.
- Added notes to [./github_api.ipynb](./github_api.ipybnb).
    - Corrected programmatic error in `get_repo_stats` that was creating a new `github.Github` object with every loop iteration, causing exhaustion of GitHub API rate limits, and also failure to run correctly.
    - Added code to create an authenticated `Github` object, using a [Personal Access Token (PAT)](https://github.com/settings/tokens).

    ```python
    from github import Github, InputFileContent
    gh = Github(login_or_token='github_personal_access_token')

    me = gh.get_user(login='github_user_name')
    ```

    - [Created a new (private) GitHub gist](https://gist.github.com/timothyhull/0211c69591bf62a3046b3e9503dc3660) using the `create_gist` method of the `Github` user object.

    ```python
    # Create code to share, as a string
    gist_code = '''
    Function to generate a list of user repos, sorted by the most number of stars.
    '''

    # Create an input file object from gist_code
    gist_code_input = InputFileContent(
        content=gist_code
    )

    # Create a dictionary with gist_code_input as the value
    gist_file_input = {
        'get_user_repos.py': gist_code_input
    }

    # Create a new gist object
    me.create_gist(
        public=False,
        files=gist_file_input,
        description='Get a user\'s most popular repos'
    )
    ```
