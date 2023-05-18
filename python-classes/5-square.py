#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 4-square.py)
"""Define a class Square."""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """__init__ method that sets the size of the square.
        Args:
            size (int): size to set the square to.
        """
        self.__size = size

    @property
    def size(self):
        """size: property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """size: property setter to set it"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
