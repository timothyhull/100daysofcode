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

:white_large_square: TBD

---

## Notes

### :notebook: 12/2/21

- Measuring application performance is refered to as "profiling."
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
