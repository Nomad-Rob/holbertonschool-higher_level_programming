#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 5-square.py)

"""Define a class Square."""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square attributes."""
        self.size = size
        self.position = position
        
    @property
    def position(self):
        """Getter for position."""
        return self.__position
    
    @property
    def size(self):
        """Getter for size."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

@position.setter
def position(self, value):
    if not isinstance(value, tuple) or len(value) != 2:
        raise TypeError("position must be a tuple of 2 positive integers")
    elif not isinstance(value[0], int) or value[0] < 0:
        raise TypeError("position must be a tuple of 2 positive integers")
    elif not isinstance(value[1], int) or value[1] < 0:
        raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = value
    
def area(self):
    """Return the current square area."""
    return self.__size ** 2

def my_print(self):
    """Print the square with the # character."""
    if self.__size == 0:
        print()
    else:
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
