## :calendar: Day 23: 8/16/2021-8/18/2021

---

## Topics:

:clipboard: Decorators practical challenge

---

## Resources:

:star: [Introduction to Python Decorators](https://www.codementor.io/@sheena/introduction-to-decorators-du107vo5c)

:star: [Advanced Uses of Python Decorators](https://www.codementor.io/@sheena/advanced-use-python-decorators-class-function-du107nxsv)

---

## Tasks:

:white_check_mark: Complete [PyBite 22](https://codechalleng.es/bites/22/)

:white_large_square: Review [Advanced Uses of Python Decorators](https://www.codementor.io/@sheena/advanced-use-python-decorators-class-function-du107nxsv)

:white_large_square: Review and refactor [`pybite_22.py`](pybite_22.py) as needed.

---

## Notes:

#### :notebook: 8/16/21

- Started PyBite 22.
    - Unable to complete the challenge using the materials covered in the video lessons although one of the articles mentioned in the lesson has a reference to an article on [Advanced Uses of Python Decorators](https://www.codementor.io/@sheena/advanced-use-python-decorators-class-function-du107nxsv).
        - I am unable to pass an argument into a decorator successfully.
    - A skim of the article indicates I need to create a function that returns a decorator in order to successfully complete the task.
    - I thought I could complete this challenge in one day although this may be a good opportunity to implement some `pytest` tests, given more time.

---

#### :notebook: 8/16/21

- Wrote `pytest` tests for [`pybite_22.py`](pybite_22.py) in [`test_pybite_22.py`](test_pybite_22.py).
    - The first test uses `pytest.mark.parameterize` to pass values as **arguments** to the function `get_text()`.
    - The second test uses `unittest.mock.patch` to mock **`input()`** function values `get_text()`.
    - Both functions use the same input data compare that to the same expected results data.

- Conducted **decorator testing** using [`decorator_testing.ipynb`](decorator_testing.ipynb).
- Successfuly developed decorator function with argument in [`pybite_22.py`](pybite_22.py) that passes **pybite 22** tests.
    - Need to review and improve understanding.

---

#### :notebook: 8/17/21

- Reviewed [Advanced Uses of Python Decorators](https://www.codementor.io/@sheena/advanced-use-python-decorators-class-function-du107nxsv)

- Conducted further **decorator testing** (_Day 2 of testing_ section) using [`decorator_testing.ipynb`](decorator_testing.ipynb).

Note>General syntax of a Python decorator object **with arguments**:

```python
def outer_decorator(*outer_args,**outer_kwargs):                            
    def decorator(fn):                                            
        def decorated(*args,**kwargs):                            
            do_something(*outer_args,**outer_kwargs)                      
            return fn(*args,**kwargs)                         
        return decorated                                          
    return decorator       


@outer_decorator(1,2,3)
def foo(a,b,c):
    print(a)
    print(b)
    print(c)


foo()
```

Which is equivalent to:

```python
def decorator(fn):                                            
    def decorated(*args,**kwargs):                            
        do_something(1,2,3)                      
        return fn(*args,**kwargs)                         
    return decorated                                          
return decorator       
    
@decorator
def foo(a,b,c):
    print(a)
    print(b)
    print(c)


foo()
```