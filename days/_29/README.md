# :calendar: Day 29: 9/9/2021-9/10/21

---

## Topics

:clipboard: Regular Expressions

---

## Resources

:star: [10 Tips to Get More From Regex](https://pybit.es/articles/mastering-regex/)

:star: [Regex HOWTO (Python Documentation)](https://docs.python.org/3.7/howto/regex.html#regex-howto)

:star: [Regex Operations (Python Documentation)](https://docs.python.org/3.7/library/re.html)

:star: [Regex101.com for Python](https://regex101.com/#python)

---

## Tasks

:white_check_mark: Watch video 9

:white_check_mark: Review 10 Tips to Get More From Regex article

:white_check_mark: Review 10 Tips Documentation for Tip 5

:white_large_square: Review 10 Tips Documentation for Tip 6 snd Tip 10

---

## Notes

### :notebook: 9/9/21

- Regular expression for matching repeating words

```python
# Import the regular expression module
import re

# Define the string to search
s = 'Paris in the the spring'

# Compile a regular expression pattern
p = re.compile(
    r'''
    (       # Open first capturing group
    \b      # Establish a word boundary
    \w+     # One or more occurrence of a word character
    )       # Close first capturing group
    \s+     # One or more occurrence of a word character
    \1      # Capturing group 1
    ''',
    re.VERBOSE
)

# Search for repeating words and display the first match
p.search(s).group()
```

---

### :notebook: 9/10/21

- Reviewed Tip 5 (Greediness) 10 Tips for Python article.

---

### :notebook: 9/11/21

- Tested Tip 5 (Greediness).
    - By default, regex searches are _greedy_, meaning they match as much as possible:

```python
# Define a text string
text = 'This is one group of words. This is another group of words.'

# Import the 're' module and run a search for words followed by a period.
import re
re.search(r'.+\.', text).group()
```

- The previous example returns the entire string, because the default  _greedy_ property of the search matches the longest possible string.

```bash
This is one group of words. This is another group of words.
```

- The match only the first sentence, make the search pattern non-greedy:

```python
# Define a text string
text = 'This is one group of words. This is another group of words.'

# Import the 're' module and run a search for words followed by a period.
import re

# Include the ? character after the .+ or .* to match the shortest possible 
re.search(r'.+?\.', text).group()
```

- The previous example matches the shortest possible string that meets the criteria, which is the first sentence, in the previous example.

```bash
This is one group of words.
```

---

- _Backreferences_ are helpful to do things like locating duplicate words:

```python
```
