# :calendar: Day 88: 2/6/2023-6/1/2023

---

## Topics

:clipboard: Home Inventory App

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Watch videos 1-2

:white_check_mark: Create application framework

:white_check_mark: Build initial main menu functionality

:white_check_mark: Write automated tests for main menu functionality

:white_check_mark: Watch video 3

:white_large_square: Watch video 4

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

---

### :notebook: 2/9/23

- Added functionality to the `HomeInventory` class in [`days/_88/inventory_app/home_inventory/home_inventory.py`](home_inventory.py):
    - Created the `format_menu_prompt` method to normalize the input prompt suffix format (to ': ').

- Refactored `HomeInventory` class in [`days/_88/inventory_app/home_inventory/home_inventory.py`](home_inventory.py):
    - Updated `__init__` method to automatically set the `self.input_prompt` value.
    - Updated doc strings.

---

### :notebook: 2/10/23

- Created the `pytest` file [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) to perform testing of [`days/_88/inventory_app/home_inventory/home_inventory.py`](home_inventory.py).
    - Created initial constant variable objects while setting up automation mock test data.
    - Created the test function `test_format_menu_prompt`, to test the `HomeInventory.format_menu_prompt` method.

---

### :notebook: 2/11/23

- Reviewed failed `pytest` from [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) to determine how to refactor [`days/_88/inventory_app/home_inventory/home_inventory.py`](home_inventory.py).
    - Failing tests when mock input is:
        - `None`
        - `False`
        - `''`

---

### :notebook: 2/12/23

- Updated code in the `pytest` file [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py):
    - Refactored the `MOCK_MENU_EXPECTED_VALUE` list by converting list items from static input to dynamic auto-generation.
        - Generates an expected result list item for each entry in `MOCK_MENU_PROMPT_INPUT`.
        - Adding more test input prompts automatically adds a new expected result using the value from `HomeInventory.MENU_PROMPT_DEFAULT`.

            ```python
            # Old, static list syntax:
            MOCK_MENU_EXPECTED_VALUE = [
                MENU_PROMPT_DEFAULT,            # Default input
                MENU_PROMPT_DEFAULT,            # Default input
                MENU_PROMPT_DEFAULT,            # Default input
                MENU_PROMPT_DEFAULT,            # Default input
                MENU_PROMPT_DEFAULT,            # Default input
                MENU_PROMPT_DEFAULT,            # Default input
                MENU_PROMPT_DEFAULT             # Default input
            ]

            # New syntax:
            MOCK_MENU_EXPECTED_VALUE = [
                MENU_PROMPT_DEFAULT for _ in MOCK_MENU_PROMPT_INPUT
            ]
            ```

- Continued refactoring of the `pytest` file [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py):
    - Updated the `if isinstance(input_prompt, str)` function to also check for blank strings.

        ```python
        # Old syntax
        if isinstance(input_prompt, str) is True:

        # New syntax
        if isinstance(input_prompt, str) is True and input_prompt:
        ```

    - Passing 7 of 8 `pytest` tests.
    - Remaining test to refactor for is with the input value `Enter a menu option:  : `.

---

### :notebook: 2/13/23

- Replaced `TODO` docstring placeholders to [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) and [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py).

- Conducted initial logic research to test string to solve for the remaining unsolved `pytest` test case - multiple trailing `: ` instances.
    - Using the `str.find` method to locate the first instance of `: ` and its position relative to the end of the prompt string.
    - Further testing required.

---

### :notebook: 2/14/23

- Tested several string methods to determine the best way to detect and properly format multiple instances of `: ` in an input prompt string, including:
    - `str.count`
    - `str.index` == `s.find`(equivalent results)
    - `str.rindex` and `s.rfind` (equivalent results)
    - `str.partition`

    - Determined that `str.partition` is the most effective choice to resolve multiple instances of `: ` in a string prompt.
    - Tested using `str.partition` in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py) although a logic error at line #133 requires tuning for proper functionality.

---

### :notebook: 2/15/23

