#!/usr/bin/python3
# Write a function that prints x elements of a list


def safe_print_list(my_list=[], x=0):
    try:
        for element in my_list[:x]:
            print(element, end=' ')
    except TypeError:
        return 0
    else:
        print()
        return min(x, len(my_list))
