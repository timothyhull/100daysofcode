# :calendar: Day 49: 12/2/2021-12/10/2021

---

## Topics

:clipboard: Measuring Performance

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Watch videos 1-3

:white_check_mark: Tested `cProfile` module on `/workspaces/100daysofcode/days/_49/demo/final_csv_code/program.py`

:white_check_mark: Watch videos 4-5

:white_check_mark: Re-watch video 5

:white_check_mark: Watch video 6

:white_check_mark: Refactor `/workspaces/100daysofcode/days/_49/demo/starter_csv_code/program.py` to reduce profiling footprint

:white_check_mark: Watch video 7

:white_check_mark: Refactor `/workspaces/100daysofcode/days/_49/demo/starter_csv_code/research.py` to for performance optimization

:white_check_mark: Watch videos 8-10

:white_check_mark: Watch video 11

:white_check_mark: Select a Python application to optimize with `cProfile`.

---

## Notes

### :notebook: 12/2/21

- Measuring application performance is referred to as "profiling."
- To profile Python applications, use the built-in `cProfile` module at the Linux CLI:

```bash
python -m cProfile script_name.py

### Sample output ###
Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      297    0.822    0.003    1.636    0.006 {built-in method builtins.sorted}
       99    0.002    0.000    0.555    0.006 research.py:53(hot_days)
       99    0.002    0.000    0.546    0.006 research.py:61(wet_days)
       99    0.002    0.000    0.540    0.005 research.py:57(cold_days)
    36135    0.278    0.000    0.278    0.000 research.py:54(<lambda>)
    36135    0.271    0.000    0.271    0.000 research.py:62(<lambda>)
    36135    0.265    0.000    0.265    0.000 research.py:58(<lambda>)
       99    0.010    0.000    0.084    0.001 research.py:14(init)
      365    0.018    0.000    0.037    0.000 research.py:30(parse_row)
      366    0.018    0.000    0.033    0.000 csv.py:107(__next__)
     1460    0.011    0.000    0.011    0.000 {method 'get' of 'dict' objects}
      365    0.005    0.000    0.008    0.000 <string>:1(<lambda>)
```

- Select a sort field with the `-s` option:

```bash
python -m cProfile -s cumtime
```

- `cumtime` is cumulative runtime for a given element.

---

### :notebook: 12/3/21

- To profile a Python application using code, perform the following steps:

   1. Import the Python cProfile module:
      - `import cProfile`
   2. Create a profiler by assigning a `cProfile.Profile` to a variable, and then disable the profile:
      - Immediately disabling the profiler prevents module initialization from being included in the profiling process.

      ```python
      profiler = cProfile.Profile()
      profiler.disable()
      ```

   3. Enable the profiler at a specific point in the application:
      - `profiler.enable()`
   4. Disable the profiler at a specific point, later in the application:
      - `profiler.disable()`
   4. Add Python code to a script, to display profiler statistics in the terminal (Sorted by cumulative time.):
      - `profiler.print_stats(sort='cumtime')`

---

### :notebook: 12/4/21

- Refactored `/workspaces/100daysofcode/days/_49/demo/starter_csv_code/program.py` to reduce profiling footprint:
   - Individual function calls to `research.hot_days`, `research.cold_days`, and `research.wet_days` no longer return results to the same variable name (`days`).
   - Function calls now assign to individual variables named `hot_days`, `cold_days`, and `wet_days`.
   - The refactoring allows profiling to start and stop in a contiguous block of code, removing some processes from the `cProfile` profiling.

   ```python
   import cProfile

   # Initialize a profiler object and disable profiling
   profiler = cProfile.Profile()
   profiler.disable()

   def main():
      print("Weather research for Seattle, 2014-2015")
      print()

      # Enable the profiler
      profiler.enable()

      # Call functions from the research module
      research.init()
      hot_days = research.hot_days()
      cold_days = research.cold_days()
      wet_days = research.wet_days()

      # Disable the profiler
      profiler.disable()

      # program execution continues...
   ```

---

### :notebook: 12/5/21

- Refactored the `parse_row` function in the file [research.py](./demo/starter_csv_code/research.py) to:
   1. Only convert text data to integers if the data is part of the results (min temp, max temp, precipitation).
   2. Only insert the relevant data into the `Results` namedtuple object, instead of a data set with many unused fields.
- Refactored the `__init__` function in the file [research.py](./demo/starter_csv_code/research.py) to:
   1. Only read the CSV data from a file and convert it to a Python dictionary one time:

   ```python
   def init():
      # If the data list (global var) is not empty, do not re-read the CSV file
      if data:
         return None
      # Reamining function code truncated
   ```

- Application performance snapshot _before_ refactoring:

```bash
 114912 function calls in 1.949 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       24    0.217    0.009    1.552    0.065 research.py:17(init)
     8784    0.427    0.000    0.785    0.000 csv.py:107(__next__)
     8760    0.212    0.000    0.412    0.000 research.py:30(parse_row)
       72    0.200    0.003    0.396    0.005 {built-in method builtins.sorted}
     8760    0.131    0.000    0.201    0.000 <string>:1(<lambda>)
    17544    0.141    0.000    0.143    0.000 csv.py:93(fieldnames)
       24    0.000    0.000    0.137    0.006 research.py:51(hot_days)
       24    0.000    0.000    0.132    0.006 research.py:59(wet_days)
    17544    0.127    0.000    0.127    0.000 {built-in method builtins.len}
       24    0.000    0.000    0.127    0.005 research.py:55(cold_days)
```

- Application performance snapshot _after_ refactoring:

```bash
 31617 function calls in 0.483 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       72    0.196    0.003    0.392    0.005 {built-in method builtins.sorted}
       24    0.000    0.000    0.137    0.006 research.py:46(hot_days)
       24    0.000    0.000    0.128    0.005 research.py:54(wet_days)
       24    0.000    0.000    0.127    0.005 research.py:50(cold_days)
       24    0.009    0.000    0.090    0.004 research.py:14(init)
     8760    0.069    0.000    0.069    0.000 research.py:47(<lambda>)
     8760    0.064    0.000    0.064    0.000 research.py:55(<lambda>)
     8760    0.062    0.000    0.062    0.000 research.py:51(<lambda>)
      365    0.020    0.000    0.040    0.000 research.py:31(parse_row)
      366    0.019    0.000    0.035    0.000 csv.py:107(__next__)
```

---

### :notebook: 12/6/21

- Watched videos 8-10.

---

### :notebook: 12/10/21

- Selected a Python application to optimize with `cProfile`.
   - `movie_search` application, from Day 43.
