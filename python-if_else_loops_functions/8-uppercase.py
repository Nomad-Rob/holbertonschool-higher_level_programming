#!/usr/bin/python3
def uppercase(string):
    output = ''
    for char in string:
        ascii_val = ord(char)
        # Check if lowercase character
        if 97 <= ascii_val <= 122:
            # Convert to uppercase ASCII value
            uppercase_char = chr(ascii_val - 32)
            output += uppercase_char
        else:
            output += char
    print("{}".format(output))
