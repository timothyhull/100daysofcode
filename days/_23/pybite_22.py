#!/usr/bin/env python3
''' Challenge to write a decorator with an argument.
'''

# Imports
from functools import wraps
from typing import Union


def make_html(element):
    ''' Decorator function to pass an HTML element to another
        decorator function.

        Args:
            element (str):
                The name of the HTML element to format with tags.

        Returns:
            argument_decorator (function):
                Function that applies to a decorated function,
            passing the `make_html` decorator function's argument.
            
    '''

    def argument_decorator(decorated_function):
        ''' Decorator function that applies to a decorated function,
            passing the `make_html` decorator function's argument.

            Args:
                decorated_function (function):
                    Function decorated by `make_html`.

            Returns:
                wrapper (function):
                    Function that wraps the decorated function.
        '''

        # Specify @wraps to preserve the decorated function's docstring
        @wraps(decorated_function)
        def wrapper(*args, **kwargs):

            text = decorated_function(*args, **kwargs)
            start_tag = f'<{element}>'
            end_tag = f'</{element}>'
            html = f'{start_tag}{text}{end_tag}'

            return html

        return wrapper

    return argument_decorator


@make_html('p')
@make_html('strong')
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
