# :calendar: Days 83+84: 7/10/2022-7/31/2022

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

---

## Tasks

:white_check_mark: Watch videos 8-9

:white_check_mark: Choose project application to develop - graph climate data

:white_check_mark: Develop application outline

:white_check_mark: Integrate with Better Code Hub

:white_check_mark: Setup requirements files

:white_check_mark: Download atmospheric CO2 data set from API source

:white_check_mark: Format atmospheric CO2 data `Date` key as a `datetime.datetime` object

:white_check_mark: Write method to initialize `Plotly` in offline mode

:white_check_mark: Write method to format climate data for X and Y-axis plotting.

:white_large_square: Write `pytest` tests

:white_large_square: Write application to plot data with `Plotly`

:white_large_square: Test data plotting with `Bokeh`

:white_large_square: Publish application in `Flask` app

:white_large_square: Setup basic `Flask` web service

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
    - Created initial test function `test__convert_date_string` to test the `_convert_date_string` in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
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
