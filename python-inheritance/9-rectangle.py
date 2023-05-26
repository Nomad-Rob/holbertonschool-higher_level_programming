#!/usr/bin/python3
""" Rectangle class inherits from BaseGeometry class in 7-base_geometry.py
Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
the area() method must be implemented and print() should print, and str()
should return, the following rectangle description:
[Rectangle] <width>/<height>"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """returning the area of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """the area() method must be implemented"""
        return self.__width * self.__height
