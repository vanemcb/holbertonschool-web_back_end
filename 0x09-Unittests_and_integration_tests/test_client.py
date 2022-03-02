#!/usr/bin/env python3
"""Test client module
"""
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Class TestGithubOrgClient
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """Method that tests that GithubOrgClient.org returns the
        correct value
        """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once
