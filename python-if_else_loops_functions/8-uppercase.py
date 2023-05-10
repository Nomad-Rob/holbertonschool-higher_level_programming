#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:  # Check if lowercase character
            uppercase_char = chr(ascii_val - 32)  # Convert to uppercase ASCII value
            print(uppercase_char, end='')
        else:
            print(char, end='')
    print()  # Print new line
