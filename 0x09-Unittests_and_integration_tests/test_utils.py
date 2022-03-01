#!/usr/bin/env python3
"""Test utils module
"""
from unittest import TestCase
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """Class TestAccessNestedMap
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Method that tests utils.test_access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Method that tests if a KeyError is raised
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    """Class TestGetJson
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, test_payload):
        """Method that tests utils.get_json
        """
        class Mocked(Mock):
            """Mocked class"""
            def json(self):
                """json method mocked"""
                return test_payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), test_payload)


class TestMemoize(TestCase):
    """Class TestMemoize
    """
    def test_memoize(self):
        """Method that tests utils.memoize
        """
        class TestClass:
            """Class TestClass"""
            def a_method(self):
                """Method a_method"""
                return 42

            @memoize
            def a_property(self):
                """Method a_property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
                test_obj = TestClass()
                test_obj.a_property
                test_obj.a_property
                mocked.asset_called_once()


if __name__ == '__main__':
    unittest.main()
