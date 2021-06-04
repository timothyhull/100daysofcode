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

        return r

    # Catch request exceptions
    except requests.exceptions.RequestException as e:
        print(f'{e!r}')
        raise


def main():
    r = http_request()
    print(r.json())


if __name__ == '__main__':
    main()
