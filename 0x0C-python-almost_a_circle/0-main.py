#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":
    
    r = Rectangle(5, 3)
    r.display()

    print("---")

    r1 = Rectangle(5, 3, 1, 0)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()