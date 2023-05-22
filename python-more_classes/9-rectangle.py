#!/usr/bin/python3
# Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)


class Rectangle:
    """Rectangle class"""

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
        """width setter: sets the width with new value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >0")
        self.__width = value

    @property
    def height(self):
        """height: returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter: sets the height with new value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >0")
        self.__height = value

    def area(self):
        """area: returns the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter: returns the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height)*2
