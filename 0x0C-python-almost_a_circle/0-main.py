#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle
from models.base import Base

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print(Rectangle(10, 2).__dict__)
    Rect = Rectangle(10, 5)
    print(type(Rect) == Rectangle) 
    print(type(Rect) == Base) 
    print(isinstance(Rect, Rectangle))
    print(isinstance(Rect, Base))