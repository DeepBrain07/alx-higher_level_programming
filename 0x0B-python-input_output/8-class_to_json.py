#!/usr/bin/python3

""" This module defines a class - JSON function """


def class_to_json(obj):
    """  returns the dictionary description of an object """
    return obj.__dict__
