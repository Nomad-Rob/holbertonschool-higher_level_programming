#!/usr/bin/python3
"""Square class that inherits from Rectangle (9-rectangle.py)
Instantiation with size: def __init__(self, size)
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description:
[Square] <width>/<height>"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle (9-rectangle.py)"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """returning the string representation of the rectangle"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
