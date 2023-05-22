#!/usr/bin/python3
# Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """__init__ method that sets the intial values."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: returns width."""
        return self.__width

    @width.setter
    def width(self, value):
        """width: sets width if value is valid."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """height: returns height."""
        return self.__height

    @height.setter
    def height(self, value):
        """height: sets height if value is valid."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        """area: returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter: returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__width + self.__height)

    def __str__(self):
        """__str__: returns the string representation."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """__repr__: returns the representation of the object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
