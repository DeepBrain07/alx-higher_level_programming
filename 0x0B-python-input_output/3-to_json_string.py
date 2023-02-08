#!/usr/bin/python3

""" This module defines a JSON representation of an object """
import json


def to_json_string(my_obj):
    """ Returns a JSON representation of my_obj """
    return json.dumps(my_obj)
