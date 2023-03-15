#!/usr/bin/python3

""" This module defines the base class """
import json


class Base:
    """ The base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = "{}.json".format(clas.__name__)
        myList = []
        if list_objs is None:
            pass
        else:
            
