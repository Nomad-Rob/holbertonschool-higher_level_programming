#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 2-square.py)
""""Defines a class square"""


class Square:
    """Square class with a private attribute -
    size.
    """

    def __init__(self, size=0):
        """Initializes the size variable as a private
        instance artribute
        """
        self.__size = size

    @property
    def size(self):
        """Getter property to get the size of the
        square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter property to set the size of the
        square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("ize must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns the
        current square area.
        """
        return self.__size ** 2
