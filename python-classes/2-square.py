#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 1-square.py)
"""Define a class Square."""


class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0):
        """Initialize Square with size attribute"""
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
