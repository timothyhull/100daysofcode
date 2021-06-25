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

:star: [strptime & strftime reference](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)

:star: [datetime.fromisoformat reference](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat)

---

## Tasks:

:white_check_mark: Complete PyBite 7 - **4/19/21**

:white_check_mark: Complete PyBite 67 - **4/20/21**

:white_check_mark: Complete PyBite 128 - **4/21/21**

:white_check_mark: Revise PyBite 7 using `datetime.fromisoformat` method - **4/21/21**

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



:notebook: `datetime.fromisoformat` - creates a `datetime` object from an ISO-formatted date string:

```
# * can match any any single character
YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]

# Examples:
>>> from datetime import datetime
>>> datetime.fromisoformat('2011-11-04')
datetime.datetime(2011, 11, 4, 0, 0)
>>> datetime.fromisoformat('2011-11-04T00:05:23')
datetime.datetime(2011, 11, 4, 0, 5, 23)
>>> datetime.fromisoformat('2011-11-04 00:05:23.283')
datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
>>> datetime.fromisoformat('2011-11-04 00:05:23.283+00:00')
datetime.datetime(2011, 11, 4, 0, 5, 23, 283000, tzinfo=datetime.timezone.utc)
>>> datetime.fromisoformat('2011-11-04T00:05:23+04:00')   
datetime.datetime(2011, 11, 4, 0, 5, 23,
    tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))
```


