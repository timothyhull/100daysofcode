# :calendar: Days 83+84: 7/10/2022-12/17/2022

---

## Topics

:clipboard: Data Visualization with Plotly

---

## Resources

:star: [Climate Change Indicators Dashboard](https://climatedata.imf.org/pages/access-data)

:star: [Climate Change Indicators Data/Metadata](https://climatedata.imf.org/pages/access-data)

:star: [Atmospheric CO2 Indicators Data](https://climatedata.imf.org/datasets/9c3764c0efcc4c71934ab3988f219e0e/explore)

:star: [Atmospheric CO2 Indicators API Query Info](https://climatedata.imf.org/datasets/9c3764c0efcc4c71934ab3988f219e0e/api)

:star: [Plotly Express Documentation](https://plotly.com/python/plotly-express)

:star: [`unittest.mock.mock_open` documentation](https://docs.python.org/3/library/unittest.mock.html#mock-open)

:star::star::star: [`mock_open` Tutorial Blog Post](https://nickolaskraus.io/articles/how-to-mock-the-built-in-function-open)

:star: [Plotly Time and Date Axes in Python](https://plotly.com/python/time-series)

:star: [Plotly Subplots (multiple stacked plots with a shared axis)](https://plotly.com/python/subplots/#subplots-with-shared-xaxes)

:star: [Python NamedTuple object with type hint and default values support](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

:star: [Web Visualization with Plotly and Flask article](https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946) - alternate reference, did not use in this application

:star: [Python abstract factory example](https://stackabuse.com/abstract-factory-design-pattern-in-python)

:star: [`pygount` Python line counting CLI tool](https://pypi.org/project/pygount/):

:star: [Python factory design pattern tutorial video](https://www.youtube.com/watch?v=s_4ZrtQs8Do)

:star: [Python Documentation: Abstract Base Classes (abc)](https://docs.python.org/3/library/abc.html)

:star: [Pluralsight Python Design Patterns Course](https://app.pluralsight.com/course-player?courseId=c142e95a-ec41-44db-add1-7dd1f6c2851d)

:star: [Python `inspect` Module](https://docs.python.org/3/library/inspect.html)

---

## Tasks

:white_check_mark: Watch videos 8-9

:white_check_mark: Choose project application to develop - graph climate data

:white_check_mark: Develop application outline

:white_check_mark: Integrate with Better Code Hub

:white_check_mark: Setup requirements files

:white_check_mark: Download atmospheric CO2 data set from API source

:white_check_mark: Setup basic `Flask` web service

:white_check_mark: Format atmospheric CO2 data `Date` key as a `datetime.datetime` object

:white_check_mark: Write method to initialize `Plotly` in offline mode

:white_check_mark: Write method to format climate data for X and Y-axis plotting.

:white_check_mark: Write `pytest` tests for [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py)

:white_check_mark: Write application to plot monthly atmospheric Co2 values with `Plotly`

:white_check_mark: Add application diagram to [README.md](https://github.com/timothyhull/climate-data-plotly/blob/main/README.md) using `mermaid`

:white_check_mark: Write application to plot monthly atmospheric Co2 percentage change values with `Plotly`

:white_check_mark: Write `pytest` tests for the `plot_atmospheric_co2_data_go` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py)

:white_check_mark: Create mechanism to overlay the PPM and YoY Co2 data

:white_check_mark: Write `pytest` tests for the `_compress_y_axis` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py)

:white_check_mark: Complete refactoring checklist items from [Days 83+84ar](#notebook-82422)

:white_check_mark: Write `pytest` tests for [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py)

:white_check_mark: Publish application in `Flask` app

:white_check_mark: Thoroughly review the Abstract Factory Design Pattern

---

## Notes

### :notebook: 7/10/22

- Watched videos 8-9.
- Researched climate change data sets.
- Prepared plan for app development.

---

### :notebook: 7/11/22

- Setup project GitHub repository file at [https://github.com/timothyhull/climate-data-plotly](https://github.com/timothyhull/climate-data-plotly).
    - Setup [README.md](https://github.com/timothyhull/climate-data-plotly/blob/main/README.md) with basic application framework and status/quality badges.
    - Setup integration with Better Code Hub.

---

### :notebook: 7/12/22

- Setup requirements files:
    - [requirements/requirements.txt](https://github.com/timothyhull/climate-data-plotly/blob/main/requirements/requirements.txt) - Distribution dependencies.
    - [requirements/requirements_dev.txt](https://github.com/timothyhull/climate-data-plotly/blob/main/requirements/requirements_dev.txt) - Development dependencies.
    - [requirements/requirements_linting.txt](https://github.com/timothyhull/climate-data-plotly/blob/main/requirements/requirements_linting.txt) - GitHub action linting dependencies.
    - [requirements/requirements_pytest.txt](https://github.com/timothyhull/climate-data-plotly/blob/main/requirements/requirements_pytest.txt) - GitHub action `pytest` dependencies.

- Created new Python files:
    - [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py), to run the main application.
    - [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py), to source the `ClimateData` class.

- Successfully retrieved atmospheric Co2 data from the API using the `ClimateData._get_atmospheric_co2_data` method.

---

### :notebook: 7/13/22

- Created the `_convert_date_string` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to convert date strings to `datetime.datetime` objects.
    - Updated the `_get_atmospheric_co2_data` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to format atmospheric CO2 data `Date` keys as `datetime.datetime` objects, using the `_convert_date_string` method.

- Created initial `pytest` file, [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py).
    - Created initial test function `test_convert_date_string` to test the `_convert_date_string` in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
    - All tests pass.

---

### :notebook: 7/14/22

- Created the file [web/flask_app.py](https://github.com/timothyhull/climate-data-plotly/blob/main/web/flask_app.py) to run the `Flask` web service.
    - Tested Flask service with string output from an instance of the `ClimateData` class in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

---

### :notebook: 7/15/22

- Created the HTML template file [web/templates/index.html](https://github.com/timothyhull/climate-data-plotly/blob/main/web/templates/index.html) to test the `render_template` method in [web/flask_app.py](https://github.com/timothyhull/climate-data-plotly/blob/main/web/flask_app.py).

- Created the framework for the `plot_atmospheric_co2_data` function in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

---

### :notebook: 7/16/22

- Created the `_init_plotly_offline_mode` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to initialize `Plotly` in offline mode.

---

### :notebook: 7/17/22

- Created the following method placeholders in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py):
    - `transpose_data_for_graphing` - Transpose raw data from the climate API to X and Y axis coordinate data.
    - `plot_atmospheric_co2_data` - Display atmospheric Co2 data in a graph.

---

### :notebook: 7/18/22

- Created the following methods in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py):
    - `_get_co2_ppm_date_data` - Extract a dictionary from data self.atmospheric_co2_data that only contains parts per million (PPM) and dates of measurement.
    - `_get_co2_yoy_change_data` - Extract a dictionary from data self.atmospheric_co2_data that only contains % YoY change and dates of measurement.

- Added code to the `transpose_data_for_graphing` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) that returns data transposed to a graphing-friendly (X and Y-axis) format.

- Added placeholder test functions to [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - `test_get_atmospheric_co2_data`
    - `test_transpose_data_for_graphing`
    - `test_plot_atmospheric_co2_data`
    - `test_get_co2_ppm_date_data`
    - `test_get_co2_yoy_change_data`

---

### :notebook: 7/19/22

- Added the packages to [requirements/requirements.txt](https://github.com/timothyhull/climate-data-plotly/blob/main/requirements/requirements.txt) and [requirements/requirements_dev.txt](https://github.com/timothyhull/climate-data-plotly/blob/main/requirements/requirements_dev.txt):
    - `pandas` - required to support `plotly.express`.
    - `kaleido` - required to export a `plotly.express` line graph to an image file.

- Added code to the `ClimateData.plot_atmospheric_co2_data` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
    - The method returns a `tuple` with a binary PNG in index 0, and a text HTML in index 1.

---

### :notebook: 7/20/22

- Created the `write_plot_html_file` method and revised the `plot_atmospheric_co2_data` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to write HTML plot data to local storage.
    - Successfully created and opened the file [app/plot_files/climate_data_1.html](https://github.com/timothyhull/climate-data-plotly/blob/main/app/plot_files/climate_data_1.html).

---

### :notebook: 7/21/22

- Added initial although incomplete code to the `test_get_atmospheric_co2_data` function  [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py).

---

### :notebook: 7/22/22

- Continued work on the `test_get_atmospheric_co2_data` function  [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - Added the `MOCK_RAW_CO2_JSON` and `MOCK_RAW_CO2_DICT` constants to mock the HTTP `GET` request and response objects.

---

### :notebook: 7/23/22

- Updated the [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py) `pytest` tests file:
    - Completed the `test_get_atmospheric_co2_data` function
    - Converted the `'Date'` key values in `MOCK_ROW_CO2_LIST` to `datetime.datetime` objects.
    - Created the `mock_api_request` `pytest` fixture to reduce code repetition.
    - Added the `mock_api_request_bad_date` `pytest` fixture to test for invalid date strings.
    - Updated the `test_convert_date_string function` to support the new `pytest` fixtures.
    - Added the `test_convert_date_string_error` function to test for a `ValueError` exception for invalid date strings.

- Add exception handling for invalid date strings to [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

---

### :notebook: 7/24/22

- Revised the `mock_api_request` `pytest` fixture in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py) to support passing arguments:
    - Nested a `_mock_api_request` function with a parameter (`status_code`) in the `mock_api_request` `pytest` fixture.
    - The revisions use a `pytest` _factory fixture_ methodology and allows passing custom arguments to a `pytest` fixture, promoting reuse of the fixture by several test functions.

- Revised the `test_get_atmospheric_co2_data` function in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - Sends arguments to the `mock_api_request` `pytest` fixture.

- Created the `test_get_atmospheric_co2_data_http_error` function in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py) to test for handling of `requests.exceptions.HTTPError` exceptions.

- All tests pass.

---

### :notebook: 7/25/22

- Removed the `mock_api_request_date_error` `pytest` fixture from [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py).
    - Refactored the `mock_api_request` `pytest` fixture to support an invalid date string test, triggered by setting the `date_error` parameter to `True`.
    - Refactored the `test_convert_date_string_error` function to pass `date_error=True` to `mock_api_request` (`_mock_api_request`).

- Added test code to the function `test_transpose_data_for_graphing` in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py).
    - Updated the `_get_co2_ppm_date_data` method to support passing a set of test data to `transpose_data_for_graphing` in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

- All tests pass.

---

### :notebook: 7/26/22

- Added a `namedtuple` object to [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) as a way to reference tuple values by property name instead of tuple index:

    ```python
    from collections import namedtuple

    TransposedData = namedtuple(
        typename='TransposedData',
        field_names=[
            'date',
            'co2_ppm'
        ]
    )
    ```

- Unsuccessfully tested converting a converting a two-tuple of tuples to dict key/value pairs to support a `List` or `Tuple` object as an argument for the `data` parameter in `transpose_data_for_graphing` in the file [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
    - Further testing required.

---

### :notebook: 7/28/22

- Revised the List/Tuple input option for the `transpose_data_for_graphing` in  in the file [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to work convert a list of two tuples into dictionary keys/values:

    ```python
    # Original data
    MOCK_CO2_DATE_DATA_2 = [
        (
            datetime(1958, 3, 1, 0, 0),
            datetime(1958, 4, 1, 0, 0),
            datetime(1958, 5, 1, 0, 0)
        ),
        (
            315.7, 317.45, 317.51
        )
    ]

    # Use this code to convert the list of tuples to dict keys/values
    data_zip = zip(
        MOCK_CO2_DATE_DATA_2[0],
        MOCK_CO2_DATE_DATA_2[1]
    )

    data_dict = dict(data_zip)

    # Resulting data
    print(data_dict)

    {datetime.datetime(1958, 3, 1, 0, 0): 315.7,
    datetime.datetime(1958, 4, 1, 0, 0): 317.45,
    datetime.datetime(1958, 5, 1, 0, 0): 317.51}
    ```

- All tests pass.

---

### :notebook: 7/29/22

- Updated [`.github/workflows/pytest.yml`](https://github.com/timothyhull/climate-data-plotly/blob/main/.github/workflows/pytest.yml) to include `setup-python` GitHub Action.
    - Corrects a `pytest` failure caused by an older version of `pytest` running in GitHub's cloud-hosted runner.

- Expanded the `assert` statement in `test_transpose_data_for_graphing` function in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py).

- Refactored [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) for reuse, to create additional graphs with the same methods:
    - Revised the `TransposedData` `namedtuple` object field names to support both PPM and YOY (or other) data sets.
    - Revised the docstrings in the `_get_co2_ppm_date_data` and `_get_co2_yoy_change_data` methods.
    - Revised the conditional checks for instances of `list` objects passed as an argument to the `atmospheric_co2_data` parameter in the `_get_co2_ppm_date_data` and `_get_co2_yoy_change_data` methods.
    - Revised the parameter names in the `plot_atmospheric_co2_data` method to match the `TransposedData` object's field name revisions.

- Revised [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py) to support additional test cases and data sets.
    - Added and revised mock data constants to support using the YOY mock data with the test functions that already support the PPM mock data.
    - Revised the `test_get_atmospheric_co2_data` and `test_transpose_data_for_graphing` function to test with both PPM and YOY mock data.
    - Added the `test_get_co2_ppm_date_data` and `test_get_co2_yoy_date_data` functions to test extracting specific dictionary keys/values from Python-formatted API JSON data.

- All tests pass.

---

### :notebook: 7/30/22

- Revised the `plot_atmospheric_co2_data` function in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py):
    - Requires the `TransposedData` object as the data source (`transposed_data` parameter) for generating HTML plot content.
    - Add parameters for `date_label`, `value_label`, and `title`.

- Revised [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py) to support revisions to `plot_atmospheric_co2_data`.
    - Revised order of tests to match application flow.

---

### :notebook: 7/31/22

- Revised the `write_plot_html_file` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to support `OSError` exception handling.
- Setup initial code outline for the `test_write_plot_html_file` function.

---

### :notebook: 8/1/22

- Started development on the `test_write_plot_html_file` function in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py).
    - Requires mocking the `builtins.open` function.
    - Unsuccessfully Tested the `unittest.mock.mock_open` method using the official Python [`unittest.mock` documentation](https://docs.python.org/3/library/unittest.mock.html#mock-open).
    - Additional testing required.

---

### :notebook: 8/2/22

- Rewrote calling a mock of the `builtins.open` function in `test_write_plot_html_file`, in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - Used the `unittest.mock.patch.object` with a context manager inside of the `test_write_plot_html_file` function, instead of as a decorator.
    - Used properties and methods of the `new` argument in the `unittest.mock.patch.object`.

        ```python
            # Define HTML for a mock_open object
            mock_html_data = '''
                <html>
                    <head>
                        <title>Mock Open HTML Data</title>
                    </head>
                    <body>
                        <h1>Mock Open HTML Data</h1>
                    </body>
                </html>
            '''.strip()

            # Define a mock_open object with mock_html_data
            write_html_mock = mock_open(
                read_data=mock_html_data
            )

            # Mock the builtins.open function
            with patch.object(
                target=builtins,
                attribute='open',
                new=write_html_mock
            ):

                # Call the cd.write_plot_html_file function
                cd.write_plot_html_file(
                    file_name=MOCK_HTML_FILE_NAME.split(sep='.')[0],
                    file_content=mock_html_data
                )

            assert write_html_mock.assert_called_once
            assert MOCK_HTML_FILE_NAME in str(write_html_mock.call_args_list)
        ```

- All `pytest` tests pass.

---

### :notebook: 8/3/22

- Created the `test_write_plot_html_file_error` function in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - Tests exception handling of the `write_plot_html_file` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

- Revised the `write_plot_html_file` function in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py):
    - Changed `OSError` exceptions to `FileNotFound` exceptions.
    - Added ability to determine if `pytest` calls the function, in order to set variables that raise the `FileNotFound` exception.
    - The `os.environ` property returns a dictionary-like object.
        - When `pytest` calls a function, there will be a key value of `PYTEST_CURRENT_TEST` in the object.
        - The value of `PYTEST_CURRENT_TEST` will list the name of the `pytest` test that calls the function.
    - Conditional logic can take actions based on whether or not `pytest` called the function:

        ```python
        from os import environ, path
        from pathlib import Path
        PYTEST_ENV_VAR = 'PYTEST_CURRENT_TEST'
        PYTEST_FUNCTION = 'test_function_x'

        # Determine if pytest calls the function
        PYTEST_1 = PYTEST_ENV_VAR in str(environ.keys())
        PYTEST_2 = PYTEST_WRITE_PLOT_HTML_FUNCTION in str(environ.values())

        # If pytest calls the function, set variables to raise exceptions
        if PYTEST_1 is True and PYTEST_2 is True:
            plot_dir = ''
            plot_file = ''

        else:
            # Determine the local path to the plot file directory
            current_file = path.abspath(__file__)
            current_dir = Path(current_file).parent
            plot_dir = path.join(current_dir, PLOT_FILE_PATH)
            plot_file = path.join(
                plot_dir,
                f'{file_name}.{PLOT_FILE_EXTENSION}'
            )
        ```

- All `pytest` tests pass.

---

### :notebook: 8/4/22

- Replaced text representation of application folder and file structure with a mermaid `classDiagram` chart, in [README.md](https://github.com/timothyhull/climate-data-plotly/blob/main/README.md).

---

### :notebook: 8/5/22

- Created the `test_write_plot_html_dir_error` function in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - Tests exception handling of the `write_plot_html_file` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
    - Manually raises a `FileExistsError` exception, unable to find a way to cause the `pathlib.Path.mkdir` function fail.

- All `pytest` tests pass.

---

### :notebook: 8/6/22

- Revised [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to not manually raise an exception.
    - Set variables in the conditional logic that checks for a call to the `test_write_plot_html_dir_error` function to:
        - Create a dictionary that already exists (`../`)
        - Set the `exist_ok` parameter in `pathlib.Path.mkdir` to False.
    - With the variables present, the `write_plot_html_file` method throws a `FileExistsError` exception when called by the `test_write_plot_html_dir_error` in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py).

- Revised [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - Refactored the context manager that uses `pytest.raises` for the `test_write_plot_html_dir_error` and `test_write_plot_html_file_error` functions.
    - Added a mock `pathlib.Path.mkdir` object to the `test_write_plot_html_file` function, to prevent the function from attempting to create a new directory.

- All `pytest` tests pass.
    - 100% `pytest` coverage for [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

---

### :notebook: 8/7/22

- Experimented with Plotly Express graph types.
    - Determined the `line` and `bar` graph formats work the best for the purpose of non-financial, time-series data.

- Revised [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py):
    - Added range selector to the `plot_atmospheric_co2_data` method.
    - Added automatic plot data transposition variables (by calling the `transpose_data_for_graphing` method) to the `__init__` method.
    - Revised the `labels` argument format in the `px.line` function element of `plot_atmospheric_co2_data`.
    - Added the `x_start` parameter to set start and end date ranges (based on the first and last dates in the data set) for the range slider.

- Revised [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - Replaced static mock expected values for `pytest` tests of the `test_plot_atmospheric_co2_data` function.
    - Replaced static strings in `MOCK_HTML_PLOT_SNIPPETS` with dynamic f-string values sourced from actual test input data in `MOCK_HTML_PLOT_INPUTS`:

    ```python
    # Constant defining the test values for date_label, value_label, and title
    MOCK_HTML_PLOT_INPUTS = {
    'transposed_data': MOCK_CO2_PPM_GRAPH_DATA,
        'date_label': 'Dates',
        'value_label': 'Atmospheric Co2 PPM',
        'title': 'Atmospheric Co2 Levels',
    }

    # Old MOCK_HTML_PLOT_SNIPPETS lines
    '"Dates=%{x}<br>Atmospheric Co2 PPM=%{y}<extra></extra>"': True,
    '"title":{"text":"Atmospheric Co2 Levels"}': True,

    # New MOCK_HTML_PLOT_SNIPPETS lines
    f'"{MOCK_HTML_PLOT_INPUTS.get("date_label")}=%{{x}}<br>': True,
    f'{MOCK_HTML_PLOT_INPUTS.get("value_label")}=%{{y}}<extra></extra>"': True,
    f'"title":{{"text":"{MOCK_HTML_PLOT_INPUTS.get("title")}"}}': True,
    ```

Replaced with f-strings with vars from MOCK_HTML_PLOT_INPUT.

- All `pytest` tests pass.

---

### :notebook: 8/8/22

- Revised the `plot_atmospheric_co2_data` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py):
    - Added the ability to choose from a line or bar graph with the `line_graph` parameter.
    - Added further range customizations to the `update_yaxes`, `update_xaxes` functions.
    - Enabled optional y-axis compression with the `compress_y_axis` parameter.
        - Useful in the PPM bar graph in particular, so the y-axis doesn't start its scale at 0.
        - Instead starts the scale at 95% of the lowest value.

- Refreshed graph HTML files:
    - [ppm_bar_plot_1a.html](https://github.com/timothyhull/climate-data-plotly/blob/main/app/plot_files/ppm_bar_plot_1a.html)
    - [ppm_line_plot_1a.html](https://github.com/timothyhull/climate-data-plotly/blob/main/app/plot_files/ppm_line_plot_1a.html)
    - [yoy_bar_plot_1a.html](https://github.com/timothyhull/climate-data-plotly/blob/main/app/plot_files/yoy_bar_plot_1a.html)
    - [yoy_line_plot_1a.html](https://github.com/timothyhull/climate-data-plotly/blob/main/app/plot_files/yoy_line_plot_1a.html)

---

### :notebook: 8/9/22

- Renamed all functions, files, methods, and variables that produce plot HTML data, in order to have the ability to plot data with both Plotly Express (limited functionality) and Plotly Graph Objects (more flexible functionality):
    - Added `_px` suffix to functions and methods in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py):
        - `plot_atmospheric_co2_data_px`
    - Added `px_` prefix to variables and functions in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py):
        - `px_ppm_bar`
        - `px_ppm_line`
        - `px_yoy_bar`
        - `px_yoy_line`
        - `px_graph_all`

    - Plot files:
        - [px_ppm_bar_plot_1a.html](https://github.com/timothyhull/climate-data-plotly/blob/main/app/px_plot_files/ppm_bar_plot_1a.html)
        - [px_ppm_line_plot_1a.html](https://github.com/timothyhull/climate-data-plotly/blob/main/app/px_plot_files/ppm_line_plot_1a.html)
        - [px_yoy_bar_plot_1a.html](https://github.com/timothyhull/climate-data-plotly/blob/main/app/px_plot_files/yoy_bar_plot_1a.html)
        - [px_yoy_line_plot_1a.html](https://github.com/timothyhull/climate-data-plotly/blob/main/app/plot_files/px_yoy_line_plot_1a.html)

- Duplicated the `plot_atmospheric_co2_data_px` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) and renamed the duplicate:
        - `plot_atmospheric_co2_data_go`
        - Replaced `plotly.express` (`px`) method/function calls with `plotly.graph_objects` (`go`) methods/functions.
            - **Further development and testing necessary**
    - Added `px_` prefix to Python variables and functions in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py):
        - `plot_atmospheric_co2_data_px`

---

### :notebook: 8/10/22

- Revised the `plot_atmospheric_co2_data_go` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to use `plotly.graph_objects` objects instead of `plotly.plotly_express` objects.
    - Verified graph output is similar to that of the `plotly.plotly_express` graph output from `plot_atmospheric_co2_data_ppx`.

- All `pytest` tests pass.

---

### :notebook: 8/11/22

- Experimented with multiple graphs in one plot using both [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) and [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py):
    - The two data sets, monthly Co2 PPM and +/- % of monthly YoY Co2 delta, have vastly different x-axis ranges, so [Plotly Subplots (multiple stacked plots with a shared axis](https://plotly.com/python/subplots/#subplots-with-shared-xaxes) is the best candidate to display the two data sets adjacently.
    - Saved test files to the local `_gitignore` directory.

- Minor variable/constant and functional updates to both [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) and [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py).

---

### :notebook: 8/12/22

- Started refactoring the `plot_atmospheric_co2_data_px` and `plot_atmospheric_co2_data_go` methods in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
    - Reduced the number of parameters in each function by creating and passing a `typing.NamedTuple` object of the custom class `PlotProperties` with several individual properties.
        - A `typing.NamedTuple` object is equivalent to a `collections.namedtuple` object and also allows for type hints and default values in field names.
        - Increased the Better Code Hub score from **6/10** to **7/10**.
        - Now passing the _Keep Unit Interfaces Small_ test.

            ```python
            # Import the typing.NamedTuple class
            from typing import NamedTuple

            # Constants
            PLOT_DATE_LABEL = 'Dates'
            PLOT_VALUE_LABEL = 'Values'
            PLOT_TITLE = 'Atmospheric Co2 Data'

            # NamedTuple object
            class PlotProperties(NamedTuple):
                """ Properties for formatting a graphed plot.

                    Typed version of the collections.namedtuple object with
                    field names and default values.

                    Field Names and Default Values:

                        line_graph (bool, optional):
                            Specifies whether the plot will be a line graph
                            or not.  When True, the plot will be a line graph.
                            When False, the plot will be a bar graph.  Default
                            is True.

                        date_label (str, optional):
                            Label of plot y-axis.  Default is PLOT_DATE_LABEL.

                        value_label (str, optional):
                            Label of plot y-axis.  Default is PLOT_VALUE_LABEL.

                        title (str, optional):
                            Title of plot. Default is PLOT_TITLE.

                        compress_y_axis (str, optional):
                            Determine whether the y-axis starts at 0, which
                            displays well with PPM data although poorly with
                            YOY data.  When True, compresses the y-axis range
                            to 95% of the first value of the y-axis data,
                            and 100.5% of the last value in the y-axis data.
                            Default is False.
                """

                # Field names and default values
                line_graph: bool = True,
                date_label: str = PLOT_DATE_LABEL,
                value_label: str = PLOT_VALUE_LABEL,
                title: str = PLOT_TITLE,
                compress_y_axis: bool = False
            ```

- Refactored functions in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) to support passing arguments to the  `plot_atmospheric_co2_data_px` and `plot_atmospheric_co2_data_go` methods in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) as `PlotProperties`object instances.

- Refactored [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py) to support passing arguments to the  `plot_atmospheric_co2_data_px` and `plot_atmospheric_co2_data_go` methods in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) as `PlotProperties`object instances.
    - Renamed the test function `test_plot_atmospheric_co2_data` to `test_plot_atmospheric_co2_data_px` and updated call to the `ClimateData.plot_atmospheric_co2_data_px` method to send a `PlotProperties` object as an argument.
    - Created the test function `test_plot_atmospheric_co2_data_go` to call the `ClimateData.plot_atmospheric_co2_data_go` method with `PlotProperties` object as an argument.

- All `pytest` tests pass.

---

### :notebook: 8/13/22

- Refactored [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to reduce the number of lines of code in the `plot_atmospheric_co2_data_px` method and improve the compliance score with Better Code Hub.
    - Added the following methods:
        - `setup_graph_args`
        - `update_graph_x_axis`
        - `compress_y_axis`
        - `update_graph_y_axis`
    - Relocated code from `plot_atmospheric_co2_data_px` to the new methods.
    - Improved score from **6/10** to **7/10**.

- Revised elements in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py):
    - Relocated TransposedData object definition to be adjacent to the `PlotProperties` `NamedTuple` object.
    - Revised spelling for the plural of axis to axes.

- Refactored the setup of the `PlotProperties` object in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) to support setting the `compress_y_axis` value on a per-function basis:
    - Relocated the `compress_y_access` from `PPM_PLOT_PROPERTIES` and `GO_PLOT_PROPERTIES` to individual functions.
    - Adjusted values for the `compress_y_access` value on a per-function basis.
    - Removed instances of `line_graph` arguments in the `go_yoy_bar` and `go_yoy_line` functions.

- All `pytest` tests pass.

---

### :notebook: 8/14/22

- Refactored [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) for reusability to improve the Better Code Hub **Write Code Once** and **Write Short Units of Code** scores.
    - Reduced calls to `plot_atmospheric_co2_data_px` and `plot_atmospheric_co2_data_px` from four each to once each.
    - Removed `px_graph_all` and `go_graph_all` from the list of Better Code Hub warnings, previously having 26 lines of code for each of these functions.
    - Improved BCH score from **7/10** to **8/10**.

- All `pytest` tests pass.

---

### :notebook: 8/15/22

- Refactored [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to reduce the number of lines of code in the `plot_atmospheric_co2_data_go` method and improve the compliance score with Better Code Hub.
    - Added the following methods:
        - `setup_layout_args`
        - `setup_graph_args_go`
        - `setup_graph_args_px` (renamed `setup_graph_args_px`)
            - Split functions due to the different graph arguments required for `plotly.express` and `plotly.graph_objects` plot objects.
    - Relocated code from `plot_atmospheric_co2_data_go` to the new methods.

- BCH score declined from **8/10** to **7/10**:
    - Need to refactor `plot_atmospheric_co2_data_px` and `plot_atmospheric_co2_data_go` to reduce duplicate code instances.

- Corrected variable name in the `plot_px_yoy_line` function in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py).

- All `pytest` tests pass.

---

### :notebook: 8/16/22

- Refactored [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) to reduce the number of repetitive constants, and to make constants more modular:
    - The refactor did not reduce the number of lines of code, as intended.
    - BCH score remains **7/10**:

- All `pytest` tests pass.

---

### :notebook: 8/17/22

- Refactored [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to combine the `plot_atmospheric_co2_data_px` and `plot_atmospheric_co2_data_go` into a single method `plot_atmospheric_co2_data_px`.
    - Reduced number of lines of code and instances of duplicate code.

- Refactored [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py):
    - Consolidated `px_plot` and `go_plot` functions to the `plot_graph` function.
    - Set `plot_graph` to a single method `ClimateData.plot_atmospheric_co2_data`
    - Updated `_PLOT_PROPERTIES` constants to include the `px_plot` key/value pair.
    - Reduced number of lines of code and instances of duplicate code.
    - BCH score...

- Refactored `pytest` tests in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py) to support the consolidated `ClimateData.plot_atmospheric_co2_data` method.
    - Updated `MOCK_HTML_PLOT_PROPERTIES_` constants to include the `px_plot` argument.

- Improved BCH score from **7/10** to **8/10**:
    - Now passing the **Write Code Once** standard.

- All `pytest` tests pass.

---

### :notebook: 8/18/22

- Refactored [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py), functionally decomposing the `plot_atmospheric_co2_data` method:
    - Moved code to the new methods `_plot_graph_px` and `_plot_graph_go`

- No change BCH score (**8/10**):
    - Reduced `plot_atmospheric_co2_data` method from 53 to 27 lines.
    - `plot_atmospheric_co2_data` now scored as yellow (more than 15 lines of code) instead of orange (more than 30 lines of code).

- All `pytest` tests pass.

---

### :notebook: 8/19/22

- Refactored [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py), functionally decomposing the `write_plot_html_file` method:
    - Moved code to the new methods `_set_plot_file_path`, `_create_plot_dir` and `_create_plot_file`.

- Improved BCH score from **8/10** to **9/10**:
    - Now passing the **Write Short Units of Code** standard.

- All `pytest` tests pass.

---

### :notebook: 8/20/22

- Refactored the file [web/flask_app.py](https://github.com/timothyhull/climate-data-plotly/blob/main/web/flask_app.py) to import the `app` folder directly, instead of importing the `ClimateData` class directly:
    - Researched the **Abstract Factory** design pattern to improve the BCH score.
        - Learned that by importing `app.ClimateData.ClimateData` directly caused the code to fail the **Couple Architecture Components Loosely** test.
            - This creates a "tight coupling" of code, because [web/flask_app.py](https://github.com/timothyhull/climate-data-plotly/blob/main/web/flask_app.py) cannot access other modules in the `app` folder.
        - Importing the `app` folder directly instead creates a "loose coupling" of code, because importing the `app` folder allows the flexibility to access all of its sub-components

            ```python
            # Initial, non-abstract factory method
            from app.ClimateData import ClimateData

            # Updated, abstract factory method
            import app

            # Because the Flask app variable in my file is 'app', I renamed the 'app' import
            import app as app_climate
            ```

    \*\*\* 9/3/22 update: `import.app` did not allow access to any submodules in the `app` folder, further **abstract factory** research required. \*\*\*

- Improved BCH score from **9/10** to **10/10**:
    - Now passing the **Couple Architecture Components Loosely** standard.

- All `pytest` tests pass.

---

### :notebook: 8/21/22

- Created the `test_compress_y_axis` function in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - Tests the `_compress_y_axis` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

- All `pytest` tests pass.
- `pytest` coverage at 98%.

```bash
\# pytest --cov-report=term-missing --cov=.
=================================================================== test session starts ====================================================================
platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
rootdir: /workspaces/climate-data-plotly
plugins: requests-mock-1.9.3, cov-3.0.0
collected 39 items                                                                                                                                         

tests/test_ClimateData.py .......................................                                                                                    [100%]

---------- coverage: platform linux, python 3.10.5-final-0 -----------
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
app/ClimateData.py            168      3    98%   756, 853, 1113
tests/test_ClimateData.py     131      1    99%   517
---------------------------------------------------------
TOTAL                         299      4    99%


==================================================================== 39 passed in 1.86s ====================================================================
```

---

### :notebook: 8/22/22

- Refactored [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py), functionally decomposing the `_create_graph_px` and `create_graph_go` methods:
    - Renamed methods from `_create_plot_px` and `_create_plot_go` respectively.
    - Created and moved code to methods `_plot_px` and `plot_go` to exclusively call and return `plotly.express` and `plotly.graph_objects` respectively.
        - This allows `pytest` to explicitly test the return values of `px.bar`, `px.line`, `go.Scatter`, and `go.Bar`.

- Created the `test_plot_px` and `test_plot_go` functions in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py):
    - Tests the `_plot_px` and `_plot_go` methods in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

- All `pytest` tests pass.
- `pytest` coverage at 98%.
    - `pytest` does not recognize the new test functions as resolutions to the 2 x lines of code shown as not-covered in the `pytest` coverage report:

        ```python
        graph = px.line(
            **graph_args,
            markers=True
        )

        graph.add_trace(
            go.Scatter(**graph_args)
        )
        ```

- Maintained BCH score of **10/10**.

- All `pytest` tests pass.

---

### :notebook: 8/23/22

- Created `pytest` file, [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py).
    - Created test function `test_main` to test the `main` function in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py).

- Maintained BCH score of **10/10**.

- All `pytest` tests pass.
    - Coverage report for [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py) is 35%.
    - Total coverage is 86%.

        ```bash
        root@97d9e35a0c55:/workspaces/climate-data-plotly# pytest --cov-report=term-missing --cov=.
        =================================================== test session starts ====================================================
        platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
        rootdir: /workspaces/climate-data-plotly
        plugins: requests-mock-1.9.3, cov-3.0.0
        collected 42 items                                                                                                         

        tests/test_ClimateData.py .........................................                                                  [ 97%]
        tests/test_climate_data.py .                                                                                         [100%]

        ---------- coverage: platform linux, python 3.10.5-final-0 -----------
        Name                         Stmts   Miss  Cover   Missing
        ----------------------------------------------------------
        app/ClimateData.py             174      3    98%   743, 822, 1250
        app/climate_data.py             85     55    35%   78-92, 109-123, 142-156, 175-189, 208-222, 241-255, 274-288, 307-321, 340-354, 368-387, 401-420, 441
        tests/test_ClimateData.py      146      1    99%   542
        tests/test_climate_data.py      25      0   100%
        ----------------------------------------------------------
        TOTAL                          430     59    86%


        ==================================================== 42 passed in 2.18s ====================================================
        ```

- Added missing `return None` statements to [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py).

---

### :notebook: 8/24/22

- Added the `climate_data` parameter to the `plot_graph` function in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) to require an instance of the `ClimateData.ClimateData` class.
    - Enables importing and calling functions in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) from other Python files.
        - Enables using `pytest` to send a mock instance of the `ClimateData.ClimateData` class to the `plot_graph` function.
    - Updated calls to the `plot_graph` function to send an instance of the `ClimateData.ClimateData` class as an argument to the `climate_data` parameter.

- Added `pytest` fixtures and tests to [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py):
    - Added the `pytest` fixture `mock_climate_data_main` to create a reusable interface that generates a mock instance of the `ClimateData.ClimateData` class returned by the `main` function in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py).
        - Added the `mock_climate_data_main` fixture to the `test_main` and `test_plot_graph` functions.

- Refactor needs:
    - [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py):
        - [X] Use constants in the `plot_graph` function's `print` statement.
    - [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py):
    - [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py):
        - [X] Check to see if the expected file creates successfully in `write_plot_html_file` and return a `bool` object.
            - The return value for the `open` function with a `wt` mode is a count of characters written to a new file.
    - [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py):
        - [X] Use constants in the `test_plot_graph` function.
        - [X] Use `pytest.mark.parameterize` to send multiple test data sets to the `plot_graph` function.
        - [X] Use a mock of the `file.open` method to prevent the `test__plot_graph` function from creating a new plot HTML file.

- BCH score dropped from **10/10** to **9/10**.
    - Failing the **Write Code Once** check.
    - [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) requires refactoring to reduce 4 x instances of:

        ```python
        plot_graph(
            transposed_data=climate_data.transposed_co2_ppm_date_data,
            plot_properties=plot_properties,
            climate_data=climate_data
        )

        # Display a success message
        print(
            f'\nGenerated the file {PX_PREFIX}{BAR_PPM_FILE_NAME}{FILE_SUFFIX}\n'
        )
        ```  

- All `pytest` tests pass.
    - Coverage report for [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py) is 42%, up from 35%.
    - Total coverage is 88%, up from 86%.

---

### :notebook: 8/25/22

- Refactored [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) to improve BCH score.
    - Renamed the `plot_graph` function to be an internal use function, `_plot_graph`.
    - Created a new, callable `plot_graph` function that calls the `_plot_graph` with arguments and a print statement that were common across 8 x functions:
        - `plot_px_ppm_bar`
        - `plot_px_ppm_line`
        - `plot_px_yoy_bar`
        - `plot_px_yoy_line`
        - `plot_go_ppm_bar`
        - `plot_go_ppm_line`
        - `plot_go_yoy_bar`
        - `plot_go_yoy_line`

        ```python
        # Generate a PPM bar graph
        plot_status = _plot_graph(
            plot_properties=plot_properties,
            climate_data=climate_data
        )

        # Display a success message
        print(
            f'\nGenerated the file {PX_PREFIX}{BAR_PPM_FILE_NAME}{FILE_SUFFIX}\n'
        )
        ```

    - BCH score remains at **9/10**.
        - Further refactoring to reduce repetitive code required.

    - Added the `_create_ppm_plot_properties` and `_create_yoy_plot_properties` functions to reduce duplicate code.
    - Reduced calls to the `plot_graph` function from 6 lines to 1:

        ```python
        # Original plot_graph call
        plot_graph(
            climate_data=climate_data,
            plot_properties=plot_properties
        )

        # Revised plot_graph call
        plot_graph(climate_data=climate_data, plot_properties=plot_properties)
        ```

- Improved BCH score from **9/10** to **10/10**:
    - Now passing the **Write Code Once** check.

- All `pytest` tests pass.
    - Coverage report for [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py) is 49%, up from 42%.
    - Total coverage is 90%, up from 88%.

---

### :notebook: 8/26/22

- Refactored the `_create_plot_file` and `write_plot_html_file` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to return a value:
    - Returns the value returned by the `open()` function, which is an `int` value equivalent to the number of characters written to a new file, when the `mode` argument is `wt`.

- Refactored `test_write_plot_html_file` function in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py) to account for new return value in the `ClimateData.write_plot_html_file` method:
    - Added check for match between mock file input and mock file output.
    - Getting the mock file output value required digging into the value assigned to `write_html_mock` created by the built-in `mock_open()` function:

        ```python
        # Get the attributes and methods of write_html_mock
        print({dir(write_html_mock)})

        # Found the mock file output value in the write_html_mock.mock_calls attribute
        print({write_html_mock.mock_calls})

        # Extracted the mock file output from the call_list method of list item number 2
        mock_write_value = write_html_mock.mock_calls[2].call_list()[0]

        # Converted the mock file output value to a string
        mock_write_value = str(mock_write_value)

        # Extracted the file contents with the split method, collecting list item 1 from the result
        mock_write_value = mock_write_value.split(sep="'")[1]

        # Compared the mock file input value with the mock file output value
        assert mock_file_input_string == mock_write_value
        ```

- Maintained BCH score of **10/10**.

- All `pytest` tests pass.

---

### :notebook: 8/27/22

- Refactor _create_plot_file to return two values.
The path to the plot file.
The number of characters written to a new plot file.

- Add new functions to validate new plot generation.
_validate_new_plot
_print_plot_result

Replaced text variables with text constants

- Updated `test_write_plot_html_file` function in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData) to support returning values that allow determination of whether or not a plot file write is successful:
    - Refactored the `_create_plot_file` method to return two values:
        - The path to the plot file.
        - The number of characters written to a new plot file.

- Refactored `test_write_plot_html_file` function in [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py) to account for new return value in the `ClimateData.write_plot_html_file` method:
    - Added check for match between mock file input and mock file output.

- Refactored [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) to support determining if a plot file write is successful or not:
    - Add new functions to validate new plot generation.
        - `_validate_new_plot`
        - `_print_plot_result`

- Maintained BCH score of **10/10**.

- All `pytest` tests pass.

---

### :notebook: 8/28/22

- Refactored [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) to use constants with variable substitution for printing:
    - Set constants with placeholders and used the `str.format` method to display final values:

    ```python
    # Set constant with placeholders
    PLOT_RESULT_STR = '\nCreated the {} graph "{}"\n'

    # Print statement with the str.format method to substitute variables
    print(PLOT_RESULT_STR.format(graph_type, plot_properties.title))
    ```

- Refactored [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py) to:
    - Test the `plot_graph` function directly, instead of the `_plot_graph` function.
        - `_plot_graph` calls `plot_graph`, so both functions get tested by testing `plot_graph`
    - Use the `mock_open` function, in order to prevent the test function `test_plot_graph` from creating a new HTML file when calling `plot_graph`.
    - Updated assertions to properly test for valid results.

- Maintained BCH score of **10/10**.

- All `pytest` tests pass.
    - Coverage report for [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py) is 61%, up from 49%.
    - Total coverage is 91%, up from 90%.

        ```bash
        \# pytest --cov-report=term-missing --cov=.
        =================================================== test session starts ====================================================
        platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
        rootdir: /workspaces/climate-data-plotly
        plugins: requests-mock-1.9.3, cov-3.0.0
        collected 43 items                                                                                                         

        tests/test_ClimateData.py .........................................                                                  [ 95%]
        tests/test_climate_data.py ..                                                                                        [100%]

        ---------- coverage: platform linux, python 3.10.5-final-0 -----------
        Name                         Stmts   Miss  Cover   Missing
        ----------------------------------------------------------
        app/ClimateData.py             174      2    99%   743, 822
        app/climate_data.py            104     41    61%   160, 193-200, 225-232, 266, 313-321, 340-348, 367-375, 394-402, 421-429, 448-456, 475-483, 502-510, 524-543, 557-576, 597
        tests/test_ClimateData.py      151      1    99%   542
        tests/test_climate_data.py      46      0   100%
        ----------------------------------------------------------
        TOTAL                          475     44    91%


        ==================================================== 43 passed in 1.98s ====================================================
        ```

---

### :notebook: 8/30/22

- Refactored the `_create_ppm_plot_properties` function in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py) to include a `climate_data` parameter for a `ClimateData` object.
    - Without this parameter, the function cannot be called from outside the `__main__` context (in this case for testing), because the function previously relied on the `main` function creating a climate_data object.
    - Added an argument to the `_create_ppm_plot_properties` function call in `plot_px_ppm_bar`.

- Added `pytest.mark.parameterize` to the `test_plot_graph` function in [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py).
    - `test_plot_data` now tests multiple test data sets at once.
    - Created constants to support the parameterized calls to `test_plot_graph`.

- Created the function `test_plot_px_ppm_bar` in [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py), to test the `plot_px_ppm_bar` function in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py).

- Maintained BCH score of **10/10**.

- All `pytest` tests pass.
    - Coverage report for [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py) is 65%, up from 61%.
    - Total coverage is 92%, up from 91%.

---

### :notebook: 8/31/22

- Added the following tests to [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py), to test functions in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py):
    - `test_plot_px_ppm_line`
    - `test_plot_px_yoy_bar`
    - `test_plot_px_yoy_line`
    - `test_plot_go_ppm_bar`
    - `test_plot_go_ppm_line`
    - `test_plot_go_yoy_bar`
    - `test_plot_go_yoy_line`

- Added the `graph_all` function to [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py), to graph all plots with a single function call.

- Maintained BCH score of **10/10**.

- All `pytest` tests pass.
    - Coverage report for [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py) is 86%, up from 61%.
    - Total coverage is 97%, up from 92%.

        ```bash
        \# pytest --cov-report=term-missing --cov=.
        ============================================================================ test session starts ============================================================================
        platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
        rootdir: /workspaces/climate-data-plotly
        plugins: requests-mock-1.9.3, cov-3.0.0
        collected 52 items                                                                                                                                                          

        tests/test_ClimateData.py .........................................                                                                                                   [ 78%]
        tests/test_climate_data.py ...........                                                                                                                                [100%]

        ============================================================================ 52 passed in 1.18s =============================================================================
        root@97d9e35a0c55:/workspaces/climate-data-plotly# 
        root@97d9e35a0c55:/workspaces/climate-data-plotly# 
        root@97d9e35a0c55:/workspaces/climate-data-plotly# pytest --cov-report=term-missing --cov=.
        ============================================================================ test session starts ============================================================================
        platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
        rootdir: /workspaces/climate-data-plotly
        plugins: requests-mock-1.9.3, cov-3.0.0
        collected 52 items                                                                                                                                                          

        tests/test_ClimateData.py .........................................                                                                                                   [ 78%]
        tests/test_climate_data.py ...........                                                                                                                                [100%]

        ---------- coverage: platform linux, python 3.10.5-final-0 -----------
        Name                         Stmts   Miss  Cover   Missing
        ----------------------------------------------------------
        app/ClimateData.py             174      1    99%   743
        app/climate_data.py            107     15    86%   160, 274, 540-559, 573-592, 606-609, 630
        tests/test_ClimateData.py      151      1    99%   542
        tests/test_climate_data.py     113      0   100%
        ----------------------------------------------------------
        TOTAL                          545     17    97%


        ============================================================================ 52 passed in 2.09s =============================================================================
        ```

---

### :notebook: 9/1/22

- Added the following tests to [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py), to test functions in [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py):
    - `test_px_graph_all`
    - `test_go_graph_all`
    - `test_graph_all`

- Revised [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py):
    - Added the keyword argument `climate_data` to the following functions, to support `pytest` testing and code usage from modules that import [app/climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/climate_data.py):
        - `px_graph_all`
        - `go_graph_all`
        - `graph_all`

- Maintained BCH score of **10/10**.

- All `pytest` tests pass.
    - Coverage report for [tests/test_climate_data.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_climate_data.py) is 97%, up from 86%.
    - Total coverage is 99%, up from 97%.

        ```bash
        \# pytest --cov-report=term-missing --cov=.
        =========================================== test session starts ===========================================
        platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
        rootdir: /workspaces/climate-data-plotly
        plugins: requests-mock-1.9.3, cov-3.0.0
        collected 55 items                                                                                        

        tests/test_ClimateData.py .........................................                                 [ 74%]
        tests/test_climate_data.py ..............                                                           [100%]

        ---------- coverage: platform linux, python 3.10.5-final-0 -----------
        Name                         Stmts   Miss  Cover   Missing
        ----------------------------------------------------------
        app/ClimateData.py             174      1    99%   743
        app/climate_data.py            107      3    97%   160, 274, 640
        tests/test_ClimateData.py      151      1    99%   542
        tests/test_climate_data.py     143      0   100%
        ----------------------------------------------------------
        TOTAL                          575      5    99%


        =========================================== 55 passed in 2.55s ============================================
        ```

---

### :notebook: 9/2/22

- Added initial graph display to [web/flask_app.py](https://github.com/timothyhull/climate-data-plotly/blob/main/web/flask_app.py).

- BCH score fell to **9/10**.
    - **Couple Architecture Components Loosely** failing due to change in the `import` instruction.

- All `pytest` tests pass.

---

### :notebook: 9/3/22

- Reviewed and tested abstract factory design pattern to resolve BCH **Couple Architecture Components Loosely** test failure.

---

### :notebook: 9/4/22

- Refactored to support abstract factory design pattern:
    - Repurposed the `ClimateData` class in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) as an abstract factory class.
    - Renamed the `ClimateData` class to `AtmosphericCo2PPM` in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) as a concrete factory class of the `ClimateData` class.
    - Renamed all instances of `ClimateData` to `AtmosphericCo2PPM` in the [climate-data-plotly](https://github.com/timothyhull/climate-data-plotly).

- BCH score remains **9/10**.
    - **Couple Architecture Components Loosely** failing.
    - Further abstract factory design refactoring required.

- All `pytest` tests pass.

---

### :notebook: 9/5/22

- Refactored to support abstract factory design pattern:
    - Changed the `TransposedData` `namedtuple` object to a `NamedTuple` object with type hints in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
        - Updated import statements across all repo files to reflect new path to `TransposedData` object (`app.ClimateData.AtmosphericCo2PPM.TransposedData`).
    - Moved the `PlotProperties` `NamedTuple` object to the `AtmosphericCo2PPM` class in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
        - Updated import statements across all repo files to reflect new path to `PlotProperties` object (`app.ClimateData.AtmosphericCo2PPM.PlotProperties`).
    - Updated import statements across all repo files import the `AtmosphericCo2PPM` class with an alias for brevity.

        ```python
        # Revised import statement
        from app.ClimateData import AtmosphericCo2PPM as APP

        # Usage
        climate_data = APP()
        ```

- BCH score remains **9/10**.
    - **Couple Architecture Components Loosely** failing.
    - Further abstract factory design refactoring required.

- All `pytest` tests pass.

---

### :notebook: 9/7/22

- Refactored to support abstract factory design pattern:
    - Moved the `TransposedData` and `PlotProperties` objects to a new, concrete factory class (`CustomObjs`) in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
        - The `CustomObjs` class inherits the `ClimateData` class.
        - The `AtmosphericCo2PPM` class inherits the `CustomObjs` class.

---

### :notebook: 9/8/22

- Experimented with mechanisms to find the count of code lines in a Python file, to help understand the meaning of the output from the BCH **Couple Architecture Components Loosely** report, showing 404 lines of **interface code**.
    - The best counting mechanism I found is [`pygount`](https://pypi.org/project/pygount/):

        ```bash
        # Command input
        pygount app/ClimateData.py --format=summary
        ```

        ```bash
        # Command output
        ┏━━━━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━┓
        ┃ Language ┃ Files ┃     % ┃ Code ┃    % ┃ Comment ┃    % ┃
        ┡━━━━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━┩
        │ Python   │     1 │ 100.0 │  351 │ 25.8 │     810 │ 59.4 │
        ├──────────┼───────┼───────┼──────┼──────┼─────────┼──────┤
        │ Sum      │     1 │ 100.0 │  351 │ 25.8 │     810 │ 59.4 │
        └──────────┴───────┴───────┴──────┴──────┴─────────┴──────┘
        ```

- The meaning of **interface code** requires further research, still.

---

### :notebook: 9/9/22

- Reviewed [Python abstract factory example](https://stackabuse.com/abstract-factory-design-pattern-in-python).
    - Tested the code within the article locally, to determine if it produces the expected result.
        - Local testing is successful.
    - Started process to document the class and method architecture in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) in order to refactor in an abstract factory design pattern.

---

### :notebook: 9/10/22

- Continued development of [refactoring diagram](https://lucid.app/lucidchart/ddab7221-4851-4311-af0b-08273a7439d4/edit?beaconFlowId=CA13137AA43FDDD1&invitationId=inv_f3a1d044-5254-493b-b91e-7cad8618f700&page=0_0#) for [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

---

### :notebook: 9/11/22

- Continued development of [refactoring diagram](https://lucid.app/lucidchart/ddab7221-4851-4311-af0b-08273a7439d4/edit?beaconFlowId=CA13137AA43FDDD1&invitationId=inv_f3a1d044-5254-493b-b91e-7cad8618f700&page=0_0#) for [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

---

### :notebook: 9/12/22

- Continued development of [refactoring diagram](https://lucid.app/lucidchart/ddab7221-4851-4311-af0b-08273a7439d4/edit?beaconFlowId=CA13137AA43FDDD1&invitationId=inv_f3a1d044-5254-493b-b91e-7cad8618f700&page=0_0#) for [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

- Created new file ([app/ClimateData_2.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData_2.py)) for abstract factory design pattern testing only.

---

### :notebook: 9/13/22

- Continued development of [refactoring diagram](https://lucid.app/lucidchart/ddab7221-4851-4311-af0b-08273a7439d4/edit?beaconFlowId=CA13137AA43FDDD1&invitationId=inv_f3a1d044-5254-493b-b91e-7cad8618f700&page=0_0#) for [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
    - Build base layout diagram for:
        - Abstract factory class (`ClimateData`).
        - Abstract product \#1 (`PXPlot`).
        - Abstract product \#2 (`GOPlot`).
        - Concrete factory class (`ClimatePlot`).
        - Concrete product class (`AtmosphericCO2PPMPlot`).

---

### :notebook: 9/14/22

- Continued development of [refactoring diagram](https://lucid.app/lucidchart/ddab7221-4851-4311-af0b-08273a7439d4/edit?beaconFlowId=CA13137AA43FDDD1&invitationId=inv_f3a1d044-5254-493b-b91e-7cad8618f700&page=0_0#) for [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

---

### :notebook: 9/16/22

- Reviewed YouTube video overview of the abstract factory design pattern, in an attempt to understand how to refactor the application properly.
    - Still unclear how to refactor the climate application.
    - Further research and testing required.

---

### :notebook: 9/17/22

- Re-reviewed the first portion of the YouTube video overview for the abstract factory design pattern.
    - Started testing in a new, simplified Python file (`abs_3a.py`), versus refactoring the climate application.

---

### :notebook: 9/18/22

- Reviewed and refactored simplified Python file (`abs_3b.py`) although the revisions do not result in functional code.

---

### :notebook: 9/19/22

- Reviewed and refactored simplified Python file (`abs_3b.py`) and produced the expected output.
    - Next step is to write a new file with an abstract factory design pattern framework and test.

---

### :notebook: 9/20/22

- Created new file (`abs_4.py`) for abstract factory design pattern testing.
    - Created the following classes:
        - `ITProvisioner` Abstract factory
        - `Server` Abstract product 1
        - `NetDevice` Abstract product 2
        - `CreateServer` Concrete product 1
        - `CreateNetDevice` Concrete product 2
        - `NewServer` Concrete factory 1
        - `NewNetDevice` Concrete factory 2

    - Preliminary testing results in expected behavior.
    - Requires further testing to ensure the design structure is correct.

---

### :notebook: 9/22/22

- Created new file (`abs_5.py`) for abstract factory design pattern testing.
    - Created the following classes:
        - `ServiceCatalog` Abstract factory
        - `Mobile` Abstract product 1
        - `Laptop` Abstract product 2
        - `ATTPhoneServices` Concrete product 1
        - `MacBookProServices` Concrete product 2
        - `ATTPhone` Concrete factory 1
        - `MacBookPro` Concrete factory 2

    - Preliminary testing results in expected behavior.
    - Requires further testing to ensure the design structure is correct.

---

### :notebook: 9/26/22

- The Factory Design Pattern separates object _creation_ from object _usage_.
- Without using this pattern, a function may have "weak/low cohesion", because it may do too many different things:

    1. Collect user input.
    2. Create objects from established classes (creation).
    3. Run methods of the created objects (usage)

- Relocated abstract factory test files from the `climate-data-plotly` repo to the `100DaysOfCode` repository [`days/_83_84/abstract_factory`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/abstract_factory).

---

### :notebook: 10/1/22

- Continued review of Abstract Factory Design Pattern YouTube video, and updated the file [`days/_83_84/abstract_factory/video_exporter.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/abstract_factory/video_exporter.py):
    - Partially refactored file to support **Concrete Factory** classes.
    - Need to add code to the `main_2` function, to test the updates.

---

### :notebook: 10/2/22

- Continued review of Abstract Factory Design Pattern YouTube video, and updated the file [`days/_83_84/abstract_factory/video_exporter.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/abstract_factory/video_exporter.py):
    - Updated and tested the `main_2` function, which works as expected.

---

### :notebook: 10/3/22

- Continued review of Abstract Factory Design Pattern YouTube video, and updated the file [`days/_83_84/abstract_factory/video_exporter.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/abstract_factory/video_exporter.py):
    - Added and tested the 'main_3'function:
        - Decouples object creation from usage by passing an abstract subclass object as an argument to 'main_3'.

---

### :notebook: 10/4/22

- Factory design patterns separate the _creation_ of objects from the _use_ of objects.
    - This provides flexibility to make code changes to class functions/methods and features, because it keeps developers that consume class objects from having to update their interface code (the code that accesses and runs class objects) when changes to class objects occur.
    - This is possible because the classes that typical functions consume (usage from another Python file) are abstract, and do not expose the sub-classes that actually create objects (creation).

- A strong point of factories is they allow the grouping of objects that belong together.  For example, different:
    - Currency options
    - Tax rates
    - Languages
    - Shipping rates

- Factories are not as useful in cases where a great number of factories are necessary, to account for different combinations of choices a user may select.
    - For example, a user exporting audio and video may want to define a custom exporter with their choices of audio and video codecs, instead of choosing a preset.
    - It is manageable for preset export settings to be concrete factory classes, although creating concrete factory classes for every possible combination of audio and video codecs may not make sense.

- Completed review of Abstract Factory Design Pattern YouTube video, and updated the file [`days/_83_84/abstract_factory/video_exporter.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/abstract_factory/video_exporter.py) to function properly.
    - The next step is to create a new factory design-patterned set of test classes.

---

### :notebook: 10/6/22

- Created [framework for mock program](https://lucid.app/lucidchart/fc6cad6d-bfa3-4446-858d-cd6502fd3a50/edit?invitationId=inv_c10b276a-7044-4dff-9304-197752bee888#) that uses the abstract factory design pattern.
    - Application will provision various virtual server types within different public cloud provider environments.

- Created [`server_maker`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/server_maker) directory, to host the application.

---

### :notebook: 10/10/22

- Created the file [`server_maker.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/server_maker/app/server_maker.py):
    - Created the `ServerMaker` **Abstract Factory** class, to represent a basic cloud server provisioning app.
        - Created the `create_server_config` **Abstract Method**, as an abstract reference for future **Concrete Product** classes that create new servers in different cloud platforms.
    - Created the `NamedTuple` object `ServerParams`, to serve as a container for server configuration data (host name, server size, etc.).

---

### :notebook: 10/20/22

Back after a nine day physical and mental health recovery period.

- Reviewed notes and previous content.
- Added new code to [`server_maker.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/server_maker/app/server_maker.py):
    - Added the `generate_server_name` function to auto-generate server names.
    - Added the `deploy_server_config` **Abstract Method**, to the `ServerMaker` **Abstract Factory** class as an abstract reference for future **Concrete Product** classes that deploy new servers in different cloud platforms.

---

### :notebook: 10/21/22

- Relocated the `generate_server_name` function to a new file, [`server_maker_helper.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/server_maker/app/server_maker_helper.py).

- Created the `AWSServer` concrete product class, to create AWS server configuration files using the abstract methods in the `ServerMaker` class.

---

### :notebook: 10/23/22

- Reviewed application design diagram.
- Reviewed abstract factory example diagram to determine how to name and classify classes.
    - Determined there should be no "Abstract Factory" class.
    - The Abstract Factory is a concept that includes the following class concepts:
        - Abstract Product
        - Concrete Factory
        - Concrete Product

---

### :notebook: 10/24/22

- Created the `AzureServer` and `GCPServer` concrete product classes, to create AWS server configuration files using the abstract methods in the `ServerMaker` class.
- Updated application design diagram to reflect new class structure.
    - Still working to understand the relationship between the abstract and concrete classes.

---

### :notebook: 10/25/22

- Revised classes in [`server_maker.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/server_maker/app/server_maker.py) to align more closely with [`days/_83_84/abstract_factory/video_exporter.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/abstract_factory/video_exporter.py).

---

### :notebook: 10/27/22

- Paused development of server maker application to study the abstract factory design pattern in more detail.
    - Started Pluralsight course to learn abstract factory design details:
    - Completed section 1,
    - Completed lessons 1-3 in section 2.

---

### :notebook: 11/3/22

- Continued Pluralsight design patterns course:
    - Completed section 2.
    - Created the file [`my_abstract_class.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/introduction/my_abstract_class.py) to practice creating a simple interface (Abstract Base Class), and implementation (Concrete Class).

---

### :notebook: 11/5/22

- Continued Pluralsight design patterns course:
    - Started section 3.
    - Created a simple factory package in the folder [`simple`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple) to practice creating a simple factory package (using an `__init__.py`)

---

### :notebook: 11/6/22

- Continued Pluralsight design patterns course:
    - Reviewed section 3.
    - Added Visual Studio Code configuration option to ignore specific `flake8` violations in specific files:
        - Intent is to remove `flake8` warnings in [`__init.py__`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/__init__.py) for [`F401 module imported but unused`](https://flake8.pycqa.org/en/latest/user/error-codes.html).
        - Added the [configuration option](https://9to5tutorial.com/for-beginners-introducing-flake8-to-visual-studio-code) [`--per-file-ignores=days/_83_84/*/__init__.py:F401`](https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-per-file-ignores) to the Visual Studio Code Workspace section in the **Code>Preferences>Settings**  menu.
        - Adds the following JSON to the Workspace `settings.json` file:

            ```json
            {
                "python.linting.flake8Args": [
                    "--per-file-ignores=days/_83_84/*/__init__.py:F401"
                ]
            }
            ```

---

### :notebook: 11/7/22

- Continued Pluralsight design patterns course:
    - Reviewed section 3 content.
- Refactored application layout (directory structure) to mimic the course instructor's example.
    - Moved automobile classes, including the abstract automobile class to the [`autos`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/autos) directory.
    - Performed initial review of the `inspect` module documentation.
        - Gets detailed information about Python objects.

---

### :notebook: 11/8/22

- Continued Pluralsight design patterns course:
    - Reviewed section 3 content.
    - Started initial code framework in [`auto_factory.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/auto_factory.py) file.
        - Requires methods that will populate the `autos` dictionary with a car's model name and class name.

---

### :notebook: 11/9/22

- Completed initial build of [`auto_factory.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/auto_factory/.py).
    - Need to conduct testing to understand the use and return values from`inspect` module methods.

---

### :notebook: 11/10/22

- Conducted review of code in [`auto_factory.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/auto_factory.py) in order to analyze return values from the following code:

    ```python
    import autos as Autos
    from inspect import getmembers

    classes = getmembers(Autos)
    ```

---

### :notebook: 11/11/22

- Continued review of code in [`auto_factory.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/auto_factory.py):
    - Completed analysis of the `load_autos` method and added both docstring and inline comments to describe findings.

    ```python
    def load_autos(self, carname) -> None:
        """ Gets a list of sub-classes in the 'autos' folder.

            The 'getmembers' function retrieves a list of tuples
            for the 'autos' folder.  A lambda function removes all
            objects that are not classes (__doc__, etc.), and not
            abstract classes (AbstractAutomobile).
        """

        # Creates a list of tuples with non-abstract class object in 'autos'
        classes = getmembers(
            Autos,
            # lambda function removes any non-class and abstract class objects
            lambda member: isclass(member) and not isabstract(member)
        )

        # Adds each class name and type (class) to the autos dictionary
        # The _type keyword returns the object type of tuple index 1
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, Autos.AbstractAutomobile):
                self.autos.update([[name, _type]])

        return None
    ```

---

### :notebook: 11/12/22

- Completed initial review of code in [`auto_factory.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/auto_factory.py):
    - Completed analysis of the `create_instance` method and added both docstring and inline comments to describe findings.

    ```python
    def create_instance(
        self,
        carname: str
    ) -> Union(str | Autos.NullCar):
        """ Return an abstract instance of a concrete auto class. """

        # Return an abstract instance of a defined concrete object
        if carname in self.autos:
            return self.autos[carname]
        # Return an abstract instance of NullCar concrete object
        else:
            return Autos.NullCar(carname)
    ```

---

### :notebook: 11/13/22

- Completed initial code in [`__main__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/__main__.py.):
    - Unable to successfully use code, requires further troubleshooting.
    - Returning a `TypeError` exception

        ```bash
        ./__main__.py 
        __init__.py complete.
        Traceback (most recent call last):
        File "/workspaces/100daysofcode/days/_83_84/pluralsight/factory_pattern/simple/./__main__.py", line 25, in <module>
            car.start()
        TypeError: Batmobile.start() missing 1 required positional argument: 'self'
        ```

---

### :notebook: 11/14/22

- Completed code, testing, and review of the [`simple`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple) application.
    - Created an additional class to walk through the process of adding a new auto to the factory.
        - Created the class `Rivian` in the file [`__main__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/__main__.py.).
        - Added the `Rivian` class to [`__main__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/autos/__main__.py.).
        - Added `Rivian` to the `CAR_NAMES` tuple in [`__main__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/__main__.py.).

- Corrected exception from [11/13/22](#notebook-111322) by adding parenthesis to the return value of the `AutoFactory.create_instance` method in [`auto_factory.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/simple/auto_factory.py).
    - The parenthesis are necessary to create an instance of any class.
        - `my_string = str()` returns an instance of a class.
        - `my_string_1 = str` returns a copy of a class.

```python
class AutoFactory(object):
     def create_instance(
        self,
        carname: str
    ) -> Union[str, Autos.NullCar]:
        """ Return an abstract instance of a concrete auto class. """

        # Return an abstract instance of a defined concrete object
        if carname in self.autos:
            return self.autos[carname]() # <<--- Added missing parenthesis here
        # Return an abstract instance of NullCar concrete object
        else:
            return Autos.NullCar(carname)
```

---

### :notebook: 11/15/22

- Completed the Simple Factory Pattern Pluralsight video.
    - Updated Pluralsight Evernote notes and code docstrings.
    - Need to review UML diagram for the Simple Factory Pattern for better understanding.

- Started the Full Factory Pattern Pluralsight video.
    - Need to review UML diagram for the Full Factory Pattern for better understanding.

---

### :notebook: 11/16/22

- Reviewed UML diagrams for the Simple and Full Factory Pattern examples.
- Watched all remaining section 3 lessons in the Pluralsight course.
- Next step is to build the Full Factory Pattern sample application defined in [`full`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full).

---

### :notebook: 11/17/22

- Built initial Python files for the [`full`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full) application:
    - Added factory file for each concrete factory.
    - Modified the [abstract_automobile](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/abstract_automobile.py) file to include the `name` property.

---

### :notebook: 11/18/22

- Started initial build of [loader.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/loader.py).
    - The file will dynamically import the correct concrete factory class, based on the name of the class supplied by the `factory_name` parameter.
        - The `importlib` module provides a mechanism to dynamically import modules.

            ```python
            from importlib import import_module

            import_module(
                name='random'
            )
            ```

    - Established initial code structure although relative module imports are a problem that require further troubleshooting.

---

### :notebook: 11/19/22

- Updated `import` statements in the following files to include absolute or relative paths to imported modules, in an attempt to resolve `ModuleNotFoundError.`
    - [loader.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/loader.py).
    - [lloyd_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/lloyd_factory.py).

    - `import` statement errors require additional troubleshooting.

---

### :notebook: 11/20/22

- Removed relative import `.` characters input statements in the following files:
    - factory_pattern/full/factories/loader.py).
    - [lloyd_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/lloyd_factory.py).
    - [batmobile_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/blined_factory.py).
    - [domino.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/domino_factory.py).
    - [rivian_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/rivian_factory.py).

- Resolved many import errors, further discovery and troubleshooting required.

---

### :notebook: 11/22/22

- Successfully tested - [loader.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/loader.py).
    - Added docstrings, line comments, and type hints.

---

### :notebook: 11/28/22

- Refactored concrete product class modules to use the `self.name` property, inherited from the corresponding concrete factory class modules, to replace hard-coded auto names in `print` functions with `self.name` variables.
- Applicable modules:
    - [batmobile.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/batmobile.py).
    - [domino.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/domino.py).
    - [lloyd.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/lloyd.py).
    - [rivian.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/rivian.py).

    ```python
    # Original syntax example
    class Batmobile(AbstractAutomobile):
        """ Concrete class for instances of the Batmobile. """

        def start(self) -> None:
            print('Starting Batmobile.')

            return None

        def stop(self) -> None:
            print('Stopping Batmobile.')

            return None

    # Updated syntax example
    class RivianFactory(AbstractFactory):
        """ Concrete class for instances of Rivian. """

        def create_auto(self) -> Rivian:
            """ Rivian implementation of the abstract factory class """

            self.rivian = rivian = Rivian()
            rivian.name = 'Rivian'

            return rivian
    ```

- Replaced relative path imports of concrete product class modules from concrete factory modules with absolute path imports, in order to overcome an `ImportError` exception:

    ```python
    # Original syntax example
    from abstract_factory import AbstractFactory
    from autos.rivian import Rivian

    # Updated syntax example
    from abstract_factory import AbstractFactory
    from _83_84.pluralsight.factory_pattern.full.autos.rivian import Rivian
    ```

    ```bash
    # Import error with relative import usage
    ImportError: attempted relative import with no known parent package
    ```

- Applicable modules:
    - [batmobile_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/batmobile_factory.py).
    - [domino_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/domino_factory.py).
    - [lloyd_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/lloyd_factory.py).
    - [rivian_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/rivian_factory.py).

- Modified the [loader.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/loader.py) module to append a suffix of "`_loader`" to the `name` parameter in the `load_factory` function.
    - This matches the concrete factory module names (`batmobile_factory`) when given a concrete product name (`batmobile`):

```python
# Original syntax example
factory_module = import_module(
    name=f'{factory_name}',
    package='factories'
)

# Updated syntax example
factory_module = import_module(
    name=f'{factory_name}_factory',
    package='factories'
)
```

---

### :notebook: 11/29/22

- Updated folder names for brevity:
    - Changed folder name `_83_84/pluralsight/factory_pattern/simple_factory` to `_83_84/pluralsight/factory_pattern/simple`
    - Changed `_83_84/pluralsight/factory_pattern/full_factory` to `_83_84/pluralsight/factory_pattern/full`

- Created the helper functions file [autos_helper.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/autos_helper.py) to limit reuse of code.
    - Added simple `start` and `stop` functions that allows making centralized application-wide changes to `print` output.
    - Refactored the following files to use the new functions:
        - [batmobile.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/batmobile.py).
        - [domino.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/domino.py).
        - [lloyd.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/lloyd.py).
        - [rivian.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/rivian.py).

---

### :notebook: 11/30/22

- Created initial code in [`__main__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/__main__.py.).
    - Running the code produces a number of `ModuleNotFoundError` exceptions.  Further troubleshooting required.

---

### :notebook: 12/1/22

- Modified the `factory_name` argument in the `load_factory` method if [`__main__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/__main__.py.) to include a relative import path prefix of `factories` (for the `factories` sub-directory of `__main__`).

- Modified the [loader.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/loader.py) to include exception handling for both the `ImportError` and the `ModuleNotFoundError` exceptions.
    - Modified the `name` argument in the `import_module` method to include a relative import path prefix of `factories` (for the `factories` sub-directory of `__main__`).

- Modified the `import` statements in the following files from relative to absolute paths:
    - [batmobile_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/factories/batmobile_factory.py).
    - [domino_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/domino_factory.py).
    - [lloyd_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/lloyd_factory.py).
    - [rivian_factory.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/rivian_factory.py).

---

### :notebook: 12/2/22

- Added inline comments to [`__main__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/__main__.py.)

- Refactored the following files to use absolute `import` paths:
        - [batmobile.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/batmobile.py).
        - [domino.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/domino.py).
        - [lloyd.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/lloyd.py).
        - [null_car.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/null_car.py).
        - [rivian.py](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/full/autos/rivian.py).

- Application functions properly.
    - Tested passing a dynamic name value to the `NullCar` concrete product class, to display the name of the car that has no matching concrete factory.
    - Further troubleshooting required.

---

### :notebook: 12/9/22

- Unable to find a way to dynamically insert the name of a car without an explicit, named factory into the output string, `Error, unknown car type "Camry"`.
    - Moving to Abstract factory lesson.

---

### :notebook: 12/12/22

- Completed initial watch of the Abstract Factory Pattern Pluralsight videos.
    - No notes taken, familiarization only.

- Developed initial application framework files including:
    - [`abstract/__main__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/abstract/__main__.py)
    - [`abstract/autos/__init__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/abstract/autos/__init__.py)
    - [`abstract/autos/abs_auto.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/abstract/autos/abs_auto.py)
    - [`abstract/autos/tesla/model_3.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/abstract/autos/tesla/model_3.py)
    - [`abstract/factories/__init__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/abstract/factories/__init__.py)
    - [`abstract/factories/abs_factory.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/abstract/factories/abs_factory.py)

---

### :notebook: 12/14/22

- Re-watched Abstract Factory Pattern Pluralsight videos 1-3.
    - Added overview and pattern structure Evernote notes.

---

### :notebook: 12/15/22

- Re-watched Abstract Factory Pluralsight video 4.
    - Expanded application to support three car models for one car manufacturer.
    - Next step is to expand the application to support three additional car models for one additional car manufacturer, with as little referencing existing materials as possible.

---

### :notebook: 12/16/22

- Expanded the application to support three additional car models (Bolt, Lyriq, & Hummer) for one additional car manufacturer (GM).
    - Updated [`abstract/__main__.py`](https://github.com/timothyhull/100daysofcode/tree/main/days/_83_84/pluralsight/factory_pattern/abstract/__main__.py) to loop over multiple factory classes (for each manufacturer).
    - Next step is to review code, add comments, and understand abstract factory interface flow.

---

### :notebook: 12/17/22

- TODO
