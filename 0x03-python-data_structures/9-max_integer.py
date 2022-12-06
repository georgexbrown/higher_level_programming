def max_integer(my_list=[]):
    if not list:
        return None
    else:
        my_list.sort()
        return my_list[-1]
