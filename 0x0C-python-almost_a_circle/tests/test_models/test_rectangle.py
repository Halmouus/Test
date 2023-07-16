#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTestCase(unittest.TestCase):
    """Test class for Rectangle class"""
    def test_a_positional_arguments(self):
        """Test positional argument validation"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
            
    def test_a_the_ids(self):
        """Test id coherence and duplication
        and the validity of types and values"""
        self.assertEqual(Rectangle(10, 9).id, 1)
        self.assertEqual(Rectangle(10, 9, 0, 0, None).id, 2)
        self.assertEqual(Rectangle(10, 9).id, 3)
        self.assertEqual(Rectangle(10, 9, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(10, 9, 0, 0).id, 4)
        with self.assertRaises(ValueError):
            Rectangle(10, 9, 0, 0, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 9, 0, 0, 1)
        with self.assertRaises(ValueError):
            Rectangle(10, 9, 0, 0,12)
        self.assertEqual(Rectangle(10, 9, 0, 0, 5).id, 5)
        self.assertEqual(Rectangle(10, 9, 0, 0).id, 6)
        with self.assertRaises(ValueError):
            Rectangle(10, 9, 0, 0, 6)
        self.assertEqual(Rectangle(10, 9, 0, 0, 5000).id, 5000)
        with self.assertRaises(ValueError):
            Rectangle(10, 9, 0, 0, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 9, 0, 0, 5000)
        
        
    def test_b_width(self):
        """Test width value validation"""
        with self.assertRaises(TypeError):
            Rectangle('str', 9, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 9, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(-4, 9, 0, 0)
        self.assertEqual(Rectangle(10, 9, 0, 0).id, 7)
            
            
    def test_c_height(self):
        """Test height value validation"""            
        with self.assertRaises(TypeError):
            Rectangle(5, 'str', 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, -5, 0, 0)
        self.assertEqual(Rectangle(10, 9, 0, 0).id, 8)
            
    def test_d_x(self):
        """Test x value validation"""            
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 'str', 0)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 0)
        self.assertEqual(Rectangle(5, 10, 4, 0).id, 9)
            
    def test_e_y(self):
        """Test y value validation"""         
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 0, 'str')
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 0, -1)
        self.assertEqual(Rectangle(5, 10, 0, 4).id, 10)
        
    def test_f_type(self):
        """Test type of Rectangle"""
        self.assertEqual(str(type(Rectangle(10, 5))), "<class 'models.rectangle.Rectangle'>")
        self.assertEqual(Rectangle(10, 5).__dict__,
        {'_Rectangle__width': 10, '_Rectangle__height': 5,
         '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 13}) 
    
    def test_g_type(self):
        "Test type and isinstance"
        self.assertTrue(type(Rectangle(10, 5)) == Rectangle)
        self.assertFalse(type(Rectangle(10, 5)) == Base)
        self.assertTrue(isinstance(Rectangle(10, 5), Rectangle))
        self.assertTrue(isinstance(Rectangle(10, 5), Base))
        
        
if __name__ == '__main__':
    unittest.main()