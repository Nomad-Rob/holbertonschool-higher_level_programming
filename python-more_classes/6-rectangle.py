#!/usr/bin/python3
# Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
"""Defines a Rectangle class
Private instance attributes: width
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception with the
message width must be an integer
if width is less than 0, raise a ValueError exception with the
message width must be >= 0
Private instance attribute: height
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception with the
message height must be an integer
if height is less than 0, raise a ValueError exception with the
message height must be >= 0
Public class attribute number_of_instances:
Initialized to 0
Incremented during each new instance instantiation
Decremented during each instance deletion
Public class attribute print_symbol:
Initialized to #
Used as symbol for string representation
Can be any type
Instantiation with optional width and height: def __init__(self, width=0,
height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle
perimeter:
if width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #:
if width or height is equal to 0, return an empty string
repr() should return a string representation of the rectangle to be able to
recreate a new instance by using eval() (see example below)
Print the message Bye rectangle... (... being 3 dots not ellipsis) when an
instance of Rectangle is deleted
You are not allowed to import any module
"""

class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """__init__ method.
        Args:
            width (int): integer width
            height (int): integer height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter: sets the width to a value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """height: returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter: sets the height to a value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        """area: returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter: returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perimeter = (self.__width * 2) + (self.__height * 2)
            return perimeter
