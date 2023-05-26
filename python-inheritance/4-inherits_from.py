#!/usr/bin/python3
"""The inherits_from function returns True if the object is an instance of,
oa class that inherited (directly or indirectly) from the specified class;
otherwise False"""


def inherits_from(obj, a_class):
    """inherits_from returns True if the object is an instance of,
    a_class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
