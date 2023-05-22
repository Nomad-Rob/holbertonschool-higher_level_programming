#!/usr/bin/python3
# Wrtie a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""Defines a Rectangle class
Private instance attributes: width and height
property def width(self): to retrieve it
property def height(self): to retrieve it
property def width(self, value): to set it
property def height(self, value): to set it
"""

class Rectangle:
    """Rectangle class with width and height"""
    def __init__(self, width=0, height=0):
        """Initialize Rectangle with width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
