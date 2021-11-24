# :calendar: Day 46: 11/16/2021-11/17/2021

---

## Topics

:clipboard: Web Scraping with BeautifulSoup4

---

## Resources

:star: [PyBites Project Page](https://pybit.es/pages/projects.html) (to use for parsing)

:star: [PyBites Articles Page](https://pybit.es/articles/) (to use for parsing)

---

## Tasks

:white_check_mark: Watch videos 1-2

:white_check_mark: Watch videos 3-4

:white_check_mark: Watch videos 5-6

:white_large_square: Watch videos 7-8

---

## Notes

### :notebook: 11/16/2021

- Watched introductory videos.

---

### :notebook: 11/17/2021

#### The site `https://pybit.es/pages/projects.html` returns an HTTP 406

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

### :notebook: 11/23/2021

#### The site `https://pybit.es/articles/` returns an HTTP 406

- Workaround for HTTP 406 error is to save the HTML source to the **./html/articles.html** folder.
- To search a `bs4.BeautifulSoup` object for page elements that match a specific HTML tag.
    - Use the built-in search function by specifying an HTML tag attribute of a `bs4.BeautifulSoup` object:

    ```python
    # Create a BS4 object from raw HTML
    soup = bs4.BeautifulSoup(html_text, 'html.parser')

    # Reference a tag name as an attribute of the BS4 object to search for matches
    soup.h2  # This would search for the first H2 tag element

    # Searching for sub-attributes is possible too
    soup.h2.a
    ```

    - BS4 only returns the first matching tag, it does not return all matching tags.
    - The `soup.find_all` method can return all matching items:

     ```python
    # Create a BS4 object from raw HTML
    soup = bs4.BeautifulSoup(html_text, 'html.parser')

    # Use the `soup.find_all` method to locate all H2 elements
    soup.find_all('h2')
    ```
