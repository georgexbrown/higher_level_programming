#!/usr/bin/python3

import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON serialization of list of dict
        Args:
            list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Returns JSON serialization of list of dict
        Args:
            list_objs (list): a list of inherited base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as jsonFile:
            if list_objs is None:
                jsonFile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonFile.write(Base.to_json_string(list_dicts))
