## :calendar: Day 6: 5/14/2021-5/20/2021

---

## Topics:

:clipboard: Use `collections` with my own data

---

## Resources:

:star: N/A

---

## Tasks:

:white_check_mark: Identify data set to work with ([see notes](#notes)).

:white_check_mark: Gather data set and review `collections` module options to more simply sort/manager the data.

:white_check_mark: Sort data and produce formatted output.

:white_check_mark: Update SML source code with new, simplified code.

:white_check_mark: Sort SML lights by name, alphabetically and correct capitalization.

:white_check_mark: Review `collections` objects [Jupyter Notebook](4/collections.ipynb).

---

## Notes:

#### :notebook: 5/14/21

Replace `lambda` function in Smart Meeting Light with `collection` object(s) that simplify the code:

* Current process:

```python
# Update the 'all_lights' dictionary items with light modes
    for key, value in all_lights.items():
        if value['type'] in light_types['enhanced']['names']:
            value.update({'sml_modes': light_types['enhanced']['modes']})
        else:
            value.update({'sml_modes': light_types['basic']['modes']})

    # Sort the dictionary of light IDs by the light names
    all_lights = sorted(all_lights.items(), key=lambda x: x[1]['name'])

    # Find the light with the longest name
    name_len = []
    for i, v in enumerate(all_lights):
        name_len.append(len(all_lights[i][1]['name']))
    spaces = max(name_len) + 1

    # Display list of lights and modes
    msg_banner('** Choose a light for availability monitoring **')
    print()

    # Display column headers
    header = f'No:  {"Name:":<{spaces}} {"Modes:":<28}'
    print(header)
    print(f'{"-" * len(header)}')

    # Output light list with modes
    for i, v in enumerate(all_lights):

        # Display light list number and name
        print(f'{i + 1:>2}.  '
              f'{all_lights[i][1]["name"]:<{spaces}} ', end='')

        # Loop over 'sml_modes' key and display mode capability names
        for index, mode in enumerate(all_lights[i][1]['sml_modes']):
            print(f'{light_modes[mode]["name"]}', end='')

            # Print a separator (, ) if not the last item in the mode list
            if index != len(all_lights[i][1]['sml_modes']) - 1:
                print(', ', end='')

            # Print a new line if the last item in the mode list
            else:
                print()
    print()
```

---

#### :notebook: 5/15/21

Complete the [implementation of doc strings](https://github.com/wwt/smart-meeting-light/pull/110) and function parameter typing in the Smart Meeting Light app.

---

#### :notebook: 5/16/21

- Produced initial form of refined data set, which is a `dict` of `namedtuple` objects.

```python
{'1': LightData(name='Entry 1', modes=['basic', 'basic+color', 'enhanced']),
 '10': LightData(name='Great Room Staircase', modes=['basic', 'basic+color', 'enhanced']),
 '11': LightData(name="Ella's Lamp", modes=['basic', 'basic+color', 'enhanced']),
 '12': LightData(name="Tim's Bedside", modes=['basic', 'basic+color', 'enhanced']),
 '14': LightData(name='Kitchen 2', modes=['basic', 'basic+color', 'enhanced']),
 '15': LightData(name='Kitchen 3', modes=['basic', 'basic+color', 'enhanced']),
 '16': LightData(name='Kitchen 4', modes=['basic', 'basic+color', 'enhanced']),
 '17': LightData(name='Kitchen 5', modes=['basic', 'basic+color', 'enhanced']),
 '18': LightData(name='Kitchen 6', modes=['basic', 'basic+color', 'enhanced']),
 '19': LightData(name='Kitchen 7', modes=['basic', 'basic+color', 'enhanced']),
 '2': LightData(name='Entry 2', modes=['basic', 'basic+color', 'enhanced']),
 '20': LightData(name='Dining 3', modes=['basic']),
 '21': LightData(name='Dining 4', modes=['basic']),
 '22': LightData(name='Dining 1', modes=['basic']),
 '23': LightData(name='Dining 2', modes=['basic']),
 '25': LightData(name='Entry 4', modes=['basic']),
 '26': LightData(name='Entry 5', modes=['basic']),
 '27': LightData(name='Dining 5', modes=['basic']),
 '29': LightData(name='Kitchen 1', modes=['basic']),
 '3': LightData(name='Entry 3', modes=['basic', 'basic+color', 'enhanced']),
 '30': LightData(name='Work Status Bar', modes=['basic', 'basic+color', 'enhanced']),
 '31': LightData(name='Bookshelf Status', modes=['basic', 'basic+color', 'enhanced']),
 '32': LightData(name='Lamp', modes=['basic']),
 '33': LightData(name='Desk Right', modes=['basic', 'basic+color', 'enhanced']),
 '34': LightData(name='Desk Left', modes=['basic', 'basic+color', 'enhanced']),
 '4': LightData(name="Sara's Bedside", modes=['basic', 'basic+color', 'enhanced']),
 '6': LightData(name='Lily’s Lamp', modes=['basic', 'basic+color', 'enhanced']),
 '7': LightData(name='Great Room Fireplace', modes=['basic', 'basic+color', 'enhanced']),
 '8': LightData(name='Great Room Back Door', modes=['basic', 'basic+color', 'enhanced']),
 '9': LightData(name='Great Room Wine Closet', modes=['basic', 'basic+color', 'enhanced'])}
```



* The ID numbers (`dict` keys) still require sorting.
  * Using the command `Counter(lights).most_common()` does not order the dictionary keys correctly:

```python
Counter(lights).most_common()

[('30',
  LightData(name='Work Status Bar', modes=['basic', 'basic+color', 'enhanced'])),
 ('12',
  LightData(name="Tim's Bedside", modes=['basic', 'basic+color', 'enhanced'])),
 ('4',
  LightData(name="Sara's Bedside", modes=['basic', 'basic+color', 'enhanced'])),
 ('6',
  LightData(name='Lily’s Lamp', modes=['basic', 'basic+color', 'enhanced'])),
 ('32', LightData(name='Lamp', modes=['basic'])),
 ('19',
  LightData(name='Kitchen 7', modes=['basic', 'basic+color', 'enhanced'])),
 ('18',
  LightData(name='Kitchen 6', modes=['basic', 'basic+color', 'enhanced'])),
 ('17',
  LightData(name='Kitchen 5', modes=['basic', 'basic+color', 'enhanced'])),
 ('16',
  LightData(name='Kitchen 4', modes=['basic', 'basic+color', 'enhanced'])),
 ('15',
  LightData(name='Kitchen 3', modes=['basic', 'basic+color', 'enhanced'])),
 ('14',
  LightData(name='Kitchen 2', modes=['basic', 'basic+color', 'enhanced'])),
 ('29', LightData(name='Kitchen 1', modes=['basic'])),
 ('9',
  LightData(name='Great Room Wine Closet', modes=['basic', 'basic+color', 'enhanced'])),
 ('10',
  LightData(name='Great Room Staircase', modes=['basic', 'basic+color', 'enhanced'])),
 ('7',
  LightData(name='Great Room Fireplace', modes=['basic', 'basic+color', 'enhanced'])),
 ('8',
  LightData(name='Great Room Back Door', modes=['basic', 'basic+color', 'enhanced'])),
 ('26', LightData(name='Entry 5', modes=['basic'])),
 ('25', LightData(name='Entry 4', modes=['basic'])),
 ('3', LightData(name='Entry 3', modes=['basic', 'basic+color', 'enhanced'])),
 ('2', LightData(name='Entry 2', modes=['basic', 'basic+color', 'enhanced'])),
 ('1', LightData(name='Entry 1', modes=['basic', 'basic+color', 'enhanced'])),
 ('11',
  LightData(name="Ella's Lamp", modes=['basic', 'basic+color', 'enhanced'])),
 ('27', LightData(name='Dining 5', modes=['basic'])),
 ('21', LightData(name='Dining 4', modes=['basic'])),
 ('20', LightData(name='Dining 3', modes=['basic'])),
 ('23', LightData(name='Dining 2', modes=['basic'])),
 ('22', LightData(name='Dining 1', modes=['basic'])),
 ('33',
  LightData(name='Desk Right', modes=['basic', 'basic+color', 'enhanced'])),
 ('34',
  LightData(name='Desk Left', modes=['basic', 'basic+color', 'enhanced'])),
 ('31',
  LightData(name='Bookshelf Status', modes=['basic', 'basic+color', 'enhanced']))]
```



* Using `Counter` on only the dictionary keys performs the correct sort operation although there are no corresponding values:

```python
Counter(lights.keys())

Counter({'1': 1,
         '2': 1,
         '3': 1,
         '4': 1,
         '6': 1,
         '7': 1,
         '8': 1,
         '9': 1,
         '10': 1,
         '11': 1,
         '12': 1,
         '14': 1,
         '15': 1,
         '16': 1,
         '17': 1,
         '18': 1,
         '19': 1,
         '20': 1,
         '21': 1,
         '22': 1,
         '23': 1,
         '25': 1,
         '26': 1,
         '27': 1,
         '29': 1,
         '30': 1,
         '31': 1,
         '32': 1,
         '33': 1,
         '34': 1})
```



- The `sorted` method did not help:

```python
sorted(lights.items())

[('1', LightData(name='Entry 1', modes=['basic', 'basic+color', 'enhanced'])),
 ('10',
  LightData(name='Great Room Staircase', modes=['basic', 'basic+color', 'enhanced'])),
 ('11',
  LightData(name="Ella's Lamp", modes=['basic', 'basic+color', 'enhanced'])),
 ('12',
  LightData(name="Tim's Bedside", modes=['basic', 'basic+color', 'enhanced'])),
 ('14',
  LightData(name='Kitchen 2', modes=['basic', 'basic+color', 'enhanced'])),
 ('15',
  LightData(name='Kitchen 3', modes=['basic', 'basic+color', 'enhanced'])),
 ('16',
  LightData(name='Kitchen 4', modes=['basic', 'basic+color', 'enhanced'])),
 ('17',
  LightData(name='Kitchen 5', modes=['basic', 'basic+color', 'enhanced'])),
 ('18',
  LightData(name='Kitchen 6', modes=['basic', 'basic+color', 'enhanced'])),
 ('19',
  LightData(name='Kitchen 7', modes=['basic', 'basic+color', 'enhanced'])),
 ('2', LightData(name='Entry 2', modes=['basic', 'basic+color', 'enhanced'])),
 ('20', LightData(name='Dining 3', modes=['basic'])),
 ('21', LightData(name='Dining 4', modes=['basic'])),
 ('22', LightData(name='Dining 1', modes=['basic'])),
 ('23', LightData(name='Dining 2', modes=['basic'])),
 ('25', LightData(name='Entry 4', modes=['basic'])),
 ('26', LightData(name='Entry 5', modes=['basic'])),
 ('27', LightData(name='Dining 5', modes=['basic'])),
 ('29', LightData(name='Kitchen 1', modes=['basic'])),
 ('3', LightData(name='Entry 3', modes=['basic', 'basic+color', 'enhanced'])),
 ('30',
  LightData(name='Work Status Bar', modes=['basic', 'basic+color', 'enhanced'])),
 ('31',
  LightData(name='Bookshelf Status', modes=['basic', 'basic+color', 'enhanced'])),
 ('32', LightData(name='Lamp', modes=['basic'])),
 ('33',
  LightData(name='Desk Right', modes=['basic', 'basic+color', 'enhanced'])),
 ('34',
  LightData(name='Desk Left', modes=['basic', 'basic+color', 'enhanced'])),
 ('4',
  LightData(name="Sara's Bedside", modes=['basic', 'basic+color', 'enhanced'])),
 ('6',
  LightData(name='Lily’s Lamp', modes=['basic', 'basic+color', 'enhanced'])),
 ('7',
  LightData(name='Great Room Fireplace', modes=['basic', 'basic+color', 'enhanced'])),
 ('8',
  LightData(name='Great Room Back Door', modes=['basic', 'basic+color', 'enhanced'])),
 ('9',
  LightData(name='Great Room Wine Closet', modes=['basic', 'basic+color', 'enhanced']))]
```

---

#### :notebook: 5/17/21

- Remove the `defaultdict` object and, instead, use a conventional `list` object.
- Add an attribute for ID to the `namedtuple` which carries the value of the dictionary key (ID number) for a given light.
- Produce the output in the same format as the original code but with simplified code.

```raw
** Choose a light for availability monitoring **

No:  Name:                   Modes:                      
---------------------------------------------------------
 1.  Entry 1                 basic, basic+color, enhanced
 2.  Entry 2                 basic, basic+color, enhanced
 3.  Entry 3                 basic, basic+color, enhanced
 4.  Sara's Bedside          basic, basic+color, enhanced
 5.  Lily’s Lamp             basic, basic+color, enhanced
 6.  Great Room Fireplace    basic, basic+color, enhanced
 7.  Great Room Back Door    basic, basic+color, enhanced
 8.  Great Room Wine Closet  basic, basic+color, enhanced
 9.  Great Room Staircase    basic, basic+color, enhanced
10.  Ella's Lamp             basic, basic+color, enhanced
11.  Tim's Bedside           basic, basic+color, enhanced
12.  Kitchen 2               basic, basic+color, enhanced
13.  Kitchen 3               basic, basic+color, enhanced
14.  Kitchen 4               basic, basic+color, enhanced
15.  Kitchen 5               basic, basic+color, enhanced
16.  Kitchen 6               basic, basic+color, enhanced
17.  Kitchen 7               basic, basic+color, enhanced
18.  Dining 3                basic
19.  Dining 4                basic
20.  Dining 1                basic
21.  Dining 2                basic
22.  Entry 4                 basic
23.  Entry 5                 basic
24.  Dining 5                basic
25.  Kitchen 1               basic
26.  Work Status Bar         basic, basic+color, enhanced
27.  Bookshelf Status        basic, basic+color, enhanced
28.  Lamp                    basic
29.  Desk Right              basic, basic+color, enhanced
30.  Desk Left               basic, basic+color, enhanced
```

---

#### :notebook: 5/18/21

* Transposed new code into application.
* Updated Hue remote (OAuth) API authentication to v2
* Formatting requires capitalization of **modes** column values plus alphabetical sorting by light name
* Old and new format comparison, side by side:

<table>
<tr>
<th>Old</th>
<th>New</th>
</tr>
<tr>
<td>

```bash
	No:  Name:                   Modes:                      
	---------------------------------------------------------
	 1.  Bookshelf Status        Basic, Basic+Color, Enhanced
	 2.  Desk Left               Basic, Basic+Color, Enhanced
	 3.  Desk Right              Basic, Basic+Color, Enhanced
	 4.  Dining 1                Basic
	 5.  Dining 2                Basic
	 6.  Dining 3                Basic
	 7.  Dining 4                Basic
	 8.  Dining 5                Basic
	 9.  Ella's Lamp             Basic, Basic+Color, Enhanced
	10.  Entry 1                 Basic, Basic+Color, Enhanced
	11.  Entry 2                 Basic, Basic+Color, Enhanced
	12.  Entry 3                 Basic, Basic+Color, Enhanced
	13.  Entry 4                 Basic
	14.  Entry 5                 Basic
	15.  Great Room Back Door    Basic, Basic+Color, Enhanced
	16.  Great Room Fireplace    Basic, Basic+Color, Enhanced
	17.  Great Room Staircase    Basic, Basic+Color, Enhanced
	18.  Great Room Wine Closet  Basic, Basic+Color, Enhanced
	19.  Kitchen 1               Basic
	20.  Kitchen 2               Basic, Basic+Color, Enhanced
	21.  Kitchen 3               Basic, Basic+Color, Enhanced
	22.  Kitchen 4               Basic, Basic+Color, Enhanced
	23.  Kitchen 5               Basic, Basic+Color, Enhanced
	24.  Kitchen 6               Basic, Basic+Color, Enhanced
	25.  Kitchen 7               Basic, Basic+Color, Enhanced
	26.  Lamp                    Basic
	27.  Lily’s Lamp             Basic, Basic+Color, Enhanced
	28.  Sara's Bedside          Basic, Basic+Color, Enhanced
	29.  Tim's Bedside           Basic, Basic+Color, Enhanced
	30.  Work Status Bar         Basic, Basic+Color, Enhanced	
```

</td>
<td>

```bash
		No:  Name:                   Modes:                      
	---------------------------------------------------------
	 1.  Entry 1                 basic, basic+color, enhanced
	 2.  Entry 2                 basic, basic+color, enhanced
	 3.  Entry 3                 basic, basic+color, enhanced
	 4.  Sara's Bedside          basic, basic+color, enhanced
	 5.  Lily’s Lamp             basic, basic+color, enhanced
	 6.  Great Room Fireplace    basic, basic+color, enhanced
	 7.  Great Room Back Door    basic, basic+color, enhanced
	 8.  Great Room Wine Closet  basic, basic+color, enhanced
	 9.  Great Room Staircase    basic, basic+color, enhanced
	10.  Ella's Lamp             basic, basic+color, enhanced
	11.  Tim's Bedside           basic, basic+color, enhanced
	12.  Kitchen 2               basic, basic+color, enhanced
	13.  Kitchen 3               basic, basic+color, enhanced
	14.  Kitchen 4               basic, basic+color, enhanced
	15.  Kitchen 5               basic, basic+color, enhanced
	16.  Kitchen 6               basic, basic+color, enhanced
	17.  Kitchen 7               basic, basic+color, enhanced
	18.  Dining 3                basic
	19.  Dining 4                basic
	20.  Dining 1                basic
	21.  Dining 2                basic
	22.  Entry 4                 basic
	23.  Entry 5                 basic
	24.  Dining 5                basic
	25.  Kitchen 1               basic
	26.  Work Status Bar         basic, basic+color, enhanced
	27.  Bookshelf Status        basic, basic+color, enhanced
	28.  Lamp                    basic
	29.  Desk Right              basic, basic+color, enhanced
	30.  Desk Left               basic, basic+color, enhanced
```

</td>
</tr>
</table>

---

#### :notebook: 5/19/21

- Sorted list of lights by making **name** the first attribute in the **lights** `namedtuple` and then using the `sort()` method on the **lights** object.
  - The `sort()` method appears to sort `namedtuple` objects using the first attribute as the sort key.
- Capitalized the first letter in each mode name using the `title()` method on the output strings.

```python
### Code changes ###
# Create namedtuple class to store data for a light
LightData = namedtuple('LightData', 'name id modes')

# Create a list object to store namedtuples of light data
lights = []

# Loop over the data set and populate the lights list with namedtuples
for key, value in all_lights.items():
    # Determine whether or not the light supports enhanced modes
    if value['type'] in light_types['enhanced']['names']:
        light_mode = light_types['enhanced']['modes']
    else:
        light_mode = light_types['basic']['modes']

    # Add a namedtuple of light data to the 'lights' list
    lights.append(
        LightData(
            name=value.get('name', None),
            id=key,
            modes=light_mode
        )
    )

# Sort the list by the first attribute name in the LightData (name)
lights.sort()

# Display list of lights and modes
for index, light in enumerate(lights):
    print(f'{index + 1:>2}.  '
          f'{light.name:<{spaces}} '
          f'{", ".join(light.modes).title()}')
```

```python
### Change result ###
No:  Name:                   Modes:                      
---------------------------------------------------------
 1.  Bookshelf Status        Basic, Basic+Color, Enhanced
 2.  Desk Left               Basic, Basic+Color, Enhanced
 3.  Desk Right              Basic, Basic+Color, Enhanced
 4.  Dining 1                Basic
 5.  Dining 2                Basic
 6.  Dining 3                Basic
 7.  Dining 4                Basic
 8.  Dining 5                Basic
 9.  Ella's Lamp             Basic, Basic+Color, Enhanced
10.  Entry 1                 Basic, Basic+Color, Enhanced
11.  Entry 2                 Basic, Basic+Color, Enhanced
12.  Entry 3                 Basic, Basic+Color, Enhanced
13.  Entry 4                 Basic
14.  Entry 5                 Basic
15.  Great Room Back Door    Basic, Basic+Color, Enhanced
16.  Great Room Fireplace    Basic, Basic+Color, Enhanced
17.  Great Room Staircase    Basic, Basic+Color, Enhanced
18.  Great Room Wine Closet  Basic, Basic+Color, Enhanced
19.  Kitchen 1               Basic
20.  Kitchen 2               Basic, Basic+Color, Enhanced
21.  Kitchen 3               Basic, Basic+Color, Enhanced
22.  Kitchen 4               Basic, Basic+Color, Enhanced
23.  Kitchen 5               Basic, Basic+Color, Enhanced
24.  Kitchen 6               Basic, Basic+Color, Enhanced
25.  Kitchen 7               Basic, Basic+Color, Enhanced
26.  Lamp                    Basic
27.  Lily’s Lamp             Basic, Basic+Color, Enhanced
28.  Sara's Bedside          Basic, Basic+Color, Enhanced
29.  Tim's Bedside           Basic, Basic+Color, Enhanced
30.  Work Status Bar         Basic, Basic+Color, Enhanced
```



- Updated the expressions that assigns attribute values from the selected light to the old, `dictionary` key index format to the new, `namedtuple` attribute index format:

```python
### Code changes ###
light = {}
if light_input in range(1, len(lights) + 1):
    # Assign the chosen light's list item to a variable
    light_item = lights[light_input - 1]

    # Extract the ID, name, and modes from the 'lights' namedtuple list
    light.update(
        {'light_id': light_item.id}
    )
    light.update(
        {'light_name': light_item.name}
    )
    light.update(
        {'light_modes': light_item.modes}
    )
```

```python
### Change result ###
{'light_id': '31',
 'light_name': 'Bookshelf Status',
 'light_modes': ['basic', 'basic+color', 'enhanced']}
```



---

#### :notebook: 5/20/21

* Conducted review of `collections` object [Jupyter Notebook notes.](../4/collections.ipynb)

