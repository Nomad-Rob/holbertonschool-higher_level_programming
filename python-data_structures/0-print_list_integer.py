#!/usr/bin/python3
# Write a function that prints all integers of a list.
# Prototype: def print_list_integer(my_list=[]):

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))