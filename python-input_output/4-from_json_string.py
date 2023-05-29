#!/usr/bin/python3
""" A function that returns an object represented by a JSON string
Prototype: def from_json_string(my_str):
You don’t need to manage exceptions if the string doesn’t
represent an object."""


def from_json_string(my_str):
    """ A function that returns an object represented by a JSON string"""
    import json
    return json.loads(my_str)
