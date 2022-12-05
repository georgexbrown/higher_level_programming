#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        pass
    else:
        text = ''.join([char if char not in 'cC' else '' for char in my_string])
        return text
