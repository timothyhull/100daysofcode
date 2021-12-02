#!/usr/bin/env python3
""" Web scraping application #2 using BS4. """

# Imports - Python Standard Library
from os import path
from typing import List

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
TITLE_SEARCH_PATH = 'h2.entry-title'


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


def scrape_titles(markup_text: str) -> List:
    """ Display text embedded in nested tags.

        Args:
            markup_text:
                Raw HTML markup text to parse.

        Returns:
            title_text (List):
                A list of parsed titles.
    """

    # Create a BS4 object
    soup = bs4.BeautifulSoup(markup_text, 'html.parser')

    # Get a BS4 record set
    titles = soup.select(TITLE_SEARCH_PATH)

    # Strip out all of the HTML surrounding each article, leaving only the text
    title_text = []
    for item in titles:
        title_text.append(item.string)

    return title_text


def main() -> None:
    """ Main program.

        Args:
            None.

        Returns:
            None.
    """

    # Scrape the HTML for article titles
    html = get_html()
    titles = scrape_titles(html)

    for title in titles:
        print(title.string)

    return None


if __name__ == '__main__':
    main()
