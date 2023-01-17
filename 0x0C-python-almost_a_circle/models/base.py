#!/usr/bin/python3

"""Defines class Base"""
import json


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

    @staticmethod
    def from_json_string(json_string):
        """Returns the deserialization of a JSON string
            Args:
                json_string (list): a JSON string representing a list of dicts
            """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instantiated from a dictionary attribute
        Args:
            **dictionary (dict): key/value of attribute to initialize
        """
        if dictionary:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
