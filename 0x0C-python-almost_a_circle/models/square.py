#!/usr/bin/python3

"""Imports the super class Rectangle"""

from models.rectangle import Rectangle

"""Defines a square class that inherits from rectangle"""


class Square(Rectangle):

    """Module Instantiation with attributes"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the new Squaree and set attributes
        Args:
            size (int): the length and breadth of new square
            x (int): the x coordinate of new square
            y (int): the y coordinate of new square
            id (int): the identity/descr num of new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square"""
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def __str__(self):
        """Return the str() representation of the square"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.__x, self.__y,
                                             self.__width)

    def update(self, *args, **kwargs):
        """Update the rectangle with new attributes
        Args:
            *args (int)
               - 1st argument should be the id attribute
               - 2nd argument should be the size attribute
               - 3rd argument should be the x attribute
               - 4th argument should be the y attribute

            **kwargs (dict) - key/value pair of attribute
        """
        if args:
            count = 0
            for item in args:
                if count == 0:
                    self.id = item
                elif count == 1:
                    self.__width = item
                elif count == 2:
                    self.__height = item
                elif count == 3:
                    self.__x = item
                count += 1

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.__width = value
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
