#!/usr/bin/python3

class Pack():

    smoked = 0
    lost = 0
    landed = 0
    
    def __init__(self, brand="Undefined", size=20, price, label=""):
        self.__brand = brand
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

    def smoke(self, num="1"):
        self.__size -= num
        self.__cost += (self.__unitc * num)
        self.__smoked += num

    def land(self, num="1"):
        self.__size -= num
        self.__cost += (self.__unitc * num)
        self.__landed += num

    def lose(self, num="1"):
        self.__size -= num
        self.__cost += (self.__unitc * num)
        self.__lost += num
    
    def get_cost(self):

class Cigarette(Pack):
    def __init__(self,)