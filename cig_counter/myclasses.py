#!/usr/bin/python3

class Pack():

    smoked = 0
    lost = 0
    landed = 0
    
    def __init__(self, brand="Undefined", price=None, size=20, label=""):
        self.__brand = brand
        self.__initsize = size
        self.__size = size
        self.__price = price
        self.__label = label
        self.__unitc = price / size
        self.__cost = 0
        self.__smoked = 0
        self.__landed = 0
        self.__lost = 0
    
    def get_cig_left(self):
        return self.__size

    def smoke(self, num=1):
        self.__size -= num
        self.__cost += (self.__unitc * num)
        self.__smoked += num
        return (self.__unitc * num)

    def land(self, num=1):
        self.__size -= num
        self.__cost += (self.__unitc * num)
        self.__landed += num
        return (self.__unitc * num)

    def lose(self, num=1):
        self.__size -= num
        self.__cost += (self.__unitc * num)
        self.__lost += num
        return (self.__unitc * num)
    
    def get_cost(self):
        return self.__initsize - self.__size

    def __str__(self):
        smoked = self.__initsize - self.__size
        pack = ""
        pack += f"Label : {self.__brand} \n"
        pack += f"Remaining cigarettes : {self.__size}\n"
        pack += f"Cost of smoked cigarettes : {smoked * self.__unitc}"
        return pack

class Cigarette(Pack):
    pass

class Smoker():
    pass