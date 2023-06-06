#!/usr/bin/python3
""" This module is a unittest for the Rectangle class """

import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle class """
    def setUp(self):
        """ Set up test method """
        print("Rectangle setUp")

        self.capture_output = io.StringIO()
        sys.stdout = self.capture_output

        self.rectangle = Rectangle(1, 1)

        # Reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Tear down test method """
        print("Rectangle tearDown")

        sys.stdout = sys.__stdout__

        del self.rectangle
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    # Test id assignment and if it increments correctly
    def test_id(self):
        """ Test __init__ method:
        id assignment in the Rectangle class.
        """
        print(f"Actual id: {self.rectangle.id}")
        self.assertEqual(self.rectangle.id, 1)
        rectangle2 = Rectangle(50, 50)
        print(f"Actual id: {rectangle2.id}")
        self.assertEqual(rectangle2.id, 1)
        rectangle3 = Rectangle(1, 1)
        print(f"Actual id: {rectangle3.id}")
        self.assertEqual(rectangle3.id, 2)

    # Test too many arguments in the init method
    def test_too_many_args(self):
        """
        Test too many arguments in the init method
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1, 1, 1, 1)

    def test_rectangle_creation(self):
        """ Test Rectangle creation """
        # Basic rectangle
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        # Rectangle with x
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

        # Rectangle with y
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

        # Rectangle with id
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

        # Rectangle with negative width
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4, 5)

        # Rectangle with negative height
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4, 5)

        # Rectangle with negative x
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4, 5)

        # Rectangle with negative y
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4, 5)

        # Rectangle with zero width
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2, 3, 4, 5)

        # Rectangle with zero height
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0, 3, 4, 5)
            
    def test_area (self):
        """Test area() method"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)
        
    def test_display(self):
        """Test display() method"""
        r = Rectangle(2, 2)
        
        expected = "##\n" \
                     "##\n"
        r.display()
        self.assertEqual(self.capture_output.getvalue(), expected)
        
    def test_update_args(self):
        """Test update() method with *args"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
    
    def test_update_kwargs(self):
        """Test update method with **kwargs"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=10, width=10, height=10, x=10, y=10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        
    def test_to_dictionary(self):
        """Test to_dictionary() method"""
        r = Rectangle(10, 2, 1, 9)
        expected_dict = {'id' : 1, 'width' : 10, 'height' : 2, 'x' : 1, 'y' : 9}
        self.assertEqual(r.to_dictionary(), expected_dict)
