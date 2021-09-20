#!/usr/bin/env python3

# Imports
import re

# Constants
COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')
TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')
HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """

    time_match = re.compile(
        r'''
        \d{2}   # Two digits
        :       # Literal :
        \d{2}   # Two digits
        ''',
        re.VERBOSE
    )

    time_list = time_match.findall(
        string=course
    )

    return time_list


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """

    link_hashtag_match = re.compile(
        r'''
        (?:       # Start non-capturing group
        http://   # Literal match of http://
        [a-z\./-] # Character class for a-z and literals . / -
        +         # Match 1 or more of the previous character class
        |         # Bitwise OR operator
        \#        # Literal # character
        [a-z]     # Character class for a-z
        +         # Match 1 or more of the previous character class
        )         # End non-capturing group
        ''',
        re.IGNORECASE | re.VERBOSE
    )

    link_hashtag_list = link_hashtag_match.findall(
        string=tweet
    )

    return link_hashtag_list


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """

    html_match = re.compile(
        r'''
        <p>     # Literal match of <p>
        (     # Start non-capturing group
        .+?     # Match one or more characters with non-greedy (?) quantifier
        )       # End non-capturing group
        </p>    # Literal match of </p>
        ''',
        re.VERBOSE
    )

    html_match_string = html_match.search(
        string=html
    )

    return html_match_string.group(1)


def main():
    extract_course_times()
    get_all_hashtags_and_links()
    match_first_paragraph()


if __name__ == '__main__':
    main()
