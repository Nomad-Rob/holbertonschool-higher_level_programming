#!/usr/bin/python3
"""BaseGeometry class where public instance method area is
raise an Exception with the message area() is not implemented"""


class BaseGeometry:
    """Just raise an Exception"""
    def area(self):
        """area raises an Exception with the message"""
        raise Exception("area() is not implemented")
