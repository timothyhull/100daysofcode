#!/usr/bin/env python3
""" uplink client helpers. """

# Imports - Python Standard Library

# Imports - Third-party
from requests.models import Response
import uplink

# Imports - Local


@uplink.response_handler
def handle_http_error(
    response: Response
) -> Response:
    """ HTTP exception helper for the BlogClient class.

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
