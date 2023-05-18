#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 0-square.py)


class Square:
    """Square class."""

    def __init__(self, size):
        """__init__ method that sets the size of the square.

        Args:
            size (int): size of the square.
        """
        self.__size = size
