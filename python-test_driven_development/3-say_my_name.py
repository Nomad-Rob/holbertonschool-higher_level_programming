#!/usr/bin/python3
"""3-say_my_name.py and tests/3-say_my_name.txt"""


def say_my_name(first_name, last_name=""):
    """
    prints a hello string for a name, handling input errors
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
