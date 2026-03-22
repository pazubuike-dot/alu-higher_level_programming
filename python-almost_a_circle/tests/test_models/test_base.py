#!/usr/bin/python3
"""Unittests for models/base.py"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class"""
    
    def test_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_explicit_id(self):
        self.assertEqual(Base(89).id, 89)

    def test_to_json_string(self):
        json_s = Base.to_json_string([{'id': 12}])
        self.assertEqual(type(json_s), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        list_input = [{"id": 89, "width": 10}]
        json_s = Base.to_json_string(list_input)
        self.assertEqual(Base.from_json_string(json_s), list_input)
        self.assertEqual(Base.from_json_string(None), [])
