#!/usr/bin/python3
# Write a class MyList that inherits from list
"""This is a print_sorted method that prints the list
but sorted (ascending sort)"""


class MyList(list):
    """MyList class inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
