#!/usr/bin/python3
# Write a class Rectangle that defines a rectangle by:(based on 2-rectangle.py
"""Defined in README.md"""


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
        elif value < 0:
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
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of Rectangle"""
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width
            rectangle_str += "\n"
        return rectangle_str
