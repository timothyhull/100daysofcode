#!/usr/bin/env python3
"""Fizz Buzz game for TDD testing.  Given a numeric argument...
   If the number is divisible by 3 and 5:
        Return 'Fizz Buzz'
   If the number is divisible by 3:
        Return 'Fizz'
   If the number is divisible by 5:
        Return 'Buzz'
   Otherwise, return the numeric argument

   https://en.wikipedia.org/wiki/Fizz_buzz
"""


def fizz_buzz(number: int) -> str:
    """Fizz Buzz program.

        Args:
            number (int): Integer to evaluate.

        Returns:
            response (str): Response produced from Fizz Buzz evaluation.
    """

    # Confirm the input value is an integer
    try:
        int(number)
    except ValueError as e:
        print(f'{e!r}')
        raise ValueError
    except TypeError as e:
        print(f'{e!r}')
        raise TypeError

    # Determine if the number is divisible by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        response = 'Fizz Buzz'

    # Determine if the number is divisible by 3
    elif number % 3 == 0:
        response = 'Fizz'

    # Determine if the number is divisible by 5
    elif number % 5 == 0:
        response = 'Buzz'

    # If not divisible by 3 and/or 5, return a string of the number
    else:
        response = str(number)

    return response
