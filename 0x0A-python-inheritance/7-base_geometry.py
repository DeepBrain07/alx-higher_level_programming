#!/usr/bin/python3
""" A Geometry class """


class BaseGeometry:
    """ Calculates base geometry """
    def area(self):
        """ raises an Exception with the message
           'area() is not implemented' """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
