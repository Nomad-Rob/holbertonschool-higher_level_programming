#!/usr/bin/python3
# Define a class Rectangle that defines a rectangle by(based on 3-rectangle.py
"""Defined in README.md"""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """__init__ method that sets the initial values."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be greater than or equal to zero")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be greater than or equal to zero")
        self.__height = value
