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

:white_large_square: Review 10 Tips Documentation for Tip 5

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
