#!/usr/bin/python3
# Write a function that returns a list wiith all values multiplied by a number
# without using any loops
def mutiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
