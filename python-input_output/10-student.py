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


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary representation of a Student instance
         """
        if attrs is None:
            return vars(self)
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = vars(self)[i]
            except Exception:
                pass
        return new_dict
