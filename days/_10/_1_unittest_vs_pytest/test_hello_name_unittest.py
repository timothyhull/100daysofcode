#!/usr/bin/env python3

# Imports
import unittest

# Import the function to test
from hello import hello_name


# Create a `class` for code testing
class TestHello(unittest.TestCase):

    # Define a function for code testing
    def test_hello_name(self):
        """Use the 'assertEqual' method to call the `hello_name` function
        look for a specific result"""
        self.assertEqual(hello_name('tim'), 'Hello Tim')


# Run the test when the __name__ is __main__
if __name__ == '__main__':
    unittest.main()
