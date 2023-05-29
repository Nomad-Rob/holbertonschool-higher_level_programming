#!/usr/bin/python3
""" A function that returns the JSON representation of an object (string)
Prototype: def to_json_string(my_obj):
You don’t need to manage exceptions if the object can’t be serialized."""


def to_json_string(my_obj):
    """ A function that returns the JSON representation of an object"""
    import json
    return json.dumps(my_obj)
