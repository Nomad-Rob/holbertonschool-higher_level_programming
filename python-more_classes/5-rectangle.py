#!/usr/bin/python3
# Wirte a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
"""Define a class Rectangle
Private instance attribute: width:
    - property def width(self): to retrieve it
    - property setter def width(self, value): to set it:
        - width must be an integer, otherwise raise a TypeError exception
            with the message width must be an integer
        - if width is less than 0, raise a ValueError exception with the
            message width must be >= 0
Private instance attribute: height:
    - property def height(self): to retrieve it
    - property setter def height(self, value): to set it:
        - height must be an integer, otherwise raise a TypeError exception
            with the message height must be an integer
        - if height is less than 0, raise a ValueError exception with the
            message height must be >= 0
instantiation with optional width and height:
    def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle
    perimeter:
        - if width or height is equal to 0, perimeter is equal to 0
print() and str() should print the rectangle with the character #:
    - if width or height is equal to 0, return an empty string
repr() should return a string representation of the rectangle to be able to
    recreate a new instance by using eval() (see example below)
Print the message Bye rectangle... (... being 3 dots not ellipsis) when an
    instance of Rectangle is deleted
You are not allowed to import any module
"""

class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """__init__ method that sets the intance's width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to get the value width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set the value width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """Method to get the value height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set the value height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        """Method to compute the area rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Method to compute the perimeter rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Method to print the rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Method to return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
