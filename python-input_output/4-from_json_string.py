#!/usr/bin/python3
""" A function that returns an object (Python data structure)
represented by a JSON string
Prototype: def from_json_string(my_str):
You don’t need to manage exceptions if the JSON string
doesn’t represent an object.
You don’t need to manage file permissions / exceptions."""


def from_json_string(my_str):
    """ A function that returns an object represented by a JSON string"""
    import json
    return json.loads(my_str)
