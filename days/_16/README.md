## :calendar: Day 16: 7/22/2021-7/24/2021

---

## Topics:

:clipboard: List comprehensions
:clipboard: Generators

---

## Resources:

:star: [`re.sub()` method](https://docs.python.org/3/library/re.html#re.sub) reference

---

## Tasks:

:white_check_mark: Watch videos 1-2 and create Jupyter Notebook for notes

:white_large_square: Watch video 3 and update Jupyter Notebook notes

:white_large_square: Watch video 4 and update Jupyter Notebook notes

---

## Notes:

#### :notebook: 7/23/21

- The `re.sub()` method returns a matching string with replacements matching the replacement string.
- Completed `list` comprehension section.

---

#### :notebook: 7/24/21

- Started generators section and created a simple generator:

```python
# Create the generator function
def number_generator():
    for i in range(5):
        yield(i)

# Store a generator as a variable
gen = number_generator()

# Yield generator values with the next() function
next(gen)

# Loop through the remaining values in the generator
""" The loop will start with 1 because 0 was already yielded for the 'gen' generator/variable.
    The loop will automatically stop when it yields the last available generator value
"""

for i in gen:
    print(i)
```

---
