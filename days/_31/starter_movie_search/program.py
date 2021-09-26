#!/usr/bin/env python3
""" Copied from 100DaysOfCode Repository.
    Functions added by me:
        init_logging
"""

import api
import logbook
import sys
import requests.exceptions


def main():
    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} "
                  f"has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not find server. Check your network connection.")
    except ValueError:
        print("ERROR: You must specify a search term.")
    except Exception as x:
        print("Oh that didn't work!: {}".format(x))


def init_logging(
    filename: str = None
) -> None:
    """ Initialize logging.

        Args:
            filename (str, optional):
                Logging file name.

        Returns:
            None.
    """

    # Set the logging level
    # level = logbook.CRITICAL
    # level = logbook.ERROR
    # level = logbook.WARNING
    # level = logbook.NOTICE
    # level = logbook.INFO
    # level = logbook.DEBUG
    # level = logbook.FATAL
    # level = logbook.NOTSET
    level = logbook.TRACE

    # Set the logging mode based on the absence or presence of a file name
    if filename is None:
        mode = 'stdout'

        # Create a logbook stream handler for stdout
        logbook.StreamHandler(
            stream=sys.stdout,
            level=level
        ).push_application()

    else:
        mode = 'file'

        # Create a logbook handler to write events to a file
        logbook.TimedRotatingFileHandler(
            filename=filename,
            level=level
        ).push_application()

    # Create a logging initialization message
    init_msg = (f'Logging started, level: {level}, '
                f'mode: {mode}.')

    # Start logging
    logger = logbook.Logger(
        name='Startup',
        level=level
    )

    # Use the logger.notice method to insert init_msg into he log
    logger.notice(init_msg)


if __name__ == '__main__':
    init_logging()
    main()