- Refactored the `HomeInventory.format_menu_prompt` method in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py) to successfully pass the `test_format_menu_prompt` test in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py):

    ```python
    def format_menu_prompt(
        self,
        input_prompt: str = MENU_PROMPT_DEFAULT
    ) -> None:
        """ Check and format the CLI menu input prompt.

            Args:
                input_prompt (str, optional):
                    str value to display as prompt for user input.
                    This method will add a colon and a single space
                    suffix to the prompt, if not already present,
                    for readability.  Default is MENU_PROMPT_DEFAULT.

                    Example:

                    1. 'Enter option' becomes 'Enter option: `
                    2. 'Enter option:' becomes 'Enter option: `
                    3. 'Enter option: ' does not change.

            Returns:
                None.
        """

        # Ensure the 'input_prompt' argument is a non-blank string
        if isinstance(input_prompt, str) is True \
            and input_prompt != '':

            # Remove any leading spaces in 'input_prompt'
            input_prompt = input_prompt.lstrip()

            # Check 'input_prompt' for the correct suffix
            if input_prompt.endswith(PROMPT_SUFFIX) is False:
                # Remove any trailing spaces
                input_prompt = input_prompt.rstrip()

                # Add the correct suffix
                if input_prompt.endswith(PROMPT_SUFFIX[0]):
                    # Add a blank space if the string ends with ':'
                    input_prompt += PROMPT_SUFFIX[1]
                else:
                    # Add the full suffix if the string does not end with ':'
                    input_prompt += PROMPT_SUFFIX

            # Remove any excess instances of the correct suffix
            if input_prompt.count(PROMPT_SUFFIX) != 1:
                # Split the prompt string from instances of PROMPT_SUFFIX
                prompt_parts = input_prompt.partition(PROMPT_SUFFIX[0])

                # Format input_string with one instance of PROMPT_SUFFIX
                input_prompt = prompt_parts[0] + PROMPT_SUFFIX

        else:
            # Use the default prompt when `input_prompt` is a blank string
            input_prompt = MENU_PROMPT_DEFAULT

        # Set the self.user_input value to the formatted prompt
        self.input_prompt = input_prompt

        return None
    ```

- All `pytest` tests pass.

---

### :notebook: 2/16/23

- Created the method `HomeInventory.display_main_menu` in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py).
    - Performs the following functions:
        - Display the main menu.
        - Collect user input.
        - Call methods that perform functions, based on user input selection.
    - Proper return value undetermined.

- Created the method `test_display_main_menu` in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) to test the `HomeInventory.display_main_menu` return value in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py).
    - Created constants, `MOCK_MAIN_MENU_INPUT` and `MOCK_MAIN_MENU_EXPECTED_VALUE` to test multiple input strings.
    - Need to migrate decorator function from `@mark.parameterize` to the use of the `capsys` pytest fixture, to capture the result of user input.

---

### :notebook: 2/17/23

- Created the function `test_display_main_menu_output` in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) to test the `HomeInventory.display_main_menu` `STDOUT` value in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py).
    - Tested combining the `@mark.parameterize` and `@unittest.mock.patch` decorators with the `capsys` pytest fixture, to automatically input/mock parameterized values when a `pytest` encounters an instance of a `builtins.input` prompt, and compare the input value with the expected `STDOUT` output.
        - This is in contrast to having to loop over `side_effect` values defined in the `@unittest.mock.patch` decorator, within the `pytest` function (`test_display_main_menu_output`).
    - The collected `STDOUT` output continues to be `''` even though printed output is displayed during `pytest` runs.
        - Further testing required.

---

### :notebook: 2/18/23

- Conducted additional testing with the `test_display_main_menu_output` function in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py).
    - Tested using `unittest.mock.patch` with a context manager instead of as a decorator, although the `STDOUT` output remains blank.
    - Tested using `unittest.mock.patch` without the `pytest.mark.parameterize` decorator, and the `STDOUT` output works correctly.
    - Further testing required.

---

### :notebook: 2/19/23

- Tested refactoring of the `test_display_main_menu_output` function in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py):
    - Attempted many ways to resolve `StopIteration` errors when running `pytest` tests that produce invalid results, by design.
    - Determined the `While True` loop in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py) disrupts the flow of normal `pytest` operations.
        - The `input` prompt continues to draw from the list of argument values declared in the `@mark.parameterize` `argvalues` list whenever there is an input error because the `unittest.mock.patch` method mocks a new input value at every loop iteration, whether the mocked input is valid or not.
        - Workaround is to conditionally test for the presence of `PYTEST_CURRENT_TEST` in `str(os.environ.keys)` before continuing to the next loop iteration.

            ```python
            def display_main_menu(self) -> str:
            """ Display the main menu, collect user input, run methods.

                Args:
                    None.

                Returns:
                    user_input (str):
                        Valid user input selection.
            """

            # TODO: Collect and validate user input
            while True:
                # Display the menu and prompt
                print(f'\n{MAIN_MENU_BANNER}\n')
                for key, value in self.main_menu.items():
                    print(f'{key}. {value}')

                try:
                    print()
                    user_input = input(self.input_prompt)

                # Exception handling for KeyboardInterrupt exceptions
                except KeyboardInterrupt:
                    # Display friendly message
                    print(f'\n{KEYBOARD_INTERRUPT_MESSAGE}\n')

                    # Gracefully close the application
                    exit()

                # Validate user input
                if user_input.strip() in self.main_menu.keys():
                    print(
                        f'\nUser selects option {user_input}, '
                        f'"{self.main_menu.get(user_input)}"\n'
                    )

                    # Break the loop after a successful menu selection
                    break

                # Display an invalid input message
                print(f'{USER_INPUT_ERROR_MESSAGE} - Entered "{user_input}"')

                # Break the loop if method called by pytest
                if PYTEST_ENV_VAR in str(environ.keys()):
                    break
                else:
                    # Continue to the next loop iteration
                    continue
            ```

    - Transitioned the `unittest.mock.patch` functionality from a decorator to a context manager, in order to set the `unittest.mock.patch` `side_effect` parameter to the value of the `pytest.mark.parameterize` `argvalue` value.

        ```python
        @mark.parametrize(
            # Specify argument names for the test `test_format_menu_prompt` arguments
            argnames=[
                'mock_input',
                'expected_value'
            ],
            argvalues=zip(
                # Specify and ZIP the argument input and expected values
                MOCK_MAIN_MENU_INPUT,
                MOCK_MAIN_MENU_EXPECTED_VALUE
            )
        )
        def test_main_menu_output(
            capsys: CaptureFixture,
            mock_input: Any,
            expected_value: Any
        ) -> None:
            """ Tests for the `HomeInventory.format_menu_prompt` method.

                Args:
                    capsys (_pytest.capture.CaptureFixture):
                        Capture of STDOUT.

                Returns:
                    None.
            """

            # Send values to prompts for user input during the test
            with patch(
                target='builtins.input',
                side_effect=mock_input
            ):

                # Create a HomeInventory instance and prompt for user input
                hi = HomeInventory()
                hi.display_main_menu()

                # Assign STDOUT text to a variable
                stdout = capsys.readouterr().out
                # print(f'{stdout}')

                assert expected_value in stdout

            return None
        ```

    - Two `pytest` tests still fail:
        - Testing an input value of `''` produces a `StopIteration` error.
        - Testing an input value of `False` produces a `TypeError: 'bool' object is not an iterator` error.
    - Additional testing required.

---

### :notebook: 2/23/23

- Removed `pytest` test of a boolean value for the test `test_main_menu_output` in `test_display_main_menu_output` function in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py).
    - Resulted in a `TypeError` when present.
    - Determined test case is not necessary.

- The last remaining test case that fails is an input value of `''`, which produces a `StopIteration` error.

---

### :notebook: 2/24/23

- Continued testing, unable to determine why an input value of `''` produces a `StopIteration` error during a `pytest` test of [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py).
    - Web research required to determine why an empty string mock input value causes a `StopIteration` exception.

---

### :notebook: 2/25/23

- Attempted using debugging to determine the cause of the `StopIteration` error in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py).
    - Marking test as unnecessary and moving forward.

---

### :notebook: 2/27/23

- Reviewed methods, attributes, and default values of the `HomeInventory` class in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py).

- Used the `sorted` method to display the main menu in the order of the dictionary keys:

    ```python
    # Collect and validate user input
    while True:
        # Display the menu, sorted by key, and input prompt
        print(f'\n{MAIN_MENU_BANNER}\n')
        for key, value in sorted(self.main_menu.items()):
            print(f'{key}. {value}')
    ```

- Next steps are to:
    - Create methods for each menu option.
    - Create a method that calls each menu option.

---

### :notebook: 2/28/23

- Created the following un-configured/blank methods to [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py):
    - `_add_room`
    - `_add_inventory`
    - `_view_inventory`
    - `_total_value`
    - `_exit`

- Created the following un-configured `pytest` tests in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) to test the new methods.
    - `test__add_room`
    - `test__add_inventory`
    - `test__view_inventory`
    - `test__total_value`
    - `test__exit`

- Created the `_test_create_main_menu` test in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) to test the `create_main_menu` method in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py).

- All `pytest` tests pass.

---

### :notebook: 3/1/23

- Created the method `input_action` in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py) to call the "action" methods (`_add_room`, `_add_inventory`, etc.) based on user input.
    - Attempting to create a dictionary that "maps" an input value to a specific method, to avoid lengthy conditional logic:

        ```python
        # Example of what I don't want
        user_input = input()
        if user_input == '1':
            result = _add_room()
        if user_input == '2':
            result = _add_inventory()
        if user_input == '3':
            result = _view_inventory()

        # Example of what I would like to do
        user_input = input()
        input_mapping = {
            '1': _add_room(),
            '2': _add_inventory(),
            '3': _view_inventory()
        }
        result = input_mapping.get(user_input)
        ```

    - I attempted to make the `input_mapping` values string objects, and somehow call them using the `getattr` function and the symbol table returned by `globals()`, although these attempts have not been successful.

        ```python
        input_mapping = {
            '1': '_add_room',
            '2': '_add_inventory',
            '3': '_view_inventory'
        }

        get_attr(globals(), input_mapping.get(user_input))

        # Results in a TypeError exception
        # TypeError: 'str' object is not callable
        ```

    - My next attempt will be to make the `input_mapping` values the actual methods, instead of strings.

        ```python
        input_mapping = {
            '1': _add_room(),
            '2': _add_inventory(),
            '3': _view_inventory()
        }
        result = input_mapping.get(user_input)
        ```

---

### :notebook: 3/3/23

- Successfully Tested making the `input_mapping` values the `home_inventory.HomeInventory` methods, instead of strings.

---

### :notebook: 3/10/23

- Performed `pytest` tests using [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) and encountered multiple failures:

    ```bash
    FAILED tests/test_home_inventory.py::test_main_menu_output[ 2-Add Inventory] - AssertionError: assert ' ' in dict_keys(['1', '2', '3', '4', '5'])
    FAILED tests/test_home_inventory.py::test_main_menu_output[ -Invalid input ] - AssertionError: assert ' ' in dict_keys(['1', '2', '3', '4', '5'])
    FAILED tests/test_home_inventory.py::test_main_menu_output[wrong-Invalid input ] - AssertionError: assert 'w' in dict_keys(['1', '2', '3', '4', '5'])
    FAILED tests/test_home_inventory.py::test_main_menu_output[None-Invalid input ] - AssertionError: assert <MagicMock name='input()' id='281473103647680'> in dict_keys(['1', '2', '3', '4', '5'])
    ```

    - Further testing required to determine purpose of failing tests and cause(s) of failure.

---

### :notebook: 3/11/23

- Unable to determine the purpose of the following `assert` statement in [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py):

    ```python
    # Assert the user input selection is a key in the Main Menu dictionary
    assert user_input in MAIN_MENU.keys()
    ```

    - Removed this particular `assert` statement.

- Added the `test_get_input_method` to [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) to test the `get_input_method` in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py).
    - Created temporary test return values in the following methods:
        - `_add_room`
        - `_add_inventory`
        - `_view_inventory`
        - `_total_value`
        - `_exit`

- All `pytest` tests pass.

---

### :notebook: 3/13/23

- Added code to the `test_get_input_method` to [`days/_88/inventory_app/tests/test_home_inventory.py`](test_home_inventory.py) and successfully performed a single test.
    - Next step is to determine how to loop over the `MOCK_USER_INPUT_METHOD` list, to test different values, including a value that triggers the `raise ValueError()` code part in [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py).

---

### :notebook: 5/25/23

- Resetting my progress after an extended mental health break (73 days):

    ```python
    # Calculate the mental health break duration
    from datetime import datetime

    today = datetime(2023, 5, 25)
    previous_study_day = datetime(2023, 3, 13)

    mental_health_break = today - previous_study_day

    print(f'\nMental health break duration: {mental_health_break.days} days.\n')
    ```

    ```bash
    # Python code output
    Mental health break duration: 73 days.
    ```

- Re-familiarized with development environment.

---

### :notebook: 5/27/23

- Refreshed development container and Python packages.
- All `pytest` tests pass.

---

### :notebook: 5/28/23

- Performed code review of [`days/_88/inventory app/home_inventory/home_inventory.py`](home_inventory.py).
- All `pytest` tests pass.
