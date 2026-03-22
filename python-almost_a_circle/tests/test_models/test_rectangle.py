#!/usr/bin/python3
"""Unittests for models/rectangle.py"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_basic_init(self):
        r = Rectangle(10, 2, 1, 1, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 12)

    def test_string_validation(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "1")

    def test_value_validation(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
