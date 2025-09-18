#!/usr/bin/env python3
import unittest
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test the utils.access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        takes the arguments from the parameterized decorator and tests them
        to find if the result is as expected
        """
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
