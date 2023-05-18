#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 5-square.py)


class Square:
    """Square class."""
    
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method that sets the size and position of the square.
        Args:
            size (int): size of the square.
            position (tuple): position of the square.
        """
        self.size = size
        self.position = position
    