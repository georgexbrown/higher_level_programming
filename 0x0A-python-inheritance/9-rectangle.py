#!/usr/bin/python3

"""Imports the super class BaseGeometry"""

Rectangle = __import__('7-base_geometry').BaseGeometry

"""Defines a sub class"""


class Rectangle(BaseGeometry):

    """Module instantiation with width and height"""

    def __init__(self, width, height):
        """validating and privatizing width and height
        Args:
            width: width of object
            height: height of object
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of class Rectangle"""

        return self.__width * self.__height

    def str(self):
        """Returns rectangle description for printing"""

        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__width, self.__height)
