#!/usr/bin/env python3
""" HTTP client to interact with the TalkPython blog. """

# Imports - Python Standard Library

# Imports - Third-party
from requests.models import Response
import uplink

# Imports - Local
from _55.app.uplink_helper import handle_http_error

# Constants
BASE_URL = 'https://consumerservicesapi.talkpython.fm'
BLOG_ENDPOINT = '/api/blog'


@handle_http_error
@uplink.json
class BlogClient(uplink.Consumer):
    """ HTTP client for blog API interaction.

        Client to interact with blog posts via the uplink.Consumer method.

        Args:
            uplink.Consumer (uplink.builder.ConsumerMeta):
                Base uplink consumer class, for creating
                custom consumers.
    """

    def __init__(self) -> None:
        """ Initialization method.

        Args:
            None

        Returns:
            None.
        """

        super().__init__(
            base_url=BASE_URL
        )

        return None

    @uplink.get(
        uri=BLOG_ENDPOINT
    )
    def get_all_entries(self) -> Response:
        """ Get all blog entries.

            Args:
                None.

            Returns:
                _ (requests.models.Response)
                    Response object from the requests package.
        """

    @uplink.get(
        uri=f'{BLOG_ENDPOINT}/{{entry_id}}'
    )
    def get_entry(
        self,
        entry_id: str
    ) -> Response:
        """ Get a specific blog entry by ID.

            Args:
                entry_id (str):
                    Blog entry ID.

            Returns:
                _ (requests.models.Response)
                    Response object from the requests package.
        """

    def write_entry(
        self,
        title: str,
        content: str,
        view_count: int,
        published: str
    ) -> Response:
        """ Provide a wrapper to __write_entry with a helpful docstring.

            Args:
                title (str):
                    Blog entry title.

                content (str):
                    Blog entry title.

                view_count (int):
                    Blog entry title.

                published (str):
                    Blog entry title.

            Returns:
                Returns:
                _ (requests.models.Response)
                    Response object from the requests package.
        """

        return self.__write_entry(
            title=title,
            content=content,
            view_count=view_count,
            published=published
        )

    @uplink.post(
        uri=f'{BLOG_ENDPOINT}'
    )
    def __write_entry(
        self,
        **kwargs: uplink.Body
    ) -> Response:
        """ Write a new blog entry.

            Args:
                **kwargs (uplink.Body):
                    Arbitrary keyword arguments that map to the body
                    of the HTTP POST request.

            Returns:
                _ (requests.models.Response)
                    Response object from the requests package.
        """
