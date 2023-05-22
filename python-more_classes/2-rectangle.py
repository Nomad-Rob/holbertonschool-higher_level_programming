#!/usr/bin/python3
# Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
"""Define a class Rectangle
Private instance attribute: width:
    property def width(self): to retrieve it
    property setter def width(self, value): to set it:
Private instance attribute: height:
    property def height(self): to retrieve it
    property setter def height(self, value): to set it:
Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter:
    if width or height is equal to 0, perimeter is equal to 0

"""

class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """__init__ method that sets the initial values."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: retrieve the value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """width: set width with new value."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >=0')
        self.__width = value

    @property
    def height(self):
        """height: retrieve the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """height: set height with new value."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >=0')
        self.__height = value

    def area(self):
        """area: return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter: return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
