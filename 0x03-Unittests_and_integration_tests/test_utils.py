#!/usr/bin/env python3

'''Unittest for TestAccessNestedMap'''

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(inittest.TestCase):
    '''nested map test'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, ested_map, path, expected):
        '''unittest function for access nested map'''

        self.assertEqual(access_nested_map(nested_map, path), expected)
