#!/usr/bin/env python3
""" Web scraping application using BS4. """

# Imports - Python Standard Library

# Imports - Third-Party
from typing import List
import bs4
import requests

# Constants
URL = 'https://pybit.es/pages/projects.html'


def pull_site() -> str:
    """ Pull text/HTML content from a website.

        Args:
            None.

        Returns:
            markup_text (str):
                Text/HTML website content.
    """

    # Get page content
    markup_text = requests.get(
        url=URL
    )

    # Check for HTTP error response codes
    markup_text.raise_for_status()

    return markup_text.text


def scrape(markup_text: str) -> List:
    """ Pull text/HTML content from a website.

        Args:
            markup_text:
                Raw HTML markup text to parse.

        Returns:
            project_headings (List):
                List of all project headings that match the CSS class
                named '.projectHeader'.
    """

    # List for project headings
    project_headings = []

    # Create BS4 object
    soup = bs4.BeautifulSoup(
        markup=markup_text,
        features='html.parser'
    )

    # Capture project headings HTML using the 'projectHeader' CSS class
    # <h3 class='projectHeader'>1. #100DaysOfCode</h3>
    html_project_headings = soup.select('.projectHeader')

    # Populate the project_headings list with the text between HTML tags
    for headings in html_project_headings:
        project_headings.append(headings.get_text())

    for heading in project_headings:
        print(heading)

    return project_headings


def main() -> None:
    """ Main program.

        Args:
            None.

        Returns:
            None.
    """

    site = pull_site()
    headings = scrape(site)

    print()
    for index, heading in enumerate(headings):
        print(f'{index}. {heading}')
    print()

    return None


if __name__ == '__main__':
    main()
