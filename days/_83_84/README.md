# :calendar: Days 83+84: 7/10/2022-7/15/2022

---

## Topics

:clipboard: Data Visualization with Plotly

---

## Resources

:star: [Climate Change Indicators Dashboard](https://climatedata.imf.org/pages/access-data)

:star: [Climate Change Indicators Data/Metadata](https://climatedata.imf.org/pages/access-data)

:star: [Atmospheric CO2 Indicators Data](https://climatedata.imf.org/datasets/9c3764c0efcc4c71934ab3988f219e0e/explore)

:star: [Atmospheric CO2 Indicators API Query Info](https://climatedata.imf.org/datasets/9c3764c0efcc4c71934ab3988f219e0e/api)

---

## Tasks

:white_check_mark: Watch videos 8-9

:white_check_mark: Choose project application to develop - graph climate data

:white_check_mark: Develop application outline

:white_check_mark: Integrate with Better Code Hub

:white_check_mark: Setup requirements files

:white_check_mark: Download atmospheric CO2 data set from API source

:white_check_mark: Format atmospheric CO2 data `Date` key as a `datetime.datetime` object

:white_large_square: Write `pytest` tests

:white_large_square: Write application to plot data with `Plotly`

:white_large_square: Test data ploting with `Bokeh`

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

- Created the `convert_date_string` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to convert date strings to `datetime.datetime` objects.
    - Updated the `_get_atmospheric_co2_data` method in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py) to format atmospheric CO2 data `Date` keys as `datetime.datetime` objects, using the `convert_date_string` method.

- Created initial `pytest` file, [tests/test_ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/tests/test_ClimateData.py).
    - Created initial test function `test_convert_date_string` to test the `convert_date_string` in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
    - All tests pass.

---

### :notebook: 7/14/22

- Created the file [web/flask_app.py](https://github.com/timothyhull/climate-data-plotly/blob/main/web/flask_app.py) to run the `Flask` web service.
    - Tested Flask service with string output from an instance of the `ClimateData` class in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).

---

### :notebook: 7/15/22

- Created the HTML template file [web/templates/index.html](https://github.com/timothyhull/climate-data-plotly/blob/main/web/templates/index.html) to test the `render_template` method in [web/flask_app.py](https://github.com/timothyhull/climate-data-plotly/blob/main/web/flask_app.py).

- Created the framework for the `plot_atmospheric_co2_data` function in [app/ClimateData.py](https://github.com/timothyhull/climate-data-plotly/blob/main/app/ClimateData.py).
