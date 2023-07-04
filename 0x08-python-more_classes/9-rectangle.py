#!/usr/bin/python3
"""9. A square is a rectangle"""


class Rectangle:
    """class for the Rectangle object"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """creates the Rectangle object"""
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")
        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")
        Rectangle.number_of_instances += 1

    def area(self):
        """returns the current rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the current rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """string format of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ''
        return (str(self.print_symbol) * self.__width + "\n") * \
            (self.__height - 1) + (str(self.print_symbol) * self.__width)

    def __repr__(self):
        """String representation of the rectangle for eval"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle... ")

    @property
    def height(self):
        """property to retrieve the height"""
        return self.__height

    @property
    def width(self):
        """property to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property to set the width"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """property to set the height"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to return the largest rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """class method to return square"""
        return cls(size, size)