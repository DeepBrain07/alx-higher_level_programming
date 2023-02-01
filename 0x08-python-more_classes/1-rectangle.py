#!/usr/bin/python3
""" A 'Rectangle' class """

class Rectangle:
    """ this represents a rectangle """

    def __init__(self, width=0, height=0):
        """ Initializing the class
        Args:
            width: represents the width of the triangle
            height: represents the height of the triangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """ retrieves width attribute """
        return self.__width
    @width.setter
    def width(self, value):
        """ sets width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves height attribute """
        return self.__height
    @height.setter
    def height(self, value):
        """ sets height attribute """
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value
