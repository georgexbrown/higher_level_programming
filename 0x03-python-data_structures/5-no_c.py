#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        pass
    else:
        replace = ''
        for char in my_string:
            if char == 'c' or char == 'C':
                char == ''
            replace += char
        return replace
