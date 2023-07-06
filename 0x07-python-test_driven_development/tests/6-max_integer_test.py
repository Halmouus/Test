#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_typerr_int(self):
        """Test TypeError when arg is just an integer"""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_typerr_str(self):
        """Test TypeError when the list contains both ints and strs or chars"""
        with self.assertRaises(TypeError):
            max_integer(['a', 5, -1])

    def test_empty(self):
        """Test None output if empty list"""
        result = max_integer([])
        self.assertEqual(result, None)

    def test_singleElement(self):
        """Test output if list has a single element"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_ordered(self):
        """Test the output for a list of positive integers"""
        result = max_integer([0, 5, 8, 12])
        self.assertEqual(result, 12)

    def test_reversed(self):
        """Test the output for a list of positive integers"""
        result = max_integer([12, 8, 5, 0])
        self.assertEqual(result, 12)

    def test_output_random(self):
        """Test the output for a list of positive integers"""
        result = max_integer([5, 0, 12, 8])
        self.assertEqual(result, 12)

    def test_floats(self):
        """Test the output for a list with floats"""
        result = max_integer([5, 0.3, 9.5, 8])
        self.assertEqual(result, 9.5)

    def test_output_negatives(self):
        """Test the output for a list of negative integers"""
        result = max_integer([-5, 0, -12, -8])
        self.assertEqual(result, 0)

    def test_strings(self):
        """Test the output for a list of strings"""
        result = max_integer(["hey", "hello", "bonjour", "bye"])
        self.assertEqual(result, "hey")

    def test_single_string(self):
        """Test the output for a list of negative integers"""
        result = max_integer("Hello word!")
        self.assertEqual(result, "w")


if __name__ == '__main__':
    unittest.main()