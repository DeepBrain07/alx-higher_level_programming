#!/usr/bin/python3

""" This module defines the class Square """
Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overrides the __str__ """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """ Size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the class Square """
        if args and len(args) != 0:
            attr_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attr_list[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of this class """
        myDict = {}
        attr_list = ['id', 'size', 'x', 'y']
        for key in attr_list:
            myDict[key] = getattr(self, key)
            if key == 'size':
                myDict[key] = getattr(self,'width')
        return myDict
