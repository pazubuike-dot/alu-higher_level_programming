#!/usr/bin/python3
"""Module for Square unit tests."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

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

    def test_create_square(self):
        """Test create method for Square."""
        s1 = Square(5, 1, 1, 9)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_save_to_file_square(self):
        """Test save_to_file for Square."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_load_from_file_square(self):
        """Test load_from_file for Square."""
        import os
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_square_invalid_types(self):
        """Test Square with invalid types."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1", 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_square_create(self):
        """Test Square.create() logic."""
        s1 = Square(5, 1, 1, 99)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_square_save_empty(self):
        """Test save_to_file with empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_one_arg(self):
        """Test Square initialization with only size."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_square_two_args(self):
        """Test Square initialization with size and x."""
        s = Square(5, 10)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 0)

    def test_square_positional_args(self):
        """Test Square with 1, 2, and 3 positional arguments."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s2 = Square(5, 2)
        self.assertEqual(s2.x, 2)

        s3 = Square(5, 2, 3)
        self.assertEqual(s3.y, 3)
