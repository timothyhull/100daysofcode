# :calendar: Day 46: 11/16/2021-11/17/2021

---

## Topics

:clipboard: Web Scraping with BeautifulSoup4

---

## Resources

:star: [PyBites Project Page](https://pybit.es/pages/projects.html) (to use for parsing)

---

## Tasks

:white_check_mark: Watch videos 1-2

:white_check_mark: Watch videos 3-4

:white_large_square: TBD

---

## Notes

### :notebook: 11/16/2021

- Watched introductory videos.

---

### :notebook: 11/17/2021

#### The site `https://pybit.es/pages/projects.html'` returns an HTTP 406

- BeautifulSoup4 (BS4) parses HTML content from web pages.
    - Installed with the command `pip install bs4`.
    - Use the `requests` module to download HTML content, and use BS4 to parse the content.
- Steps to parse HTML:
    1. Use `requests` to get content from a URL:
        - `r = requests.get(url)`
    2. Create a BS4 object with the response `.text` object:
        - `soup = bs4.BeautifulSoup(r.text, 'html.parser')`
    3. Get a list of items that match a specific CSS style ('titles' in this case):
        - `items = soup.select('.titles')`

---
