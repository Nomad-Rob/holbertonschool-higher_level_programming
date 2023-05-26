#!/usr/bin/python3
"""BaseGeometry based on 6-base_geometry.py has a public instance method
area() that raises an Exception with the message area() is not implemented
also Public instance method integer_validator(self, name, value) that
validates value
Name is always a string
if value is not an integer: raise a TypeError exception, with the message
<name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message
<name> must be greater than 0"""


class BaseGeometry:
    """BaseGeometry class where public instance method area is
    raise an Exception"""
    def area(self):
        """area raises an Exception with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """is validating integer and biger than 0"""
        if type(name) is not str:
            raise TypeError("{} must be a string".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
