#!/usr/bin/python3
"""Write a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary
representation of a Student instance (same as 8-class_to_json.py)
If attrs is a list of strings, only attribute names contained
in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
