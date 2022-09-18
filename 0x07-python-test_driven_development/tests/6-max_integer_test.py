#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        test subclass that inherit from the TestCase parent class
    """
    def text_doc(self):
        """
            test for the length of doc string
        """
        self.assertTrue(len(max_integer.__doc__) > 1)
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 1)

    def test_accurate_result(self):
        """
            test for the accuarcy of the function with Unsigned numbers
        """
        self.assertEqual(max_integer([2, 6, 8]), 8)
        self.assertEqual(max_integer([98, 67]), 98)
        self.assertEqual(max_integer([67]), 67)

    def test_empty_list(self):
        """
            test for empty list passed to the function
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

    def test_None_arg(self):
        """
            test for None passed to the function
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_arg(self):
        """
            test for no argument passed to the function
        """
        self.assertEqual(max_integer(), None)

    def test_negative_values(self):
        """
            test for neagtive numbers passed to the function
        """
        self.assertEqual(max_integer([-65, -54, -2]), -2)
        self.assertEqual(max_integer([-3, -45, -1]), -1)

    def test_signed_numbers(self):
        """
            test for signed numbers passed to the function
        """
        self.assertEqual(max_integer([4, 78, -1, -78, -4, 4]), 78)
        self.assertEqual(max_integer([-5, 5]), 5)

    def test_type_error(self):
        """
            test for type error exception
        """
        with self.assertRaises(TypeError):
            max_integer([1, 5, "c"])
        with self.assertRaises(TypeError):
            max_integer(["osazee", 4])
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_type_result(self):
        """
            test for tge return type of the function
        """
        self.assertIsInstance(max_integer([3, 5]), int)
        self.assertTrue(type(max_integer([5, 7])) is int)


if __name__ == "__main__":
    unittest.main()
