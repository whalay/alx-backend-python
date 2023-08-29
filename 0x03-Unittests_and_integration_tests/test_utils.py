#!/usr/bin/env python3
""" Contains functions to test utils.py """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
)


class TestAccessNestedMap(unittest.TestCase):
    """ A class to test the function access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """ Test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any) -> None:
        """ Test that a KeyError is raised for the following inputs """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ A class to test the function get_json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """ Test that utils.get_json returns the expected result """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ A class to test the function memoize """

    def test_memoize(self) -> None:
        """ Test the memoize functiion decorator """
        class TestClass:
            """ A class to test memoize """
            def a_method(self) -> int:
                """ A method that returns 42 """
                return 42

            @memoize
            def a_property(self) -> int:
                """ A property that returns what a_method returns """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test = TestClass()
            test.a_property
            test.a_property
            mock_method.assert_called_once
            self.assertEqual(test.a_property, mock_method.return_value)
