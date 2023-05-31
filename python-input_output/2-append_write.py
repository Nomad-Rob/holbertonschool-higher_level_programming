#!/usr/bin/python3
""" A function that appends a string at the end of a text file (UTF8) and
returns the number of characters added
Prototype: def append_write(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions or
file doesn't exist exceptions.
You are not allowed to import any module"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file and"""
    with open(filename, mode='a+', encoding='utf-8') as f:
        counter = f.write(text)
        return counter
