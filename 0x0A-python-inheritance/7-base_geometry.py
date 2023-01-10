#!/usr/bin/python3

"""Defines a class that raises an  exception"""


class BaseGeometry():

    """Raises an exception to indicate not implemented"""

    def area(self):
        raise Exception("area() is not implemented")

    """Raise exceptions at validation error"""

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
