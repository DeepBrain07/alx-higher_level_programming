#!/usr/bin/python3

""" This module defines a class Student """


class Student:
    """ Representation of a Student """
    def __init__(self, first_name, last_name, age):
        """ Initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        myDict = {}
        if type(attrs) == list:
            for key in attrs:
                if key in self.__dict__:
                    myDict[key] = self.__dict__[key]
            return myDict
        return self.__dict__
