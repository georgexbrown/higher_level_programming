#!/usr/bin/python3

"""Defines class Base"""


class Base:
    """Represents base model for all other classes

    Attributes:
        __nb_objects (int): the number of instantiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the new base and set its attributes
        Args:
            id (int): the identity of the new base
        """
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
