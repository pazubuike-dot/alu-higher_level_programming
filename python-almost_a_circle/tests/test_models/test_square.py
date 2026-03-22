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

    def test_to_dictionary(self):
        """Test dictionary output for Square."""
        s = Square(10, 2, 1, 9)
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_create_square(self):
        """Test Square create method."""
        s1 = Square(5, 1, 1, 99)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_save_to_file_square(self):
        """Test save_to_file for Square."""
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)
