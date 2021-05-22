## :calendar: Day 7: 5/21/21

---

## Topics:

:clipboard: Python Data Structures - `list`, `tuple`, and `dictionary`

---

## Resources:

:star: TBD

---

## Tasks:

:white_check_mark: Watch videos 1-3

:white_large_square: Watch videos 4-6

---

## Notes:

#### :notebook: 5/21/21

`list` objects

```Python
# Create a list (these are three example options)
num_list = [1, 2, 3, 4, 5]
num_list_1 = [x for x in range(1,6)]
num_list_2 = list(range(1,6))

# In [2]: num_list
# Out[2]: [1, 2, 3, 4, 5]

# Reverse the list item order
num_list.reverse()
# In [6]: num_list
# Out[6]: [5, 4, 3, 2, 1]

# Reverse the list order with the `sort` method
num_list.sort()
# In [8]: num_list
# Out[8]: [1, 2, 3, 4, 5]

# Convert a string to a list
my_name = 'timothy'
my_name_list = list(my_name)
#In [11]: list(my_name)
#Out[11]: ['t', 'i', 'm', 'o', 't', 'h', 'y']

# Return the last item from a list, and remove that item with the `pop` method
# In [16]: my_name_list.pop()
# Out[16]: 'y'

# In [18]: my_name_list
# Out[18]: ['t', 'i', 'm', 'o', 't', 'h', 'y']

# Remove from any list index with the `pop` method
my_name_list.pop(3)
In [23]: my_name_list
Out[23]: ['t', 'i', 'm', 't', 'h']

# Insert a list item at a specified index (insert before the specified index)
my_name_list.insert(3, 'o')

# Add an item to the end of a list with the `append` method
my_name_list.append('y')

# Remove, without returning a value, any list item
del my_name_list[0]

# In [31]: my_name_list
# Out[31]: ['i', 'm', 'o', 't', 'h', 'y']
```

