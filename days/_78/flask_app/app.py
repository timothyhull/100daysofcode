#!/usr/bin/env python3
""" Basic Flask form app. """

# Imports - Python Standard Library

# Imports - Third-Party
from flask import (
    Flask, render_template, request
)

# Imports - Local

# Constants

# Flask object
app = Flask('__main__')


# Default route
@app.route(
    '/',
    methods=['GET', "POST"]
)
def index() -> str:
    """ Default route to index.html.

    Args:
        None.

    Return:
        html_text (str):
            HTML text to return to the web browser.
    """

    # Check for form data
    if request.method == 'POST':
        html_text = render_template(
            template_name_or_list='index.html',
            form_data=request.form
        )

    else:
        # Generate index.html from templates/index.html
        html_text = render_template(
            template_name_or_list='index.html',
        )

    return html_text


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5000,
        debug=True
    )
