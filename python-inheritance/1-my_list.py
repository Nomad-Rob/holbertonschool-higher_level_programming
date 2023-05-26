#!/bin/bash/python3
# Write a class MyList that inherits from list
"""This is a print_sorted method that prints the list
but sorted (ascending sort)"""


class MyList(list):
    """MyList class inherits from list"""
    def print_sorted(self):
        """print_sorted method"""
        print(sorted(self))
