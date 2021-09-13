# :calendar: Day 29: 9/9/2021-9/12/21

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

:white_check_mark: Review 10 Tips Documentation for Tip 6

:white_large_square: Review 10 Tips Documentation for Tip 8

:white_large_square: Review 10 Tips Documentation for Tip 9

:white_large_square: Review 10 Tips Documentation for Tip 10

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

### :notebook: 9/12/21

- The regex syntax `\b` indicates a _word boundary_.
    - The match for a word boundary does not consume any characters (zero length).
    - Will match at the boundaries of word and non-word characters.
    - `\b` enables a "whole word only" functionality with the syntax `\bword\b`.

- `\b` matches:
    - Before the first character in a string, if the first character is a word character (`\w`).
    - After the last character in a string, if the first character is a word character (`\w`).
    - Between two characters in a string, where one is a word character (`\w`) and the other is not a word character (`\W`).

<details><summary><b>Example #1</b></summary>

```python
# Import the regular expression module
import re

# Define a string to search
text = 'This is a thrilling episode to thrash about in the bath through Thursday.'

# Match every instance of 'th' and 'Th' when preceded by a non-word character.
r = re.compile(
    r'''
    \b         # Start a word boundary
    [tT]h      # Literal th or Th
    ''',
    re.VERBOSE
)

# Display a list of matches
r.findall(text)
```

</details>

<details><summary><b>Example #2</b></summary>

```python
# Import the regular expression module
import re

# Define a string to search
text = 'This is a thrilling episode to thrash about in the bath through Thursday.'

# Match every instance of 'th' and 'Th' when followed by a non-word character.
re.search(r'[tT]h\b', text)
```

</details>

- _Backreferences_ are helpful to do things like locating duplicate words:

```python
# Import the regular expression module
import re

# Define a string to search
text = 'This is the song song that never never ends'

''' Match any word that appears immediately after itself.
    Create match group 1 to find every word, then search for group 1
    immediately after the match string.
'''

r = re.compile(
    r'''
    (          # Start match group 1
    \b         # Start a word boundary
    \w+        # Match one or more word characters
    )          # End match group 1
    \s+        # Match one or more space characters
    \1         # Match an instance of match group 1
    ''',
    re.VERBOSE
)

# Display a list of matches
r.findall(text)

```
