#!/usr/bin/env python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("Last digit: {}".format(last_digit))
    return last_digit
