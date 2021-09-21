#!/usr/bin/env python3

# Imports
import re

# Constants


def extract_course_times():
    '''Use re.findall to capture all mm:ss timestamps in a list'''
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')

    times_regex = re.compile(
        r'''
        \d{2}   # Two digits
        :       # Literal :
        \d{2}   # Two digits
        ''',
        re.VERBOSE
    )

    times = times_regex.findall(
        string=flask_course
    )

    return times


def split_on_multiple_chars():
    '''Use re.split to split log line by ; , .
       but not on the last ... so list should have len of 4
       (hint check re.split docs for extra switches)'''
    logline = ('2017-11-03T01:00:02;challenge time,regex!.'
               'hope you join ... soon')

    logline_list = re.split(
        pattern=r'(?:;|,|\.)',
        string=logline,
        maxsplit=3
    )

    return logline_list


def get_all_hashtags_and_links():
    '''Use re.findall to extract the URL and 2 hashtags of this tweet'''
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')

    tweet_regex = re.compile(
        r'''
        (?:         # Start non-capturing group
        http://     # Literal http://
        \S+         # One or more non-space characters
        |           # Bitwise OR
        \#          # Literal #
        \S+         # One or more non-space characters
        )           # End non-capturing group
        ''',
        re.VERBOSE
    )

    tweet_result = tweet_regex.findall(
        string=tweet
    )

    return tweet_result


def match_first_paragraph():
    '''Use re.sub to extract the content of the first paragraph (excl tags)'''
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')

    html_text = re.sub(
        pattern=r'<p>(.+)</p>(.+)',
        repl=r'\1',
        string=html
    )

    return html_text


def find_double_words():
    '''Use re.search(regex, text).group() to find the double words'''
    text = 'Spain is so nice in the the spring'

    text_result = re.search(
        pattern=r'''
        (       # Start capture group #1
        \b      # Word boundary #1
        \w+     # One or more word characters
        )       # End capture group #1
        # Capture group #1 matches any full word, no surrounding spaces
        \s      # Single space character
        \b      # Word boundary #2
        \1      # Result of capture group #1
        # \s, followed by the \b, followed by \1 matches repeat words
        ''',
        string=text,
        flags=re.VERBOSE
    )

    return text_result.group()


def match_ip_v4_address(ip):
    '''Use re.match to match an ip v4 address (no need for exact IP ranges)'''

    ip_address = re.match(
        pattern=r'''
        ^                       # Start of line
        (                       # Start capture group #1
        [1-2]?                  # 0 or 1 occurrences of 1-2
        [0-9]?                  # 0 or 1 occurrences of 0-9
        [0-9]                   # 0-9
        )                       # End capture group #1
        # Capture group #1 matches an IP address, no numeric range checking
        (?:                     # Start non-capture group #1
        \.                      # Literal .
        [1-2]?[0-9]?[0-9]?      # Reuse previous IP address match
        )                       # End non-capture group #1
        {3}                     # Repeat non-capture group #1 three times
        $                       # End of line
        ''',
        string=ip,
        flags=re.VERBOSE
    )

    return ip_address
