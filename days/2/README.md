## :calendar: Day 2: 4/19/2020 - 4/21/2020

---

## Topics:

:clipboard: `datetime` objects

---

## Resources:

:star: [PyBite 7](https://codechalleng.es/bites/7/): Parsing dates from logs

:star: [PyBite 67](https://codechalleng.es/bites/67/): Working with datetimes

:star: [PyBite 128](https://codechalleng.es/bites/128/): Work with datetime's strptime and strftime

:star: [Unpacking lists into function arguments](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-list)

:star:: [strptime & strftime reference](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)

---

## Tasks:

:white_check_mark: Complete PyBite 7

:white_check_mark: Complete PyBite 67

:white_check_mark: Complete PyBite 128

---

## Notes:

:notebook: `strptime` - creates a `datetime` object from a **string** representing a date/time, with a corresponding **format string**:

```python
from datetime import datetime

# Convert a string to a datetime object
date_string = 'May 24, 1980'
date_object = datetime.strptime(date_string, '%B %d, %Y')
print(date_object)
# Output: datetime.datetime(1980, 5, 24, 0, 0)
```



:notebook: `strftime` - creates a **string** from a `date`, `datetime`, or `time` object, with a format string:

```python
from datetime import date

# Convert a date object to a string
today = date.today()
date_format_1 = today.strftime('%d %B, %Y')
date_format_2 = today.strftime('%m/%d/%y')
print(date_format_1, date_format_2)
# Output: 20 April, 2021 04/20/21
```

