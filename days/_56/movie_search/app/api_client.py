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
                None.

            Returns:
                _ (requests.models.Response):
                    API response in the form of a Response object from
                    the requests module.

        """

    @uplink.get(
        uri=f'{DIRECTOR_ENDPOINT}/{{director}}'
    )
    def director_search(
        self,
        director: str
    ) -> Response:
        """ Search for movies by director.

            Args:
                None.

            Returns:
                _ (requests.models.Response):
                    API response in the form of a Response object from
                    the requests module.

        """

    @uplink.get(
        uri=f'{IMDB_CODE_ENDPOINT}/{{imdb_code}}'
    )
    def imdb_code_search(
        self,
        imdb_code: str
    ) -> Response:
        """ Search for movies by IMDB code.

            Args:
                None.

            Returns:
                _ (requests.models.Response):
                    API response in the form of a Response object from
                    the requests module.

        """
