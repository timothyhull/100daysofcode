## :calendar: Day 22: 8/13/2021-8/15/2021

---

## Topics:

:clipboard: Decorators

---

## Resources:

:star: [Hitchhiker's Guide to Python Function Arguments](https://docs.python-guide.org/writing/style/#function-arguments)

:star: [`functools.wraps`](https://docs.python.org/3/library/functools.html#functools.wraps)

:star: [PyBites Decorators Article](https://pybit.es/decorators-by-example.html)

---

## Tasks:

:white_check_mark: Watch videos 1-2

:white_check_mark: Review concepts from 8/13/21

:white_check_mark: Watch video 3

:white_check_mark: Watch video 4

:white_large_square: TBD

---

## Notes:

#### 8/13/21 :notebook:

- Created [Jupyter Notebook for decorators lessons](decorators.ipynb).
- Worked with decorator functions.
- Worked with the `*args` and `**kwargs` function arguments.

---

#### 8/14/21 :notebook:

- Reviewed decorator function creation.
- Created a decorator function to time a decorated function.
- Tested the functionality of the `@wraps` decorator within a decorator function definition to determine its purpose.
    - Without `@wraps`, the docstring **is not** available for the decorated function, using the `help()` function.
    - With `@wraps`, the docstring **is** available for the decorated function, using the `help()` function.

---

#### 8/15/21 :notebook:

- Worked with nested decorator functions in the [Jupyter Notebook](decorators.ipynb).
    - Successfully wrapped a function in two decorators.
- Used `itertools.cycle` to display a wait timer.
