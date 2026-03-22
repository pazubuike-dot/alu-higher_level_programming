#!/usr/bin/python3
"""Unittests for Square."""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Thorough tests for Square."""

    def test_size_validation(self):
        """Test type and value errors for size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_update_kwargs(self):
        """Test square update with kwargs."""
        s = Square(5, 0, 0, 1)
        s.update(size=10, x=2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 10")
