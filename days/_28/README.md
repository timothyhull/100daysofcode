# :calendar: Day 28: 9/5/2021-9/8/2021

---

## Topics

:clipboard: Regular Expressions

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Watch videos 1-3

:white_check_mark: Review Jupyter Notebook notes

:white_check_mark: Watch videos 4-5

:white_check_mark: Watch video 6

:white_large_square: Watch video 7-8

---

## Notes

### :notebook: 9/5/21

- Created [Jupyter Notebook](regular_expressions.ipynb) for regular expressions.
    - Worked with `str` methods which are available for basic text search and replace options.
    - Conducted basic testing with the `re` module `search` and `match` methods.

---

### :notebook: 9/6/21

- Reviewed content in the [Jupyter Notebook](regular_expressions.ipynb) from the previous day.
- Updated [Jupyter Notebook](regular_expressions.ipynb).
    - Added notes for **string capturing parenthesis** and `re.findall`.

---

### :notebook: 9/7/21

- Updated [Jupyter Notebook](regular_expressions.ipynb).
    - Added notes for `re.compile` and `re.verbose`.

Non-capturing group note:

- A non-capturing group allows the use of parenthesis to group match criteria without creating a matching group (with a unique matching group number).
    - This is useful if you want to designate a complex search pattern that should repeat several times:

```python
import re

# The non-capturing group allows me to match a word followed by a space character (twice in this case)
search_pattern = re.compile(
    r'''
    (?:         # Non-capturing (
    [a-zA-Z']+  # One or more a-z, A-Z, or literal ' characters
    \s          # Literal space character
    )           # Non-capturing )
    {2}         # Repeat the non-capturing group twice
    ''',
    re.VERBOSE
)
```

---

### :notebook: 9/8/21

- Updated [Jupyter Notebook](regular_expressions.ipynb).
    - Added notes for `re.sub`.

- `re.sub` performs more advanced substring replacement.
    - The parameters are `pattern`, `repl`, and `string`.
    - `pattern` supports raw strings for regular expression **search** operations.
        - Supports using capturing groups, with parenthesis.
    - `repl` also supports raw strings for regular expression matching groups (`\1`).

```python
import re

text = 'My #1 favorite food is pizza, my #2 favorite food is pancakes, and my #3 favorite food is pickled jalapenos.'

re.sub(
    pattern=r'#(\d[\sa-zA-Z]+is\s)[a-zA-Z\s]+([,.])',
    repl=r'#\1chocolate\2',
    string=text
)
```
