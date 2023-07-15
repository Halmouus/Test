#!/usr/bin/python3
"""1. Base class module"""


class Base:
    """class for the Base object"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Instantiation with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects