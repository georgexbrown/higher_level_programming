#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        pass
    else:
        table = {67:None, 99:None}
        return my_string.translate(table)
