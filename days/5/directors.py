#!/usr/bin/env python3

# Imports
from collections import defaultdict, namedtuple, Counter
from csv import DictReader
from urllib.request import urlretrieve

# Constants
DATA_SET_FILE_NAME = 'movies.csv'
DATA_SET_URL = ('https://raw.githubusercontent.com/'
                'sundeepblue/movie_rating_prediction/'
                'master/movie_metadata.csv')

# Download data set to file
urlretrieve(DATA_SET_URL, DATA_SET_FILE_NAME)

# Define a namedtuple to store the data in a logical way
Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=DATA_SET_FILE_NAME):
    """Function to extract all movies from the CSV data set and store them
    in a dictionary.  Keys are directors, values are lists of movies,
    as namedtuples.
    """

    # Create a defaultdict for the directors
    directors = defaultdict(list)

    # Open data set as a CSV and convert to a dictionary
    with open(data, 'rt', encoding='utf-8') as file:
        for line in DictReader(file):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(movie, year, score)
            directors[director].append(m)

    return directors


def top_n_directors_by_movie_count(directors: dict, count: int = 5):
    """Function to display the top number of directors from a dictionary of
    dictionaries where keys are director names and values are namedtuples
    with movie title, release year, and IMDB score.
    """

    # Create a Counter object to store the directors dictionary keys/values
    c = Counter()

    # Populate the Counter object with with tuples
    # The first tuple index is the director name
    # The second tuple index is the length of the movies list for that director
    for director, movies in directors.items():
        c[director] += len(movies)

    # Count the top N directors, by number of movies
    top_n = c.most_common(count)

    return top_n


def top_n_directors_by_movie_count_and_le_year(
    directors: dict,
    year: int,
    count: int = 5,
):
    """Function to display the top number of directors from a dictionary of
    dictionaries where keys are director names and values are namedtuples
    with movie title, release year, and IMDB score.  Filter by operator
    of less than or equal to a specific year.
    """

    # Create a Counter object to store the directors dictionary keys/values
    c = Counter()

    # Populate the Counter object with with tuples
    for director, movies in directors.items():
        # Loop over the list of Movies namedtuples for each director
        for m in movies:
            # Filter any movies that do not match the criteria
            if m.year <= year:
                # The first tuple index is the director name
                # The second tuple index is the number of movies
                # for that director that match the comparision criteria
                c[director] += 1

    # Count the top N directors, by number of movies that met the criteria
    top_n = c.most_common(count)

    return top_n


def top_20_rated_directors_desc_order(directors: dict):
    """Print the top 20 highest rated directors with their movies ordered
    desc on rating."""

    # Create a Counter to score a tuple of director and their average score
    director_avg = Counter()

    # Loop over the directors dictionary
    for director, movies in directors.items():
        # Calculate the total score as the sum of every score for each movie
        # Loop over the movies list to calcualte the sum
        total_score = sum(m.score for m in movies)

        # Calculate the total movies as the length of the movies list
        total_movies = len(movies)

        # Divide the total score by the total movies and round to two decimals
        avg_score = round(total_score / total_movies, 2)

        # Add a key/value to the director_average counter
        director_avg[director] += avg_score

    # Get the top 20 directors from the counter
    top_20_directors = director_avg.most_common(20)

    # Convert the Counter tuples to namedtuples
    DirAvgScore = namedtuple('DirAvgScore', 'director avg_score')

    # Loop over the Counter (list of tuples) with enumeration, to indices
    for index, value in enumerate(top_20_directors):
        # Convert each tuple to a namedtuple by passing each unpacked
        # list item (a tuple) as arguments to the DirAvgScore namedtuple
        # e.g. top_20_directors[0] = DirAvgScore(value[0], value[1])
        top_20_directors[index] = DirAvgScore(*value)

    # Loop over the Counter and print each director and their average score
    print()
    for index, value in enumerate(top_20_directors):
        print(f'{index + 1:02d}. {value.director:<50}'
              f'{value.avg_score:.2f}\n'
              f'{"-" * 58}')

        # Sort movies for any director with more than one film
        # Look up the number of movies for the current director by length
        # of the list of movies in the 'directors' object
        if len(directors[value.director]) > 1:
            # Create a default dictionary to store movies and their scores
            movie_scores = defaultdict(float)
            for movies in directors[value.director]:
                movie_scores[movies.title] = movies.score

            # Convert movie_scores to a Counter object and sort by score
            # using the most_common method
            movies_counter = Counter(movie_scores).most_common()

            # Loop over the counter and display the year for the current
            # iteration by looking up the year based on the movie title
            for movie in movies_counter:
                # Loop through the director's list of movies
                for i, mov in enumerate(directors[value.director]):
                    # Try to find the list index of the current movie title
                    if movie[0] in mov:
                        # When the list index is matched, extract the
                        # matching year from the directors object, using
                        # the matched index
                        year = directors[value.director][i].year
                # Display the movie year, title, and average score, from the
                # movie_counters Counter
                print(f'{year}] '
                      f'{movie[0]:<48}{movie[1]:.2f}')

        # For directors with only one film
        # Display director movie data, from the directors dictionary
        else:
            for movies in directors[value.director]:
                print(f'{movies.year}] {movies.title:<48}{movies.score:.2f}')
        print()
