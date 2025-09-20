#!/usr/bin/env python3
import unittest
from parameterized import parameterized
import client
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """test the GithubOrg class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get):
        """
        tests whether the return value of get_json is as
        expected
        """
        org = client.GithubOrgClient(org_name)
        expected = {"payload": True}
        mock_get.return_value = expected
        result = org.org
        self.assertEqual(result, expected)
        mock_get.assert_called_once_with(
            f"https: //api.github.com/orgs/{org_name}")
