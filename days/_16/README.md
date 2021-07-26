## :calendar: Day 16: 7/22/2021-7/25/2021

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

#### :notebook: 7/25/21

- Produced a sequence using both a `list` and a generator, to consider that the generator may take less code to produce.

`list` method:

```python
# Create a list of options
options = 'red orange yellow green blue purple white black'.split()
print(options)
```

```python
# Create a list of HTML <option> tags using the defined options
def create_select_options(options=options):
    # Blank list for option tags
    select_list = []

    # Populate option tag list
    for option in options:
        select_list.append(
            f'<option value={option}>{option.title()}</option>'
        )

    return select_list

from pprint import pprint
pprint(create_select_options())
```

Generator method:
```python
# Create a list of HTML <option> tags using the defined options
def create_select_options_generator(options=options):
    for option in options:
        yield(f'<option value={option}>{option.title()}</option>')

list(create_select_options_generator())
```
