#!/usr/bin/env python3

# Imports
import requests

# Constants
HEADERS = {
    'Accept': 'application/json'
}
URL = 'https://jsonplaceholder.typicode.com/posts/1'
TIMEOUT = 3


def http_request(url=URL):
    try:
        r = requests.get(
            url=url,
            headers=HEADERS,
            timeout=TIMEOUT
        )

        r.raise_for_status()

        return r

    # Catch raise_for_status exceptions
    except requests.exceptions.HTTPError as e:
        print(f'{e!r}')
        raise

    # Catch connection timeouts
    except requests.exceptions.ConnectTimeout as e:
        print(f'{e!r}')
        raise

    # except requests.exceptions.InvalidHeader as e:
    #     print(f'{e!r}')
    #     raise


def main():
    r = http_request()
    print(r.json())


if __name__ == '__main__':
    main()
