#!/usr/bin/python3

"""Defines a rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, __width=0, __height=0):
        """Initializing this rectangle class
        Args:
            width: represents width of rectangle
            height: represents height of rectangle
        Raises:
            TypeError: if value is not integer
            valueError: if value is less than zero
        """
        self.width = __width
        self.height = __height

    @property
    def width(self):
        """Retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value