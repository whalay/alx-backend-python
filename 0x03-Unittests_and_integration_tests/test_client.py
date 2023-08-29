#!/usr/bin/env python3
""" A module to test client.py """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ A class to test the GithubOrgClient class """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json) -> None:
        """ A method to test the org method """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/{}"
                                              .format(org_name))

    def test_public_repos_url(self) -> None:
        """ A method to test the _public_repos_url method """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test"}
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class._public_repos_url, "test")

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url) -> None:
        """ A method to test the public_repos method """
        mock_public_repos_url.return_value = "test"
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = [{"name": "test"}]
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class.public_repos(), ["test"])
            mock_get_json.assert_called_once_with("test")

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, expected_return) -> None:
        """ A method to test the has_license method """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.has_license(repo, license_key),
                         expected_return)


@parameterized_class((
    "org_payload",
    "repos_payload",
    "expected_repos",
    "apache2_repos"),
    [(
        TEST_PAYLOAD[0][0],
        TEST_PAYLOAD[0][1],
        TEST_PAYLOAD[0][2],
        TEST_PAYLOAD[0][3]
    )]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ A class to test the GithubOrgClient class """

    @classmethod
    def setUpClass(cls) -> None:
        """ A method to set up the class """
        config = {'return_value.json.side_effect': [
                    cls.org_payload,
                    cls.repos_payload,
                    cls.org_payload,
                    cls.repos_payload
                ]}
        cls.patcher = patch('requests.get', **config)
        cls.patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """ A method to tear down the class """
        cls.patcher.stop()

    def test_public_repos(self) -> None:
        """ A method to test the public_repos method """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("test"), [])

    def test_public_repos_with_license(self) -> None:
        """ A method to test the public_repos method with license """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
