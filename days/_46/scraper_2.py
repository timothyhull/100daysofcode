#!/usr/bin/env python3
""" Web scraping application #2 using BS4. """

# Imports - Python Standard Library
from os import path

# Imports - Third-Party
import bs4
# import requests

# Constants
# URL = 'https://pybit.es/articles/'
CURRENT_DIR = path.dirname(__file__)
HTML_DIR = 'html'
HTML_FILE = 'articles.html'
HTML_PATH = path.join(
    CURRENT_DIR,
    HTML_DIR,
    HTML_FILE
)


def get_html() -> str:
    """ Pull text/HTML content from a local file.

        Args:
            None.

        Returns:
            html_text (str):
                Text/HTML website content.
    """

    with open(
        file=HTML_PATH,
        mode='rt',
        encoding='utf-8'
    ) as file:
        html_text = file.read()

    return html_text


def scrape(markup_text: str) -> None:
    """ Pull text/HTML content from a website.

        Args:
            markup_text:
                Raw HTML markup text to parse.

        Returns:
            project_headings (List):
                List of all project headings that match the CSS class
                named '.projectHeader'.
    """

    return None


def main() -> None:
    """ Main program.

        Args:
            None.

        Returns:
            None.
    """

    return None


if __name__ == '__main__':
    main()
