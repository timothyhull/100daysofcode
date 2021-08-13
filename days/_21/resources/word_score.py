#!/usr/bin/env python3
""" Score scrabble words
"""

# Imports
from collections import namedtuple

# Define a namedtople to support letter values list
Values = namedtuple('Values', 'value letters')

# Constants
VALUES = [
    Values(1, 'eaoinrtlsu'),
    Values(2, 'dg'),
    Values(3, 'bcmp'),
    Values(4, 'fhvwy'),
    Values(5, 'k'),
    Values(8, 'jx'),
    Values(10, 'qz')
]


def word_score(
    words: list,
    values: list = VALUES
) -> int:
    """ Determine the score of a word, given a list of letter values.

        Args:
            words (list):
                A list of words to score.
            values (list):
                A list of namedtuple objects with int values for each letter

        Returns:
            max_word_score (namedtuple):
                The word with the highest score and its score
    """

    # Initialize the max_word_score variable
    MaxWordScore = namedtuple('MaxWordScore', 'word score')
    max_word_score = MaxWordScore(word='', score=0)

    # Loop over the list of words
    for word in words:

        # Initialize a score at 0
        word_score = 0

        # Loop through the letters in the word to calculate the score
        for letter in word:

            # Loop through the values list to find a letter match
            for v in values:

                # Check for the current letter in the current values index
                if letter in v.letters:
                    word_score += v.value
                    break

        # Set the word score
        if word_score > max_word_score.score:
            max_word_score = MaxWordScore(word=word, score=word_score)

    return max_word_score
