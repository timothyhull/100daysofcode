#!/usr/bin/env python3

# Import the function to test
from hello import hello_name


# Define a function for code testing
def test_hello_name():
    assert hello_name('tim') == 'Hello Tim'
