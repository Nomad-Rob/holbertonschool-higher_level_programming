#!/usr/bin/python3
"""The is_kind_of_class function returns True if the
object is an instance of, or if the object is an instance
of a class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class returns True if the object is an instance of,
    a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
