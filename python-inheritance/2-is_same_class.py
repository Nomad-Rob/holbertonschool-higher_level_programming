#!/usr/bin/python3
# Wrtie a function that returns True if the object is
# exactly an instance of the specified class ; otherwise False
"""The is_same_class function returns True if the
object is exactly an instance"""


def is_same_class(obj, a_class):
    """is_same_class function returns True if the object
    is exactly an instance of the specified class such as int, float, etc"""
    if type(obj) is a_class:
        return True
    else:
        return False
