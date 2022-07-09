# :calendar: Day 82: 7/6/2022

---

## Topics

:clipboard: Data Visualization with Plotly

---

## Resources

:star: [Pybites RSS feed](https://pybit.es/feed)

:star: [`Plotly` on PyPI](https://pypi.org/project/plotly)

:star: [`Plotly` documentation](https://plotly.com/python)

:star: [`feedparser` on PyPI](https://pypi.org/project/feedparser)

:star: [`feedparser` documentation](https://feedparser.readthedocs.io/en/latest)

:star: [Getting Started with Plotly for Python](https://plot.ly/python/getting-started)

---

## Tasks

:white_check_mark: Watch videos 1-3

:white_check_mark: Watch video 4

:white_check_mark: Watch video 5

:white_large_square: Read [Getting Started with Plotly for Python](https://plot.ly/python/getting-started)

---

## Notes

### :notebook: 7/6/22

- Watched videos 1-3.
- Setup [`plotly.ipynb`](https://github.com/timothyhull/100daysofcode/blob/main/days/_82/plotly.ipynb) for lesson notes and testing Python code.
    - Created the function `convert_to_datetime` to convert date formatted strings to `datetime.datetime` objects.
    - Created the function `get_category` to extract an RSS feed entry from its `link` key.

---

### :notebook: 7/7/22

- Watched video 4.
- Created data sets to plot in [`plotly.ipynb`](https://github.com/timothyhull/100daysofcode/blob/main/days/_82/plotly.ipynb) using `Counter` objects:
    - Set 1 is the number of RSS entries per month.
    - Set 2 is the number of RSS entries per category.
    - Set 3 is the number time tags appear in RSS entries.

---

### :notebook: 7/8/22

- Watched video 5.
- Created the `transpose_data_for_graphing` function in [`plotly.ipynb`](https://github.com/timothyhull/100daysofcode/blob/main/days/_82/plotly.ipynb).
    - Converted `posts_by_month`, `category_counts`, and `tag_counts` to data that can form `x` and `y` axises.
