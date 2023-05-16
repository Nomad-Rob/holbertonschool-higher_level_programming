#!/usr/bin/python3
# Write a function that prints x elements of a list
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return i + 1
    except IndexError:
        print()
        return i
