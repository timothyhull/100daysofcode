## :calendar: Day 6: 5/14/2021-5/16/2021

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

:white_large_square: Sort data and produce formatted output.

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



- The `sorted` method did not help:

```python
In [7]: sorted(lights.items())
Out[7]: 
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

