#!/usr/bin/python3
"""2. First Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class for the Rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation with id, width, height, x and y"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """property to retrieve the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """property to set the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """property to set the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """property to retrieve x"""

        return self.__x

    @x.setter
    def x(self, value):
        """property to set x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property to retrieve y"""

        return self.__y

    @y.setter
    def y(self, value):
        """property to set y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value