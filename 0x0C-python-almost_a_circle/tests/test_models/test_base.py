#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """Test class for Base class"""
    def test_id(self):
        """Test id coherence"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        
    def test_id2(self):
        """Test id coherence"""
        b1 = Base(4)
        b2 = Base(1)
        b3 = Base()
        b4 = Base(3)
        b5 = Base()
        
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 5)


if __name__ == '__main__':
    unittest.main()