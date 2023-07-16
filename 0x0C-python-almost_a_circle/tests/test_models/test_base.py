#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """Test class for Base class"""
    def test_id(self):
        """Test id coherence and duplication"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 4)
        with self.assertRaises(ValueError):
            Base(3)
        with self.assertRaises(ValueError):
            Base(1)
        with self.assertRaises(ValueError):
            Base(12)
        self.assertEqual(Base(5).id, 5)
        self.assertEqual(Base().id, 6)
        with self.assertRaises(ValueError):
            Base(6)
        self.assertEqual(Base(5000).id, 5000)
        with self.assertRaises(ValueError):
            Base(3)
        with self.assertRaises(ValueError):
            Base(5000)

if __name__ == '__main__':
    unittest.main()