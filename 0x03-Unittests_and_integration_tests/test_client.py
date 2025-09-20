#!/usr/bin/env python3
import unittest
from parameterized import parameterized
import client
from unittest.mock import patch, Mock, PropertyMock


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
        api = "https://api.github.com/orgs"
        org = client.GithubOrgClient(org_name)
        expected = {"payload": True}
        mock_get.return_value = expected
        result = org.org
        self.assertEqual(result, expected)
        mock_get.assert_called_once_with(f"{api}/{org_name}")

    def test_public_repos_url(self):
        """
        tests the public_repos_url whethger it returns the
        required result while mocking the org method
        """
        expected = "https://api.github.com/orgs/google"
        payload = {"repos_url": expected}
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
                 ) as mock_obj:
            client_obj = client.GithubOrgClient("google")
            mock_obj.return_value = payload
            test_result = client_obj._public_repos_url
            self.assertEqual(payload["repos_url"], test_result)
