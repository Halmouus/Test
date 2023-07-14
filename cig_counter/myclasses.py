#!/usr/bin/python3
from datetime import datetime

class Pack():

    smoked = 0
    lost = 0
    lended = 0
    
    def __init__(self, brand="Undefined", price=None, size=20, label=""):
        self.__brand = brand
        self.__initsize = size
        self.__size = size
        self.__price = price
        self.__label = label
        self.__unitc = price / size
        self.__cost = 0
        self.__smoked = 0
        self.__lended = 0
        self.__lost = 0
    
    @property
    def get_timing(self):
        return datetime.now().strftime('%d/%m/%y %H:%M:%S')
    
    @property
    def get_cig_left(self):
        return self.__size

    def smoke(self, num=1):
        self.__size -= num
        self.__cost += (self.__unitc * num)
        self.__smoked += num
        timing = self.get_timing 
        return [timing, (self.__unitc * num)]

    def lend(self, num=1):
        self.__size -= num
        self.__cost += (self.__unitc * num)
        self.__lended += num
        timing = self.get_timing
        return [timing, (self.__unitc * num)]

    def lose(self, num=1):
        self.__size -= num
        self.__cost += (self.__unitc * num)
        self.__lost += num
        timing = self.get_timing
        return [timing, (self.__unitc * num)]

    @property
    def get_cost(self):
        return self.__initsize - self.__size

    def write_sfile(self, smoker):
        pass

    def __str__(self):
        smoked = self.__initsize - self.__size
        pack = ""
        pack += f"Label : {self.__brand} \n"
        pack += f"Remaining cigarettes : {self.__size}\n"
        pack += f"Cost of smoked cigarettes : {smoked * self.__unitc:.2f}"
        return pack

class Cigarette(Pack):
    pass

clas

class Smoker():
    def __init__(self, name="Unnamed", age="Undefined"):
        self.__name = name
        self.__age = age
        self.__smoker_file = f"{name}.txt"
        with open(self.__smoker_file, 'w') as s_file:
            s_file.write(f"Hey {self.__name}, you're a damn big ass smoker!\n")
            
    @property
    def getname(self):
        return self.__name
    
    @property
    def getfile(self):
        return self.__smoker_file

    def smoke(self, pack, num=1):
        s_record = ""
        record = pack.smoke(num)
        s_record = f"{self.getname} smoked {num} at {record[0]}\n"
        with open(self.getfile, 'a') as s_file:
            s_file.write(s_record)