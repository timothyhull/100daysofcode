# :calendar: Day 49: 12/2/2021

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

:white_large_square: TBD

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
