# :calendar: Day 52: 12/12/2021-12/16/2021

---

## Topics

:clipboard: Parsing RSS feeds with `feedparser`

---

## Resources

:star: `feedparser` on [PyPI](https://pypi.org/project/feedparser/)

:star: [`pytest` mock for the `file.open` function](https://medium.com/@AbhijeetKasurde/pytest-how-to-mock-the-built-in-open-d7c6e50e9984)

---

## Tasks

:white_check_mark: Watch videos 1-4

:white_check_mark: Choose an RSS feed to parse

:white_check_mark: Retrieve an RSS feed

:white_check_mark: Write PyTest tests for [pull_xml.py](app/pull_xml.py)

:white_check_mark: Add docstrings and comments to [pull_xml.py](app/pull_xml.py)

:white_check_mark: Watch video 5

:white_check_mark: Parse an RSS feed with `feedparser`

:white_large_square: Watch video 6

---

## Notes

### :notebook: 12/12/21

- RSS stands for Really Simple Syndication, Rich Site Summary, and RDF (Resource Data Framework) Site Summary.

- Installed `feedparser` from PyPI with Python pip.
    - `pip install -U feedparser`
    - Typically used with the `requests` module, to retrieve RSS content.

- Selected RSS feed:
    - [Department of Veterans Affairs Office of Public and Intergovernmental Affairs RSS Feed](http://www.va.gov/rss/rss_PressRel.asp)

- Created Python application files:
    1. [test_parser.py](tests/test_parser.py) - `pytest` tests for **parser.py**.
    2. [test_pull_xml.py](tests/test_pull_xml.py) - `pytest` tests for **pull_xml.py**.
    3. [parser.py](app/parser.py) - Parser for RSS XML.
    4. [pull_xml.py](app/pull_xml.py) - Pull RSS XML from source with the `requests` module.

---

### :notebook: 12/13/21

- Moved [parser.py](app/parser.py) and [pull_xml.py](app/pull_xml.py) to the `app` subdirectory.
- Created `pytest` tests for the `get_rss_feed` and `write_rss_to_xml` functions in [tests/test_pull_xml.py](tests/test_pull_xml.py).
    - Successfully tested successful mock HTTP request to the VA API.
    - Successfully tested failed (HTTP 400) mock HTTP request to the VA API.
    - Successfully tested mock file open operation on the XML RSS file.

---

### :notebook: 12/14/21

- Added docstrings and comments to [pull_xml.py](app/pull_xml.py).
    - Successfully performed all `pytest` tests.

---

### :notebook: 12/15/21

- Added code to [parser.py](app/parser.py).
    - Imported `feedparser`.
    - It is possible for `feedparser` to collect RSS data from a source feed, although the preferred strategy is to parse from local files, to avoid reliance on an Internet connection to parse.
    - Designated the file to load

- Parsing an RSS XML file with the `feedparser.parse` method.
    - Pass the XML file path to the `feedparser.parse` method.

        ```python
        import feedparser
        XML_FILE = 'rss_data.xml'

        # Use a context manager to load the file contents
        with open(
            file=XML_FILE.
            mode='rt',
            encoding='utf-8'
        )as file:
            rss_data = file.read()

        # Pass the RSS XML data to the parse method
        feed = feedparser.parse(rss_data)
        ```

    - The instructional videos did not use a context manager, which I think is a good practice for reading from a file.

    - The `feedparser.feed` method returns an object attribute named `entries`, which is a `list` of a special dictionary type (`feedparser.util.FeedParserDict`).
        - Each list item is an XML element.
        - A sample of the output is available in the file [example_output/feedparser.feed.py](example_output/feedparser.feed.py.)
        - A `published` attribute of a `feedparser.util.FeedParserDict` object returns the timestamp found in the XML document under the `<pubDate>` tag.
        - The `title` and `link` attributes of a `feedparser.util.FeedParserDict` object return the RSS element title and link, respectively found in the XML document.

---

### :notebook: 12/16/21

- To display information from the object returned by the `feedparser.feed` method is possible using a `for` loop:

    ```python
    import feedparser

    # Pass the RSS XML data to the parse method
    feed = feedparser.parse(rss_data)

    # Loop over the entries key, and display entry attributes
    for entry in feed.entries:
        print(f'{entry.title}')
        print(f'{"=" * len(entry.title)}')
        print(f' - Timestamp: {entry.published}')
        print(f' - Link: {entry.link}\n')
    ```

- Created `pytest` tests for the `read_xml_file` and `parse_rss_xml` functions in [tests/test_parser.py](tests/test_pparser.py).
    - Successfully tested successful mock file open and XML parsing to STDOUT.

- Completed code for [app/parser.py](app/parser.py)