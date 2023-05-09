#!/usr/bin/env python3

'''Unittest for TestAccessNestedMap'''

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''nested map test'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''unittest function for access nested map'''

        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''unittest for access nested map exception'''

        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''get json unittest'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''unittest for get json'''

        class Mocked(Mock):
            '''mock class'''

            def json(self):
                '''json mocked method'''

                return test_payload

        with patch("requests.get") as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''unittest for memoize'''

    def test_memoize(self):
        '''unittest for memoize'''

        class TestClass:
            '''class for test'''

            def example_method(self):
                '''returns 42'''

                return 42

            @memoize
            def example_property(self):
                '''returns example_method'''

                return self.example_method()

        with patch.object(TestClass, 'example_method') as mocked:
            spec = TestClass()
            spec.example_property
            spec.example_property
            mocked.asset_called_once()
