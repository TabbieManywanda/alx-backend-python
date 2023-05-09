#!/usr/bin/env python3

'''Unittest for client'''

import unittest
import json
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''class to implement test_org method'''

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        '''unittest for org'''

        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)

    @parameterized.expand([
        ('random-url', {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        '''unittest for public repos url'''

        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        '''unittest for public repos'''

        payload = [{'name': 'Google'}, {'name': 'TT'}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = 'world'
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ['Google', 'TT'])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, key, expectation):
        '''unittest for has license'''

        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expectation)


@parameterized_class([
    'org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'],
    TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''integration class test'''

    @classmethod
    def setUpClass(cls):
        '''class method to set up'''
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''class method to tear down'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''unittest for public repos'''

    def test_public_repos_with_license(self):
        '''test public with license'''


if __name__ == '__main__':
    unittest.main()
