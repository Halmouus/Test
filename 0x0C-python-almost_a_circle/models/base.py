#!/usr/bin/python3
"""1. Base class module"""


class Base:
    """class for the Base object"""
    __nb_objects = 0
    __id_list = []
    
    def __init__(self, id=None):
        """Instantiation with id"""
        if id is not None:
            if id in Base.__id_list:
                raise ValueError(f"{id} already exists")
            self.id = id
            Base.__id_list.append(id)
        else:
            Base.__nb_objects += 1
            while(Base.__nb_objects in Base.__id_list):
                Base.__nb_objects += 1
            self.id = Base.__nb_objects
            Base.__id_list.append(self.id)