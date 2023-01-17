#!/usr/bin/python3

"""Imports the super class Base"""

from models.base import Base

"""Defines a rectangle class that inherits from Base"""


class Rectangle(Base):

    """Module Instantiation with attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the new Rectangle and set attributes
        Args:
            width (int): the width of new rectangle
            height (int): the height of new rectangle
            x (int): the x coordinate of new rectangle
            y (int): the y coordinate of new rectangle
            id (int): the identity/descr num of new rectangle
        Raises:
            TypeError: If either of width or height is not an integer
            ValueError: If either of width or height is less or equal to 0
            TypeError: If either of x or y is not an integer
            ValueError: If either of x or y is less than 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the rectangle"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x coordinate of the rectangle"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y coordinate of the rectangle"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle shape using the '#' character"""
        for x in range(self.__height):
            for y in range(1, self.__width):
                print('#', end="")
            print('#')

    def __str__(self):
        """Return the str() representation of the rectangle"""
        return "[{}] ({}) {}/{}- {}/{}".format(self.__class__.__name__,
                                               self.id, self.__x, self.__y,
                                               self.__width, self.__height)

    def update(self, *args):
        """Update the rectangle with new attributes
        Args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
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
            elif count == 4:
                self.__y = item
            count += 1
