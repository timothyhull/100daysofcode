#!/usr/bin/env python3
""" API client for the Movie Search application. """

# Imports - Python Standard Library

# Imports - Third-Party
from requests.models import Response
import uplink

# Imports - Local

# Constants
BASE_URL = 'https://movieservice.talkpython.fm/api/'
MOVIE_ENDPOINT = 'search'
DIRECTOR_ENDPOINT = 'director'
IMDB_CODE_ENDPOINT = 'movie'


@uplink.response_handler
def handle_http_error(
    response: Response
) -> Response:
    """ HTTP exception helper for the MovieSearchClient class.

        Args:
            response (requests.models.Response):
                Response object from the requests package.

        Returns:
            response (requests.models.Response)
                Response object from the requests package.
    """

    # Raise a requests.exceptions.HTTPError for any HTTP errors
    response.raise_for_status()

    return response


@handle_http_error
class MovieSearchClient(uplink.Consumer):
    """ Movie Search API client class.

        Args:
            uplink.Consumer (uplink.builder.ConsumerMeta):
                Base uplink consumer class, for creating
                custom consumers.

    """

    def __init__(self) -> None:
        """ Initialization method for the MovieSearchClient class.

            Inherits the uplink.Consumer class and sets a base URL for
            API requests.

            Args:
                None.

            Returns:
                None
        """

        # Inherit the uplink.Consumer class and set a base URL
        super().__init__(
            base_url=BASE_URL
        )

        return None

    @uplink.get(
        uri=f'{MOVIE_ENDPOINT}/{{keyword}}'
    )
    def title_search(
        self,
        keyword: str
    ) -> Response:
        """ Search for movies by title.

            Args:
                keyword (str):
                    Movie keyword search string.

            Returns:
                _ (requests.models.Response):
                    API response in the form of a Response object from
                    the requests module.

        """

    @uplink.get(
        uri=f'{DIRECTOR_ENDPOINT}/{{keyword}}'
    )
    def director_search(
        self,
        keyword: str
    ) -> Response:
        """ Search for movies by director.

            Args:
                keyword (str):
                    Director keyword search string.

            Returns:
                _ (requests.models.Response):
                    API response in the form of a Response object from
                    the requests module.

        """

    @uplink.get(
        uri=f'{IMDB_CODE_ENDPOINT}/{{keyword}}'
    )
    def imdb_code_search(
        self,
        keyword: str
    ) -> Response:
        """ Search for movies by IMDB code.

            Args:
                keyword (str):
                    IMDB code search string.

            Returns:
                _ (requests.models.Response):
                    API response in the form of a Response object from
                    the requests module.

        """
