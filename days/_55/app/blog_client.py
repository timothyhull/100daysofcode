#!/usr/bin/env python3
""" HTTP client to interact with the TalkPython blog. """

# Imports - Python Standard Library

# Imports - Third-party
from requests.models import Response
import uplink

# Imports - Local

# Constants
BASE_URL = 'https://consumerservicesapi.talkpython.fm'
BLOG_ENDPOINT = '/api/blog'


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

    @uplink.get(BLOG_ENDPOINT)
    def get_all_entries(self) -> Response:
        """ Get all blog entries.

            Args:
                None.

            Returns:
                _ (requests.models.Response).
                    Response object from the requests package.
        """
