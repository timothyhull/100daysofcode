#!/usr/bin/env python3
""" Simple Flask application. """

# Imports - Python Standard Library

# Imports - Third-Party
from flask import Flask, render_template

# Imports - Local
from _76.flask_app.data import favorite_pizzas

# Create Flask application object for this file
app = Flask(__name__)


# Create a default route function to the Flask app
@app.route('/')
def index() -> str:
    """ Function that operates the web application root path.

        Args:
            None.

        Returns:
            TODO (str):
                Text HTML output from the Jinja2 template rendering of
                index.html.

    """

    # Return HTML text to render as a web page
    return render_template(
        'index.html',
        favorite_pizzas=favorite_pizzas
    )


if __name__ == '__main__':
    # Run the Flask app
    app.run(
        host='localhost',
        port=5000,
        debug=True
    )
