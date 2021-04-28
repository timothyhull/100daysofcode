#!/usr/bin/env python3

# Imports
from collections import defaultdict, namedtuple
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
                movie = line['movie_title'].replace('`\xa0`', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(movie, year, score)
            directors[director].append(m)

    return directors
