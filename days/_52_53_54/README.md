# :calendar: Day 52+53+54: 12/12/2021-12/24/2021

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

:white_check_mark: Watch video 6

:white_check_mark: Add error checking to parser, to ensure tags are present before printing

:white_check_mark: Watch video 7

:white_check_mark: Email RSS data (do something useful with the RSS data)

:white_check_mark: Write `pytest` tests to support the email program

---

## Notes

### :notebook: 12/12/21

- RSS stands for Really Simple Syndication, Rich Site Summary, and RDF (Resource Data Framework) Site Summary.

- Installed `feedparser` from PyPI with Python pip.
    - `pip install -U feedparser`
    - Typically used with the `requests` module, to retrieve RSS content.

- Selected RSS feed:
    - [Department of Veterans Affairs Office of Public and Intergovernmental Affairs RSS Feed](http://www.va.gov/rss/rss_PressRel.asp)

- Created Python test and application files:
    1. [tests/test_parser.py](tests/test_parser.py) - `pytest` tests for **parser.py**.
    2. [tests/test_pull_xml.py](tests/test_pull_xml.py) - `pytest` tests for **pull_xml.py**.
    3. [app/parser.py](app/parser.py) - Parser for RSS XML.
    4. [pprogull_xml.py](app/pull_xml.py) - Pull RSS XML from source with the `requests` module.

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

---

### :notebook: 12/17/21

- Watched video 6.
- Added `pytest` to [tests/test_parser.py](tests/test_parser.py), to check for an `AttributeError`.

- Added error checking to parser, to ensure tags are present before printing.
- Added TDD `pytest` tests to [tests/test_parser.py](tests/test_parser.py)
- Added TDD code to meet `pytest` test criteria.
    - Uses `pytest.raises` to check for an AttributeError, raised by a missing XML tag.
    - Successfully passed all tests.

---

### :notebook: 12/18/21

- Created new Python test and application files to support sending emails:
    1. [tests/test_send_email.py](tests/test_send_email.py) - `pytest` tests for **send_email.py**.
    2. [app/send_email.py](app/send_email.py) - Email send application.

- Created `pytest` test `test_collect_email_info` to test the `collect_email_info` function.
    - Mocked data for the `input` function as well as the `getpass.getpass` method.
        - Mocking this data successfully required the command `import getpass` in [app/send_email.py](app/send_email.py), instead of `from getpass import getpass`.
        - This is because the `unittest.mock.patch` function required the first argument to reference `getpass.getpass`.
    - Successfully tested the `collect_email_info` function in [app/send_email.py](app/send_email.py).

---

### :notebook: 12/19/21

- Removed collection on the email subject from the `collect_email_info` function.
    - Relocated email subject collection to `create_email_body`.

- Started developing `pytest` tests for the `create_email_body` function [tests/test_send_email.py](tests/test_send_email.py) -

---

### :notebook: 12/20/21

- Updated `pytest` tests in [tests/test_send_email.py](tests/test_send_email.py), to support testing the `test_create_email_body` function.
    - Adjusted the `test_collect_email_info` function and constants to support the required format for `namedtuple` contents (`EmailInfo` and `EmailBody`).
- Updated the `create_email` function in [app/send_email.py](app/send_email.py) to comply with the requirements in the `test_collect_email_info` `pytest` function.
    - Adjusted constants to support the required format for `namedtuple` contents (`EmailInfo` and `EmailBody`).

---

### :notebook: 12/21/21

- Created `pytest` tests in [tests/test_send_email.py](tests/test_send_email.py) to support testing the `test_send_email` function.
    - Created assertion based on a boolean.
- Created the `send_email` function in [app/send_email.py](app/send_email.py) to comply with the requirements in the `test_send_email` `pytest` function.
    - Need to determine how to mock the `smtplib.SMTP` function, to avoid attempting to send an actual email with `pytest`

---

### :notebook: 12/22/21

- Tested sending an email with Gmail using iPython.
    - Created a Gmail app-specific password.
    - Successfully sent an email using functions in [app/send_email.py](app/send_email.py).
- Updated the `test_send_email` in [tests/test_send_email.py](tests/test_send_email.py), to mock a call to `smtplib.SMTP.sendmail`.
    - Unable to successfully mock the `smtplib` object.
    - The email attempts to send with mocked credentials.

---

### :notebook: 12/23/21

- Researched `unittest.mock.patch` to determine how to properly test `smtplib.SMTP.sendmail`.
    - Determined I likely need to create multiple mock objects using `@patch` decorators, one for each of the `smtplib` methods in the `send_email` function.

        1. `SMTP`
        2. `SMTP.ehlo`
        3. `SMTP.starttls`
        4. `SMTP.login`
        5. `SMTP.sendmail`

    - Tests successfully pass with a mock object for each method in the `send_email` function, although the test requires connectivity to Gmail (TCP 587) to pass.
    - Need to determine how to run test with a mock connection to Gmail.
        - Likely requires determining how to pass mock arguments to the `SMTP` method, used as a context manager.

---

### :notebook: 12/24/21

- Conducted extensive testing to properly mock an `smtplib.SMTP` method.
    - Several attempts to adjust the mock object properties still resulted in a connection attempt to the specified SMTP server (smtp.gmail.com).
    - The root cause of the failed mock was importing the `SMTP` module using a `from` keyword.
    - Correcting the problem required that I make the following change in [app/send_email.py](app/send_email.py):

        ```python
        # Remove this line
        from smtplib import SMTP

        # Insert this line
        import SMTP

        # Remove this block
        with SMTP(
            # Define the outgoing mail server
            host='smtp.gmail.com',
            port=587
        ) as conn:

        # Insert this block
        with smtplib.SMTP(
            # Define the outgoing mail server
            host='smtp.gmail.com',
            port=587
        ) as conn:
        ```

    - All tests pass successfully following this change, and no connection attempt to smtp.gmail.com takes place.

        ```bash
        root@50c4c4310ffd:/workspaces/100daysofcode/days/_52_53_54# pytest -v
        ==================================================== test session starts ====================================================
        platform linux -- Python 3.9.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /usr/local/bin/python
        cachedir: .pytest_cache
        rootdir: /workspaces/100daysofcode/days/_52_53_54
        plugins: requests-mock-1.9.3, cov-3.0.0, anyio-3.3.4
        collected 10 items                                                                                                          

        tests/test_parser.py::test_read_xml_file PASSED                                                                       [ 10%]
        tests/test_parser.py::test_parse_rss_xml PASSED                                                                       [ 20%]
        tests/test_parser.py::test_parse_rss_xml_output PASSED                                                                [ 30%]
        tests/test_parser.py::test_parse_rss_xml_errors PASSED                                                                [ 40%]
        tests/test_pull_xml.py::test_get_rss_feed_successful PASSED                                                           [ 50%]
        tests/test_pull_xml.py::test_get_rss_feed_http_error PASSED                                                           [ 60%]
        tests/test_pull_xml.py::test_write_rss_to_xml PASSED                                                                  [ 70%]
        tests/test_send_email.py::test_collect_email_info PASSED                                                              [ 80%]
        tests/test_send_email.py::test_create_email_body PASSED                                                               [ 90%]
        tests/test_send_email.py::test_send_email PASSED                                                                      [100%]

        ==================================================== 10 passed in 0.23s =====================================================

        ```
