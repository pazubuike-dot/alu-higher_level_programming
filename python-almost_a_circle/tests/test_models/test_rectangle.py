#!/usr/bin/python3
"""Unittests for Rectangle."""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Thorough tests for Rectangle validation and methods."""

    def test_type_validation(self):
        """Test for TypeError on non-integer inputs."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_value_validation(self):
        """Test for ValueError on invalid numbers."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_update_args(self):
        """Test the update method with *args."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, width=1, height=2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/2")
