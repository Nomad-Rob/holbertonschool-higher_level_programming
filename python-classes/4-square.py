#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 3-square.py)
"""Define a class Square."""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """__init__ method that sets the size of the square.

        Args:
            size (int): size of Square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """size: property to retrieve it

        Args:
            size (int): size of Square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        Returns:
            self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size: property setter to set it

        Args:
            value (int): size of Square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """area: method that returns the current square area

        Args:
            None

        Returns:
            The area of the square
        """
        return self.__size ** 2
