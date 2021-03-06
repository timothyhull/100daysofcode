#!/usr/bin/env python3
""" Scrabble word finder tool.
    A draw is 7 letters.
"""

# Imports
from itertools import permutations
import os
import urllib.request
# Import `random.choice` to select random letters
from random import choice
# Import `string.ascii_lowercase` to get alphabet letters
from string import ascii_lowercase
from _21.resources.word_score import word_score

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)
LETTERS = ascii_lowercase
NUM_LETTERS = 7

with open(DICTIONARY) as f:
    WORDS = set([word.strip().lower() for word in f.read().split()])


def get_letter_draw(
    letters: str = LETTERS,
    size: int = NUM_LETTERS
) -> list:
    """ Get a list of DRAW_LENGTH random letters from LETTERS.

        Args:
            letters (str):
                String of alphabet letters.
            size (int):
                Number of letters in the random draw.

        Returns:
            draw(list):
                A list of random letters.
    """

    draw = [choice(LETTERS) for _ in range(NUM_LETTERS)]

    return draw


def get_possible_dict_words(
    draw: list = get_letter_draw(),
    max_perm_size: int = NUM_LETTERS
) -> list:
    """ Get all possible words from a draw (list of letters) which are
        valid dictionary words. Use _get_permutations_draw and provided
        dictionary.

        Args:
            max_perm_size (int):
                Maximum permutation size.

        Returns:
            dict_words (list):
                A list of valid words.
    """

    # Create a list for valid words
    dict_words = []

    # Loop over the permutation size range
    for perm in range(1, max_perm_size + 1):
        # Get the permutations for the current max_perm_size iteration
        perms = _get_permutations_draw(
            draw=draw,
            max_perm_size=perm
        )

        # Loop over the current permutations iteration and search for words
        for word in perms:
            join_word = ''.join(word)
            if join_word in WORDS:
                dict_words.append(join_word)

    return dict_words


def _get_permutations_draw(
    draw: list = get_letter_draw(),
    max_perm_size: int = NUM_LETTERS
) -> list:
    """ Helper to get all permutations of a draw (list of letters), hint:
        use itertools.permutations (order of letters matters).

        Args:
            draw(list):
                List of NUM_LETTERS random letters.
            max_perm_size(int):
                Size of the permutation.

        Returns:
            perms (permutations):
                Permutations of NUM_LETTERS random letters.
    """

    perms = permutations(
        iterable=draw,
        r=max_perm_size)

    return perms


def main():
    # Get a draw of letters
    draw = get_letter_draw()
    print(f'\n The letter draw is "{" ".join(draw).upper()}"\n')

    # Get a list of dictionary words
    words = get_possible_dict_words(
        draw=draw
    )
    print('The available words from the letter draw are:')
    for word in words:
        print(word)

    # Determine the word with the highest score
    max_score_word = word_score(words)
    print(f'\nThe word with the maximum score is '
          f'"{max_score_word.word.title()}" '
          f'with a score of {max_score_word.score}\n')


if __name__ == '__main__':
    main()
