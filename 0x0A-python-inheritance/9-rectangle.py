#!/usr/bin/python3

""" inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a subclass of BaseGeometry """
    def __init__(self, width, height):
        """ instantiation """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """ calculates the area of the rectangle """
        return self.__width * self.__height
    def __str__(self):
        """ returns the print() and str() representation of a rectangle """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
