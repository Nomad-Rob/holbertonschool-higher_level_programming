#!/usr/bin/python3
# Define a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
"""Define a class Rectangle
Private instance attribute: width:
    property def width(self): to retrieve it
    property setter def width(self, value): to set it:
        width must be an integer, otherwise raise a TypeError exception
        with the message width must be an integer
        if width is less than 0, raise a ValueError exception with
        the message width must be >= 0
Private instance attribute: height:
    property def height(self): to retrieve it
    property setter def height(self, value): to set it:
        height must be an integer, otherwise raise a TypeError exception
        with the message height must be an integer
        if height is less than 0, raise a ValueError exception with
        the message height must be >= 0
Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle
perimeter:
    if width or height is equal to 0, perimeter is equal to 0
print() and str() should print the rectangle with the character #: (see example below)
repr() should return a string representation of the rectangle to be able to
recreate a new instance by using eval() (see example below)
You are not allowed to import any module
"""

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
