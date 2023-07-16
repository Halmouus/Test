#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """Test class for Base class"""
    def test_a_id(self):
        """Test id coherence"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 4)
    
    def test_b_duplication(self):
        """Test id coherence and duplication"""
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

    def test_c_special_values(self):
        """Test for special values output"""
        self.assertEqual(Base().id, 7)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-1).id, -1)
        with self.assertRaises(ValueError):
            Base(-1)
        self.assertEqual(Base().id, 8)
    
    def test_d_special_values_2(self):
        """Test for special values output"""
        self.assertEqual(Base().id, 9)
        self.assertEqual(Base("str").id, 'str')
        with self.assertRaises(ValueError):
            Base("str")
        self.assertEqual(Base().id, 10)

    def test_e_class_type(self):
        """Test for type and dictionary representation"""
        self.assertEqual(str(type(Base())), "<class 'models.base.Base'>")
        self.assertEqual(Base().__dict__, {'id': 13})

    def test_f_special_values(self):
        """Test for special values output : lists and tuples"""
        self.assertEqual(Base([10, 20, 30]).id, [10, 20, 30])
        with self.assertRaises(ValueError):
            Base([10, 20, 30])
        self.assertEqual(Base(['a', 'b', 'c']).id, ['a', 'b', 'c'])
        with self.assertRaises(ValueError):
            Base(['a', 'b', 'c'])
        self.assertEqual(Base(('a', 1, 'str', 0, [0, 1, 2])).id, ('a', 1, 'str', 0, [0, 1, 2]))
        with self.assertRaises(ValueError):
            Base(('a', 1, 'str', 0, [0, 1, 2]))

    def test_g_private_attribute_access(self):
        """Test for type and dictionary representation"""
        with self.assertRaises(AttributeError):
            Base().__nb_objects
        with self.assertRaises(AttributeError):
            Base().__id_list
            
if __name__ == '__main__':
    unittest.main()