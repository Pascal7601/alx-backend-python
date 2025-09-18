#!/usr/bin/env python3
import unittest
import utils
from parameterized import parameterized
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",), 1),
        ({"a": 1}, ("a", "b"), 1)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        tests whether the utils.access_nested_map function will return
        a keyerror when the key is not found
        """
        with self.assertRaises(KeyError) as msg:
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ tests the utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        tests the utils.get_json function if it returns values
        as expected when mocked with mock_get instead of requests.get
        """
        fake_res = Mock()
        fake_res.json.return_value = test_payload
        mock_get.return_value = fake_res
        result = utils.get_json(test_url)
        self.assertEqual(result["payload"], test_payload["payload"])
        mock_get.assert_called_once_with(test_url)
