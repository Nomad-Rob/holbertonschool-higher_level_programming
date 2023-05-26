#!/usr/bin/python3
# Write a function that returns the list of
# available attributes and methods of an object
"""This defines the lookup module, which is returning the list
of available attributes and methods of an object"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
