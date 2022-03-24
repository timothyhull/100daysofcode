# :calendar: Day 61: 3/18/2022-3/23/2022

---

## Topics

:clipboard: Using the Github API with Python

---

## Resources

:star: [PyGithub](https://pypi.org/project/PyGithub/) on PyPI

:star: [GitPython](https://pypi.org/project/GitPython/) on PyPI

:star: [GitHub API Rate Limiting Documentation](https://docs.github.com/en/rest#rate-limiting)

:star: [Python Debugger (`pdb`) Documentation](https://docs.python.org/3.7/library/pdb.html)

:star: [PyBites Article - How to Use `pdb` to Debug Your Code](https://pybit.es/articles/pdb-debugger)

:star: [PEP 553 - Python Built-In `breakpoint` Debugging Function](https://peps.python.org/pep-0553/)

---

## Tasks

:white_check_mark: Watch videos 1-2

:white_check_mark: Watch video 3

:white_check_mark: Watch video 4

:white_check_mark: Watch video 5 and create a GitHub gist

:white_check_mark: Watch video 5

:white_check_mark: Review PyBites `pdb` article

:white_large_square: Review official `pdb` documentation

:white_large_square: Watch video 6

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

---

### :notebook: 3/22/22

- Watched video 6.
- Reviewed functionality of the Python Debugger (`pdb`) module.
    - Part of the Python Standard Library.
    - Pauses code execution, and allows the use of a REPL.
    - Very useful for inspecting objects and debugging, without having to continuously rerun code (with `print` function calls).

        ```python
        # Import the pdb and pprint modules
        from pprint import pprint

        # Create a github.Github user object for a specific user
        github_user = gh.get_user(login='timothyhull')

        # Get a PaginatedList of a user's gists
        gists = github_user.get_gists()

        # Loop over the user's gists
        for gist in gists:
            import pdb; pdb.set_trace()

        ''' While in set_trace mode, enter some commands to inspect objects:

                - pprint(dir(gist))
                - gist.owner
                - !help(gist)  # The ! prefix is required
        '''

        # Use output from commands in set_trace mode to create friendly output for each gist
        for gist in gists:
            print(
                f'GitHub gists for "{github_user.name}":\n'
                f'  Owner: {gist.owner}'
                f'  ID: {gist.id}\n'
                f'  Description: {gist.description}\n'
                f'  Created on: {gist.created_at}\n'
                f'  URL: {gist.url}\n'
            )
        ```

---

### :notebook: 3/23/22

- Researched and tested the Python `breakpoint` function, as a replacement for `import pdb; pdb.set_trace()`.
- Located `pdb`/`breakpoint` documentation by typing `help` during a debug session:

    ```text
    In [1]: breakpoint()
    --Call--
    > /usr/local/lib/python3.9/site-packages/IPython/core/displayhook.py(252)__call__()
    -> def __call__(self, result=None):
    (Pdb) help

    Documented commands (type help <topic>):
    ========================================
    EOF    c          d        h         list      q        rv       undisplay
    a      cl         debug    help      ll        quit     s        unt      
    alias  clear      disable  ignore    longlist  r        source   until    
    args   commands   display  interact  n         restart  step     up       
    b      condition  down     j         next      return   tbreak   w        
    break  cont       enable   jump      p         retval   u        whatis   
    bt     continue   exit     l         pp        run      unalias  where    

    Miscellaneous help topics:
    ==========================
    exec  pdb
    ```
