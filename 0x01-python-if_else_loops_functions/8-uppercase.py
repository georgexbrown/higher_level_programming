#!/usr/bin/python3
def uppercase(str):
    up = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            up += chr(ord(c) - 32)
        else:
            up += c
    print("{}".format(up))
