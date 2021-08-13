#!/usr/bin/env pytest
""" Test pybite_65.
"""

# Imports
from _21.pybite_65 import get_letter_draw, WORDS, \
                          get_possible_dict_words, _get_permutations_draw, main
from itertools import permutations
from random import randint
from re import search
from string import ascii_lowercase

# Constants
WORDS
DRAW_LENGTH = 7
LETTERS = ascii_lowercase
OUTPUT_TEXT_1 = r'The letter draw is "([A-Z]\s){6}[A-Z]"'
OUTPUT_TEXT_2 = r'The available words from the letter draw are:\n([a-z]\n)+'
OUTPUT_TEXT_3 = r'The word with the maximum score is "[A-Z][a-z]*" '
OUTPUT_TEXT_4 = r'with a score of \d+'


def test_get_letter_draw() -> None:
    """ Test the get_letter_draw function.
    """

    # Assert the return value is a list
    draw = get_letter_draw()
    assert type(draw) == list

    # Assert each item in the list is a lowercase letter
    for letter in draw:
        assert letter in LETTERS


def test_get_possible_dict_words() -> None:
    """ Test the get_possible_dict_words function.
    """

    dict_words = get_possible_dict_words(
        max_perm_size=DRAW_LENGTH
    )

    # Determine if the return value is a list object
    assert type(dict_words) == list

    # Determine if each list item is a valid dictionary word
    for word in dict_words:
        assert word in WORDS
        assert len(word) in range(1, DRAW_LENGTH + 1)


def test_get_permutations_draw() -> None:
    """ Test the _get_permutations_draw function.
    """

    # Get a draw from the function
    letter_draw = _get_permutations_draw(
        draw=get_letter_draw(),
        max_perm_size=randint(1, DRAW_LENGTH)
    )

    # Determine if the return value is a permutations object
    assert type(letter_draw) == permutations

    # Determine if each permutation has a length > 0 and <= DRAW_LENGTH
    for perm in list(letter_draw):
        assert len(perm) in range(1, DRAW_LENGTH + 1)

        # Determine if each character in the return value is a lowercase letter
        for letter in perm:
            assert letter in LETTERS


def test_main(capfd) -> None:
    """ Test the main function
    """

    main()

    # Get the printed output with capfd
    output = capfd.readouterr().out
    print(output)

    # Search output for test strings
    search_1 = search(OUTPUT_TEXT_1, output)
    search_2 = search(OUTPUT_TEXT_2, output)
    search_3 = search(OUTPUT_TEXT_3, output)
    search_4 = search(OUTPUT_TEXT_4, output)

    # Determine if the output meets test criteria
    assert search_1 is not None
    assert search_2 is not None
    assert search_3 is not None
    assert search_4 is not None
