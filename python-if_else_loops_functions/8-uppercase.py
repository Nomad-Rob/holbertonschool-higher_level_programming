#!/usr/bin/python3
def uppercase(string):
    output = ''
    for char in string:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:  # Check if lowercase character
            uppercase_char = chr(ascii_val - 32)  # Convert to uppercase ASCII value
            output += uppercase_char
        else:
            output += char
    print("{}".format(output))
