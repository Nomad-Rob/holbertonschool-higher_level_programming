#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
and then save them to a file
You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
You don’t need to manage arguments passed to the script (see example below)"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    file = load_from_json_file("add_item.json")
except FileNotFoundError:
    file = []

argc = len(sys.argv)
for i in range(1, argc):
    file.append(sys.argv[i])
save_to_json_file(file, "add_item.json")
