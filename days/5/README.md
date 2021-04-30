## :calendar: Day 5: 4/27/21 - 4/29/21

---

## Topics:

:clipboard: Practice using movie data

---

## Resources:

:star: PyBite #13 - [Highest Rated Movie Directors](https://pybit.es/codechallenge13.html)

:spiral_notepad: PyBite #13 [data set](https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv)

:telescope: [Solution notebook](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/04-06-collections/collections.ipynb)

:card_file_box: Python `csv.DictReader` [documentation](https://docs.python.org/2/library/csv.html#csv.DictReader)

---

## Tasks:

:white_check_mark: Start work on PyByte #13 - **4/27/21**

:white_check_mark: Review `get_movies_by_director` function in PyBite #13

:white_check_mark: Create `top_n_directors_by_movie_count` function in PyBite #13

:white_check_mark: Create `top_n_directors_by_movie_count_and_le_year` function in PyBite #13

:white_check_mark: Create `top_20_rated_directors_desc_order` function in PyBite #13

:white_large_square: Complete PyBite #13

---

## Notes:

:notebook: `Counter` objects support standalone creation and can support adding tuples using the augmented assignment operators `+=` (to add additional values) to evaluate with the `most_common` method:

```python
# Create a standalone Counter object
c = Counter()

# Add some tuples
c['Tim'] += 41
c['Sara'] += 40
c['Lily'] += 13
c['Ella'] += 10

# Use the most_common method to display the N tuples with the biggest numbers
c.most_common(3)
```
