## :calendar: Day 5: 4/27/21 - 5/1/21

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

:white_check_mark: Review `get_movies_by_director` function in PyBite #13 - **4/28/21**

:white_check_mark: Create `top_n_directors_by_movie_count` function in PyBite #13 - **4/28/21**

:white_check_mark: Create `top_n_directors_by_movie_count_and_le_year` function in PyBite #13 - **4/28/21**

:white_check_mark: Create `top_20_rated_directors_desc_order` function in PyBite #13 - **4/29/21**

:white_check_mark: Update `top_20_rated_directors_desc_order` function in PyBite #13 - **4/30/21**

:white_check_mark: Complete PyBite #13 - **5/1/21**

---

## Notes:

#### :notebook: 4/27/21

Counter` objects support standalone creation and can support adding tuples using the augmented assignment operators `+=` (to add additional values) to evaluate with the `most_common` method:

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
#### :rage: 4/30/21

When working with multiple and/or complex data sets, it may be helpful to draw out or have a reference for what the structured data sets looks like to know if they are `dictionaries`, `lists`, `Counters`, etc., in order to access the nested data objects with more simplicity, and less frustration.

#### :notebook: 5/1/21

Structured data types for PyBite #13:

```shell
# Run the program in the interactive shell
ipython -i directors.p
```

```python
# 'directors' object (defaultdict)
directors = get_movies_by_director()
type(directors)
# collections.defaultdict

# Set a director name to test with
director = 'James Cameron'

# 'directors' keys are director names and values are list objects
type(directors[director])
# list

# 'directors' key value list items are namedtuple objects
directors[director]
# [Movie(title='Avatar', year=2009, score=7.9),
#  Movie(title='Titanic', year=1997, score=7.7),
#  Movie(title='Terminator 2: Judgment Day', year=1991, score=8.5),
#  Movie(title='True Lies', year=1994, score=7.2),
#  Movie(title='The Abyss', year=1989, score=7.6),
#  Movie(title='Aliens', year=1986, score=8.4),
#  Movie(title='The Terminator', year=1984, score=8.1)]

# 'movie_scores' keys are movie names, values are scores
movie_scores = defaultdict(float,
            {'Avatar': 7.9,
             'Titanic': 7.7,
             'Terminator 2: Judgment Day': 8.5,
             'True Lies': 7.2,
             'The Abyss': 7.6,
             'Aliens': 8.4,
             'The Terminator': 8.1})

# 'movie_scores' object (defaultdict)
type(movie_scores)
# collections.defaultdict

# Convert 'movie_scores' to 'movies_counter' object (Counter), sorted by average score
movies_counter = Counter(movie_scores).most_common()

# 'movies_counter' Counter object becomes a list of tuples
movies_counter
# [('Terminator 2: Judgment Day', 8.5),
#  ('Aliens', 8.4),
#  ('The Terminator', 8.1),
#  ('Avatar', 7.9),
#  ('Titanic', 7.7),
#  ('The Abyss', 7.6),
#  ('True Lies', 7.2)]

# 
for movie in movies_counter:
    # Loop through the director's list of movies
    for i, mov in enumerate(directors[director]):
        # Try to find the list index of the current movie title
        if movie[0] in mov:
            # When the list index is matched, extract the
            # matching year from the directors object, using
            # the matched index
            year = directors[director][i].year
    # Display the movie year, title, and average score, from the
    # movie_counters Counter
    print(f'{year}] '
            f'{movie[0]:<48}{movie[1]:.2f}')

```

