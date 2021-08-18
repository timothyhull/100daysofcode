#!/usr/bin/env python3
''' Challenge to write a decorator with an argument.
'''

# Imports
from functools import wraps
from typing import Union


def make_html(function, element) -> str:
    ''' Decorator function to add HTML tags to a specified element.

        Args:
            element (str):
                The name of the HTML element to format with tags.

        Returns:
            html (str):
                The original elemented formatted has HTML
    '''

    # Specify @wraps to preserve the decorated function's docstring
    @wraps(function)
    def wrapper(*args, **kwargs):

        text = function(*args, **kwargs)
        start_tag = f'<{element}>'
        end_tag = f'</{element}>'
        html = f'{start_tag}{text}{end_tag}'

        return html

    return wrapper


# @make_html('p')
# @make_html('strong')
def get_text(text: Union[str, int, float] = None) -> str:
    ''' Function to collect text for HTML formatting.

        Args:
            text (str):
                Text to format as HTML.

        Returns:
            text (str):
                Text to format as HTML.
    '''

    if text is None:
        text = input('\nEnter text to format as HTML: ')

    return text
