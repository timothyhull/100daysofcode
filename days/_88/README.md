# :calendar: Day 88: 2/6/2023-2/13/2023

---

## Topics

:clipboard: Home Inventory App

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Watch videos 1-2

:white_large_square: Create application framework

:white_large_square: Build initial main menu functionality

:white_large_square: Watch video 3

---

## Notes

### :notebook: 2/6/23

- Watched videos 1, 2, and 2:34 of video 3.
- Started developing home inventory application framework and main menu:
    - Created the following files:
        - [`days/_88/inventory_app/__init__.py`](__init__.py) - package initialization file.
        - [`days/_88/inventory_app/__main__.py`](__main__.py) - main package file.
        - [`days/_88/inventory_app/home_inventory/home_inventory.py`](home_inventory.py) - classes, functions, variables, etc. that comprise the application functionality.

    - Experimented with several different methods of creating a main menu:
        - A `typing.NamedTuple` object could work although it seems to be overcomplicated.
        - A `list` or `tuple` object would work although the relationship between index and value is less readable than ideal.
        - A `dict` object seems to be the best choice.

    - Created the `MAIN_MENU` constant in [`days/_88/inventory_app/home_inventory/home_inventory.py`](home_inventory.py) to provide a dictionary of menu options.

        ```python
        MAIN_MENU = {
            '1': 'Add Room',
            '2': 'Add Inventory',
            '3': 'View Inventory List',
            '4': 'Total Value',
            '5': 'Exit'
        }
        ```

---

### :notebook: 2/7/23

- Refactored/restructured [`days/_88/inventory_app/home_inventory/home_inventory.py`](home_inventory.py) such that the top-level object is a class (`HomeInventory`) with methods that perform different operations within an instance of the class:
    - The `create_main_menu` method creates a main menu using a dictionary of values (`menu_items`) passed as an argument.
        - The method creates the `self.main_menu` attribute with the dictionary of values in the `menu_items` parameter.
    - The `__init__` method calls the `create_main_menu` method and to automatically assign a default menu dictionary to `self.main_menu`.
        - The method accepts a custom set of menu values via the optional parameter `menu_items`.
        - The default dictionary value assigned to the `menu_items` parameter is `MAIN_MENU`.

---

### :notebook: 2/8/23

- Refactored `HomeInventory` class in [`days/_88/inventory_app/home_inventory/home_inventory.py`](home_inventory.py) to function properly with both default and custom values for the `self.main_menu` object.
